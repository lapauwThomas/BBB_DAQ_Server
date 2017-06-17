'''
Created on 16 Jun 2017

@author: thoma
'''
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("UDP Client ", self.client_address,"sent: "  , ''.join('{:02x} '.format(x) for x in data), "\n");
        hex_string = ''.join('{:02x} '.format(x) for x in data)
        out.write(hex_string +"\n")
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    server = socketserver.UDPServer(("192.168.7.1",1520), MyUDPHandler)
    print("UDP Server is booting")
    out =  open('out.txt', 'w')
    server.serve_forever()