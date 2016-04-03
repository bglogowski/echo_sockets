#!/usr/bin/env python3

import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    sock.connect(server_address)

    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        amount_received = 0
        amount_expected = len(msg)

        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(msg.encode('utf-8'))

        while True:
            chunk = sock.recv(16)
            received_message += chunk.decode('utf8')
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            amount_received += len(chunk)
            if amount_received == amount_expected:
                break

        return received_message

    finally:
        print('closing socket', file=log_buffer)
        sock.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
