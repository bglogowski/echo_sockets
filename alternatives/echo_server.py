#!/usr/bin/env python3

import socket

class EchoServer():
    """Listens on a port, and returns an echo response"""

    def __init__(self, host = '127.0.0.1', port = 50000, connection_pool = 5, buffer_size = 4096):
        """Initializes the echo server:

        Attributes:
            host -- hostname or IP to listen on
            port -- port to listen on
            connection_pool -- client connection backlog
            buffer_size -- amount of data to receive from client
        """
     
        self.host = host
        self.port = port
        self.connection_pool = connection_pool
        self.buffer_size = buffer_size

        # Only proceed to the next step if the previous step was successful
        if self.create_socket():
            if self.bind_socket():
                if self.listen_socket():
                    return self.receive_data()
                else:
                    print('Could not listen to socket')
            else:
                print('Could not bind to socket')
        else:
            print('Could not create socket')


    def create_socket(self):
        """Creates a network socket"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            return False
        return True

    def bind_socket(self):
        """Binds to a socket"""
        try:
            self.sock.bind((self.host, self.port))
        except:
            return False
        return True

    def listen_socket(self):
        """Listens on a socket for connections"""
        try:
            self.sock.listen(self.connection_pool)
        except:
            return False
        return True

    def receive_data(self):
        """Receives data from a client, and echos it back."""
        while 1:
            client, address = self.sock.accept()
            print('Client connection recieved from:', address[0])
            data = client.recv(self.buffer_size)
            if data:
                print('    Response recieved:', data.decode())
                client.send(data)
            client.close() 

# Instantiate the server with all the defaults, capture the result
result = EchoServer()
