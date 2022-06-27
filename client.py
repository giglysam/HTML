
import socket
soc = socket.socket()
host = socket.gethostname()
port = 8080
soc.bind(('', port))
print("waiting for connections...")
soc.listen()
conn, addr = soc.accept()
print(addr, "is connected to server")

while True:
  command = input(str("Enter message:"))
  conn.send(command.encode())
  data = conn.recv(1024)
  if command == 'exit':
     quit()

