# -*- coding: utf-8 -*-

import socket
import threading

bip = "0.0.0.0"
bport = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bip,bport))

server.listen(5)

print(f"Listening on {bip},{bport}")

def handle_client(client_socket):
    req = client_socket.recv(1024)

    print(req.decode("utf-8"))

    client_socket.send(b"ACK".encode("utf-8"))
    
    client_socket.close()


while True:
    client,addr = server.accept()
    print(client)
    client_hand = threading.Thread(target=handle_client,args=(client,))
    client_hand.start()
