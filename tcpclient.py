# -*- coding: utf-8 -*-
import socket

user = input(">> ")

thost = user
tport =  9999

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((thost,tport))
    msg = input(">>> ")
    msg = msg.encode("utf-8")
    client.send(msg)
    response = client.recv(1024)
    print(response)
