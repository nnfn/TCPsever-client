# -*- coding: utf-8 -*-

import socket
import threading

bip = "127.0.0.1"
bport = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bip,bport))

server.listen(5)

print(f"Listening on {bip},{bport}")

def handle_client(client_socket):
    req = client_socket.recv(1024)

    print(f"res{req}")

    client_socket.send(b"ACK!")

    client_socket.close()

while True:
    client,addr = server.accept()
    print(client)
    client_hand = threading.Thread(target=handle_client,args=(client,))
    client_hand.start()