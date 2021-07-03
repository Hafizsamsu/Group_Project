# Python program to implement client side of chat room.
import socket
import select
import sys
from Crypto.Cipher import AES
import random, string, base64
import signal
import sys

# quit button
def signal_handler(sig, frame):
    print(' Exiting chat...DONE!')
    sys.exit(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket with inputted ip and port
#IP_address = '192.168.56.106'
#Port = 8000
IP_address = input('IP Address: ')
Port = input('Port: ')
Port = int(Port)
server.connect((IP_address, Port))

while True:


        # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

        # socket stuff, pls ignore
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

