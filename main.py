

import socket
import time

HOST = ""  # Standard loopback interface address (localhost)
PORT = 5560  # Port to listen on (non-privileged ports are > 1023)

exit1_Sequence = ["FORWARD" , "FORWARD" , "FORWARD", "RIGHT" , "FORWARD" , "STOP" ]
exit1_Senquence_server = ["FORWARD" , "LEFT" , "FORWARD", "RIGHT" , "LEFT" , "STOP"]
exit2_Sequence = ["FORWARD" , "FORWARD" ,  "RIGHT" , "FORWARD" , "STOP" ]
exit2_Senquence_server = ["FORWARD" , "FORWARD" ,  "RIGHT" , "FORWARD" , "STOP" ]
exit3_Sequence = ["FORWARD" ,  "RIGHT" , "FORWARD" , "STOP" ]
exit3_Senquence_server = ["FORWARD" ,  "RIGHT" , "FORWARD" , "STOP" ]
exit4_Sequence = ["FORWARD" ,  "RIGHT" , "RIGHT" , "STOP" ]
exit4_Senquence_server = ["FORWARD" ,  "RIGHT" , "RIGHT" , "STOP" ]

Points = ["POINT_A" , "POINT_B" , "POINT_C" , "POINT_D" , 
          "POINT_E" , "POINT_F" , "POINT_G" , "POINT_H" , 
          "POINT_I" , "POINT_J" , "POINT_K" ]

VEHICLE_1 = "192.168.11.102"
VEHICLE_2 = "192.168.11.102"
DASHBOARD = "192.168.11.102"




def sendDataToVehicle(message, HOST , PORT):
    try:
        client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))   
        client.send(message.encode('utf-8'))
        data = client.recv(1024)
        print(repr(data))
        client.close()
    except:
        print("Error: Can't connect to the vehicle")


def sendDataToDashboard(message, HOST , PORT):
    try:
        client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))   
        client.send(message.encode('utf-8'))
        data = client.recv(1024)
        client.close()
    except:
        print("Error: Can't connect to the dashboard")
        


def setupServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server.bind((HOST, PORT))
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
    dataMessage = data.split(' ')
    vehicle = dataMessage[0]
    command = dataMessage[1]

    if vehicle == 'VEHICLE_1':
        
        if command == Points[0]:
            connection.send("OK".encode('utf-8'))
            time.sleep(1)
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Senquence_server[0] , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + exit1_Senquence_server[0] , DASHBOARD, 6003)

            
        elif command == Points[1]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Senquence_server[1] , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + exit1_Senquence_server[2] , DASHBOARD, 6003)
            
        elif command == Points[2]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Senquence_server[2] , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + exit1_Senquence_server[2] , DASHBOARD, 6003)
            
        elif command == Points[3]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Senquence_server[3] , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + exit1_Senquence_server[3] , DASHBOARD, 6003)
            
        elif command == Points[4]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Senquence_server[4] , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + exit1_Senquence_server[4] , DASHBOARD, 6003)

            
        elif command == Points[5]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + "STOP" , DASHBOARD, 6003)
            
        elif command == Points[6]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + "STOP" , DASHBOARD, 6003)
            
        elif command == Points[7]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + "STOP" , DASHBOARD, 6003)
            
        elif command == Points[8]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Senquence_server[-1] , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + exit1_Senquence_server[-1] , DASHBOARD, 6003)
            
        elif command == Points[9]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + "STOP" , DASHBOARD, 6003)
            
        elif command == Points[10]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_2, 6002)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_2 - " + "STOP" , DASHBOARD, 6003)
            

    elif vehicle == 'VEHICLE_2':

        if command == Points[0]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command, DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Sequence[4] , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + exit1_Sequence[4], DASHBOARD, 6003)
            
        elif command == Points[1]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Sequence[3] , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + exit1_Sequence[3], DASHBOARD, 6003)
            
            
        elif command == Points[2]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + "STOP", DASHBOARD, 6003)
            
        elif command == Points[3]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + "STOP", DASHBOARD, 6003)
            
        elif command == Points[4]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Sequence[0] , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + exit1_Sequence[0] , DASHBOARD, 6003)
            
        elif command == Points[5]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Sequence[1] , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + exit1_Sequence[1] , DASHBOARD, 6003)
            
            
        elif command == Points[6]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle(exit1_Sequence[2] , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + exit1_Sequence[2] , DASHBOARD, 6003)
            
        elif command == Points[7]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + "STOP" , DASHBOARD, 6003)
            
        elif command == Points[8]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command, DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + "STOP" , DASHBOARD, 6003)
            
        elif command == Points[9]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + "STOP" , DASHBOARD, 6003)
            
        elif command == Points[10]:
            connection.send("OK".encode('utf-8'))
            sendDataToDashboard(vehicle + " " + command , DASHBOARD, 6003)
            time.sleep(1)
            sendDataToVehicle("STOP" , VEHICLE_1, 6001)
            time.sleep(1)
            sendDataToDashboard("VEHICLE_1 - " + "STOP" , DASHBOARD, 6003)
            

    elif command == 'KILL':
        print("Server is shutting down")
        
    else:
        print('Unknown Command')
    # Send the reply back to the client
    
    
    connection.close()




while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        
        pass



