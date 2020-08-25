#! /use/bin/python3

import socket

TCP_IP="192.168.181.190"
TCP_PORT=6996
BUFFER_SIZE=100

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))
s.listen(s)

conn, addr = s.accept()
print('Connection address:', addr)

while s:
    data=conn.recv(BUFFER_SIZE)
    if not data:break
    print("Received data:", data)
    conn.send(data) #echo

conn.close
