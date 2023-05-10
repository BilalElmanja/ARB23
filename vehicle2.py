# echo-client.py

import socket
import time
HOST = "192.168.11.102"  # The server's hostname or IP address
PORT = 6002  # The port used by the server





def sendDataToServer(message, HOST , PORT):
    client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))   
    client.send(message.encode('utf-8'))
    data = client.recv(1024)
    client.close()



def setupServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, 6002))
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
            # reply to the server
            connection.sendall("VEHICLE_2 MOVING FORWARD".encode('utf-8'))
            time.sleep(5)
            sendDataToServer("VEHICLE_2 POINT_B", HOST, 5560)

        elif command == "RIGHT":
            print("Vehicle is moving right")
            connection.send("VEHICLE_2 MOVING FORWARD".encode('utf-8'))
            time.sleep(5)
            sendDataToServer("VEHICLE_2 POINT_C", HOST, 5560)

        elif command == "LEFT":
            print("Vehicle is moving left")
            connection.send("VEHICLE_2 MOVING LEFT".encode('utf-8'))
            time.sleep(5)
            sendDataToServer("VEHICLE_2 POINT_D", HOST, 5560)

        elif command == "STOP":
            print("Vehicle is stopping")
            connection.send("VEHICLE_2 MOVING FORWARD".encode('utf-8'))
            time.sleep(5)
            sendDataToServer("VEHICLE_2 POINT_E", HOST, 5560)
            break

       
        
        connection.close()




while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        pass
   
        
        
    
