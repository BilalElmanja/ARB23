# echo-client.py

import socket
import time
HOST = "192.168.11.102"  # The server's hostname or IP address
PORT = 6001  # The port used by the server


def sendDataToServer(message, HOST , PORT):
    client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))   
    client.send(message.encode('utf-8'))
    data = client.recv(1024)
    client.close()



def setupServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, 6001))
    except socket.error as msg:
        print(msg)
    return server

def setupConnection():
    s = setupServer()
    s.listen(3)  # Allows one connection at a time.
    connection, address = s.accept()
    return connection

def dataTransfer(connection):

    while True:
        # Receive the data
        data = connection.recv(1024)  # Receive the data
        data = data.decode('utf-8')
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]

        print(command)
        if command == "FORWARD":
            print("Vehicle is moving forward")
            connection.send("VEHICLE_1 MOVING FORWARD".encode('utf-8'))
            time.sleep(5)
            sendDataToServer("VEHICLE_1 POINT_B", HOST, 5560)

        elif command == "RIGHT":
            print("Vehicle is moving right")
            connection.send("VEHICLE_1 MOVING RIGHT".encode('utf-8'))
            time.sleep(5)
            sendDataToServer("VEHICLE_1 POINT_C", HOST, 5560)
        
        elif command == "LEFT":
            print("Vehicle is moving left")
            connection.send("VEHICLE_1 MOVING LEFT".encode('utf-8'))
            time.sleep(5)
            sendDataToServer("VEHICLE_1 POINT_C", HOST, 5560)
            
        elif command == "STOP":
            print("Vehicle is stopping")
            connection.send("VEHICLE_1  STOPPING".encode('utf-8'))
            time.sleep(5)
            sendDataToServer("VEHICLE_1 POINT_D", HOST, 5560)
            break

       
        
        connection.close()


message = input("start, print OK: ") 
sendDataToServer("VEHICLE_1 POINT_A", HOST, 5560)

while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        pass
   
        
        
    
