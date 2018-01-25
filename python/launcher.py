#!/usr/bin/env python3

#import sys
import subprocess
import socket
import re
import shlex

def openConnection(mysock,size):
    conn, addr = mysock.accept()
    conn.settimeout(30)
    while True:
        try:
            data = conn.recv(size)
        except socket.timeout:
            print("Connection Closed Due To Timeout")
            closeConnection(conn)
            return None
        if not data:
            break
        if (data == "acks-42".encode() or data == "acks-42\n".encode()):
            closeConnection(conn)
            return 'exit'
        match = re.search(r'^c: run station (.{1,})$',data.decode().rstrip())
        if match:
            ret=raydioStart(match.group(1))
            print(ret)
            conn.send((ret+"\n").encode()[:1024])
        else:
            print("Received: "+data.decode().rstrip())
            conn.send(("Received: "+data.decode()).encode())
    closeConnection(conn)
    print("Connect Closed")
    return None
def closeConnection(oldSock):
    oldSock.shutdown(socket.SHUT_RD)
    oldSock.close()
def raydioStart(station):
    command="ls -l "+shlex.quote(station)
    command=shlex.split(command)
    return("Returnning before doing anything")
    try:
        p = subprocess.Popen(command,shell=False,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
        output = p.communicate()[0]
    except:
        return("Station Not Valid")
    if output:
        return("Success")
    else:
        return("")

TCP_IP='0.0.0.0'
TCP_PORT=8887
BUFFER_SIZE=1024

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(1)

while True:
    ret = openConnection(sock,BUFFER_SIZE)
    if ret == 'exit':
        break
closeConnection(sock)
print("Socket Closed")
