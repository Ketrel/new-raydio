#!/usr/bin/env python3

#import sys
import subprocess
import socket
import re
import shlex

#from contextlib import contextmanager
#@contextmanager
#def activeConnection(connection):
#    try:
#        yield
#    except socket.timeout:
#        print("Connection Timed Out")
#    finally:
#        print("Connection Closed")
#        connection.shutdown(socket.SHUT_RD)
#        connection.close()

class activeConnection():
    def __init__(self, connection):
        self.connection = connection
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.connection.shutdown(socket.SHUT_RD)
        self.connection.close()
        if args[0] == socket.timeout:
            print("Connection Timed Out")
            return True
        else:
            print("Connection Closed")

def openConnection(mysock,size,regs):
    conn, addr = (mysock.accept())
    with activeConnection(conn):
        conn.settimeout(30)
        while True:
            data = conn.recv(size)
            if not data:
                break
            else:
                matched = False
                matchedKey = None
                for key,reg in enumerate(regs):
                    match = reg.search(data.decode())
                    if match:
                        matched = True
                        matchedKey = key
                        break;
                if matched:
                    if matchedKey == 0:
                        ret=raydioStart(match.group(1))
                        print(ret)
                        conn.send((ret+"\n").encode()[:1024])
                    elif matchedKey == 1:
                        return 'exit'
                else:
                    print("Received: "+data.decode().rstrip())
                    conn.send(("Received: "+data.decode()).encode())
    return None

def raydioStart(station):
    match = re.search(r"^[a-zA-Z0-9_-]+$",station)
    if not match:
        #This shouldn't ever happen since the regex that passes checks
        # to call this function should catch it, but just to be safe...
        return("Command Contains Invalid Characers")
    command="/usr/bin/liquidsoap /stationScripts/"+station
    return("Returnning before doing anything\nWhen Live, Would Run: '"+command+"'")
    command=shlex.split(command)
    #try:
    #    p = subprocess.Popen(command,shell=False,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    #    output = p.communicate()[0]
    #except:
    #    return("Station Not Valid")
    #if output:
    #    return("Success")
    #else:
    #    return("")

TCP_IP='0.0.0.0'
TCP_PORT=8887
BUFFER_SIZE=1024
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((TCP_IP,TCP_PORT))
    sock.listen(1)

    #acks-42 = admin-command-kill-server-42
    regs=(
            re.compile(r'^c: run ([a-zA-Z0-9_-]+)\n?$'),
            re.compile(r'^acks-42\n?$'),
         )
    while True:
        ret = openConnection(sock,BUFFER_SIZE,regs)
        if ret == 'exit':
            break
print("Sever Exited")
