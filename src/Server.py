'''
Created on 10 May 2017

@author: thoma
'''
print("Server is booting")


import socketserver
from threading import Thread

class service(socketserver.BaseRequestHandler):
    def handle(self):
        data = 'dummy'
        print( "Client connected with ", self.client_address)
        while len(data):
            data = self.request.recv(1024)
            #self.request.send(data)
            print("Client:",self.client_address, "sent", data)

        print("Client exited")
        self.request.close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

t = ThreadedTCPServer(("192.168.7.1",1520), service)
t.serve_forever()


# import socket
# import threading
# 
# class ThreadedServer(object):
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         self.sock.bind((self.host, self.port))
# 
#     def listen(self):
#         self.sock.listen(5)
#         while True:
#             client, address = self.sock.accept()
#             client.settimeout(60)
#             threading.Thread(target = self.listenToClient,args = (client,address)).start()
# 
#     def listenToClient(self, client, address):
#         size = 1024
#         while True:
#             try:
#                 data = client.recv(size)
#                 if data:
#                     # Set the response to echo back the recieved data 
#                     response = data
#                     client.send(response)
#                 else:
#                     raise error('Client disconnected')
#             except:
#                 client.close()
#                 return False
# 
# if __name__ == "__main__":
#     while True:
#         port_num = input("Port? ")
#         try:
#             port_num = int(port_num)
#             break
#         except ValueError:
#             pass
# 
#     ThreadedServer('',port_num).listen()