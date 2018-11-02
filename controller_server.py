import socket
import sys
from command_zipper import unzip_states

# Слушает порт, принимает 5 байт


#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

try:

    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    while True:
        print('connection from', client_address)

        data = connection.recv(5)
        states = unzip_states(data)
        print('received {}'.format(states))
finally:
    # Clean up the connection
    connection.close()