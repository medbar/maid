import socket
from command_zipper import *
from keyboard_controller import KeyboardController
import time

def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    keyboard_controller = KeyboardController()
    try:
        while True:
            states = keyboard_controller.get_states()
            # Send data
            message = zip_states(states)
            sock.sendall(message)
            time.sleep(0.1)

    finally:
        print('closing socket')
        sock.close()


if __name__ == "__main__":
    main()