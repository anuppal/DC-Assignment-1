import socket

# Client configuration
HOST = '127.0.0.1'
PORT = 32178

# Server 1 configuration
SERV1_HOST = '127.0.0.1'
SERV1_PORT = 12345

# File request
filename = "abc.txt"

# Pathname
# pathName = "Data/"

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((HOST,PORT))
client_socket.connect((SERV1_HOST, SERV1_PORT))

# CLIENT sends a file request with a “pathname” to SERVER 1. 
client_socket.send(filename.encode())
# client_socket.send(pathName.encode())

# Receive the file content from the server. 
# In this code, 'wb' as the second argument in open() is used to open the file in binary write mode.

data = client_socket.recv(1024)
print(data)

client_socket.close()
