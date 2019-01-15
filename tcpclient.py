# -*- coding: utf-8 -*-
import socket

user = input("サーバー側のIPを入力>> ")

thost = user
tport =  9999

while True:
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((thost,tport))
  msg = input(">> ")
  client.send(msg.encode("utf-8"))
  res = client.recv(1024)
  print(res.decode("utf-8"))
