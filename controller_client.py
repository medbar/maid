import socket
from command_zipper import *

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    states = [0, 1, 2, 3, 4]
    # Send data
    message = zip_states(states)

    sock.sendall(message)

finally:
    print('closing socket')
    sock.close()