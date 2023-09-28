import socket

# Server 1 configuration
SERV1_HOST = 'localhost'
SERV1_PORT = 12345

# File request
filename = 'abc.txt'

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERV1_HOST, SERV1_PORT))

# Send the filename to the server
client_socket.send(filename.encode())

# Receive the file content from the server. 
# In this code, 'wb' as the second argument in open() is used to open the file in binary write mode.

data = client_socket.recv(1024)
print(data)
# with open(filename, 'wb') as file:
#     data = client_socket.recv(1024)
#     while data:
#         file.write(data)
#         data = client_socket.recv(1024)

# print(f"File '{filename}' received successfully.")

# Close the connection
client_socket.close()
