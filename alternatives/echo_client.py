#!/usr/bin/env python3

import socket

def echo_client(msg):
    host = 'localhost'
    port = 50000
    size = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(msg.encode('utf-8'))
    data = sock.recv(size)
    sock.close()
    return data.decode()


# Test the function:
print('Response from server:', echo_client('Ping'))


