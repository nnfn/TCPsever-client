# -*- coding: utf-8 -*-
import socket

bip = "0.0.0.0"
bport = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bip,bport))

server.listen(1)

print(f"Listening on {bip},{bport}")

def handle_client():
    while True:
        conn, addr = server.accept()
        req = conn.recv(1024)
        if not req:
            conn.shutdown(1)
            break
        print(req.decode("utf-8"))
        user = input(">> ")
        if user == "exit":
            conn.shutdown(1)
            break
        conn.send(user.encode("utf-8"))

if __name__ == '__main__':
    handle_client()
