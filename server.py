import os
import socket
soc = socket.socket()
host = "127.0.0.1"
port = 8080
soc.connect((host, port))
print("Connected to Server.")
command0 = soc.recv(1024)
command = command0.decode()
print(str(command))
if command.__contains__('open'):
        com = command.replace('open ', '')
        myfile = open(com, "r")
        data0 = myfile.read().splitlines()
        res0 = str(data0).replace(',', '\n')
        res1 = str(res0).replace('[', '')
        res2 = str(res1).replace(']', '')
        res3 = str(res2).replace("'", '')
        print(res3)
