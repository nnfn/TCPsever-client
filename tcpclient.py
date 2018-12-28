import socket

thost = "127.0.0.1"
tport =  9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((thost,tport))
msg = input(">>> ")
msg = msg.encode()
client.send(msg)
response = client.recv(1024)
print(response)