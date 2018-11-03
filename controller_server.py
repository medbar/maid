import socket
import sys
from command_zipper import unzip_states
import threading
from queue import Queue



class ServerListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.command_queue = Queue()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('0.0.0.0', 10000)
        print('starting up on {} port {}'.format(*self.server_address))


    def run(self):
        self.sock.bind(self.server_address)
        # Listen for incoming connections
        self.sock.listen(1)
        try:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            while True:
                print('connection from', client_address)

                data = connection.recv(5)
                states = unzip_states(data)
                print('received {}'.format(states))
                self.command_queue.put(states)
        finally:
            # Clean up the connection
            connection.close()



if __name__=="__main__":
    from motors_driver import MotorsDriver
    import time
    motor_driver = MotorsDriver()
    server = ServerListener()
    server.setDaemon(True)
    server.start()

    cur_delay = 0
    while True:
        if cur_delay == 10:
            if server.command_queue.empty():
                motor_driver.clean_all_motors()
            state = server.command_queue.get()
            cur_delay = 0
            server.command_queue.task_done()

        time.sleep(0.01)
        cur_delay +=1

