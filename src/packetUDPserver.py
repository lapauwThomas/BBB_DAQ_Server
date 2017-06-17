'''
Created on 16 Jun 2017

@author: thoma
'''
'''
Created on 16 Jun 2017

@author: thoma
'''
import socketserver




class MyUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
#         print("UDP Client ", self.client_address,"sent: \n"  , ''.join('{:02x} '.format(x) for x in data), "\n");
        timestamp = ''.join('{:02x} '.format(x) for x in data[len(data)-4:len(data)] )
        print("ts",timestamp, "\n")
        for j in range(0, 16):
            cCount = ''.join('{:02x} '.format(x) for x in data[28*j:28*j+4] )
            hex_string = ''.join('{:02x} '.format(x) for x in data[28*j+5:28*j+28] )
            linetext = cCount + "      "+  hex_string+ "       "+ timestamp
            outFile.write(linetext+"\n")
            outFile.flush()
            print("UDP Client ", self.client_address,"sent: ", linetext, "\n")
        socket.sendto(data.upper(), self.client_address)


server = socketserver.UDPServer(("192.168.7.1",1520), MyUDPHandler)
print("UDP packet Server is booting")
global outFile
outFile =  open('outFile.txt', 'w')
server.serve_forever()

   