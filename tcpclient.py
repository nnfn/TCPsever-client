# -*- coding: utf-8 -*-
import socket


thost = "127.0.0.1"
tport =  1234

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((thost,tport))
    msg = input(">> ")
    if msg == "exit":
        client.close()
        break
    client.send(msg.encode("utf-8"))
    res = client.recv(1024)
    print(res.decode("utf-8")) # てす

