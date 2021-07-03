# Python program to implement server side of chat room.
import socket
import select
import sys
from _thread import *
from Crypto.Cipher import AES
import random, string, base64

# socket stuffs
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind socket with inputted ip and port
#IP_address = '192.168.56.106'
#Port = 8000
IP_address = input('IP Address: ')
Port = input('Port: ')
Port = int(Port)
server.bind((IP_address, Port))

# listens for 100 active connections. This number can be increased as per convenience.
server.listen(100)
print ("Server online. Waiting for connections...")

list_of_clients = []

def clientthread(conn, addr):

        # sends a message to the client whose user object is conn
        conn.send("Welcome to the secured chatroom. Press CTRL+C to exit anytime. Have fun!".encode('utf-8'))

        while True:
                        try:
                                message = conn.recv(2048).decode('utf-8')
                                if message:

                                        # prints the message and address
                                        print ("<" + addr[0] + "> " + message[48:])

                                        # Calls broadcast function to send message to all
                                        #message_to_send = "<" + addr[0] + "> " + message
                                        broadcast(message, conn)
                                else:
                                        # message may have no content if the connection is broken, in this case we remove the connection
                                        remove(conn)

                        except:
                                continue
