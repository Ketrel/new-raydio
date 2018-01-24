#!/usr/bin/env python3

import sys
import socket
import re

def openDrawer(mysock,size):
    conn, addr = mysock.accept()
    conn.settimeout(30)
    while True:
        try:
            data = conn.recv(size)
        except socket.timeout:
            print("Connection Closed Due To Timeout")
            tooCrusty(conn)
            return None
        if not data:
            break
        if (data == "admin-command-kill-server 42".encode() or data == "admin-command-kill-server 42\n".encode()):
            tooCrusty(conn)
            return 'exit'
        match = re.match(r'^command: run station (.{1,})$',data.decode().rstrip())
        if match:
            conn.send("".join(["Recieved Special Command To Launch: ",match.group(1),"\n"]).encode())
        else:
            print("".join(["Received: ",data.decode('utf-8').rstrip()]))
            conn.send("".join(["Received: ",data.decode('utf-8')]).encode())
    tooCrusty(conn)
    print("Connect Closed")
    return None
def tooCrusty(oldSock):
    oldSock.shutdown(socket.SHUT_RD)
    oldSock.close()



TCP_IP='0.0.0.0'
TCP_PORT=8887
BUFFER_SIZE=1024

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(1)

while True:
    ret = openDrawer(sock,BUFFER_SIZE)
    if ret == 'exit':
        break
tooCrusty(sock)
print("Socket Closed")
