# echo-client.py

import socket
import time
HOST = "192.168.11.102"  # The server's hostname or IP address
PORT = 6003  # The port used by the server


def setupServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, 6003))
    except socket.error as msg:
        print(msg)
    return server

def setupConnection():
    s = setupServer()
    s.listen(1)  # Allows one connection at a time.
    connection, address = s.accept()
    return connection

def dataTransfer(connection):

    
    # Receive the data
    data = connection.recv(1024)  # Receive the data
    data = data.decode('utf-8')
    

    print(data)
    
        

    connection.close()

while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        pass
   
        
        