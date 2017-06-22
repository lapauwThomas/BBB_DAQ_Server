
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        timestamp = ''.join('{:02x} '.format(x) for x in data[len(data)-4:len(data)] )
        print("ts",timestamp, "\n")
        for j in range(0, 17):
            cCount = ''.join('{:02x} '.format(x) for x in data[28*j:28*j+4] )
            hex_string = ''.join('{:02x} '.format(x) for x in data[28*j+4:28*j+28] )
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

