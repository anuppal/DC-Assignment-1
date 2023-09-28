import socket
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
F_DIRECTORY = "Data/"
SERVER2_HOST = 'localhost'
SERVER2_PORT = 12346

FORMAT="utf-8"
ADDR = (IP,PORT)
SIZE = 1024

# Creating the Server Socket
print(f"Server 1 listening on Server-1 {ADDR}")
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"Server-1 Listening at {ADDR}")

def send_file_to_client(client_socket, file_path):
    # Open and send the file to the client
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)
    print(f"File '{file_path}' sent successfully.")

while True:
    # Accept incoming connections
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive the filename from the client
    filename = client_socket.recv(1024).decode()
    print(f"Received request for file: {filename}")

    # Construct the full file path
    file_path = os.path.join(FILE_DIRECTORY, filename)

    # Check if the file exists locally
    if os.path.exists(file_path) and os.path.isfile(file_path):
        send_file_to_client(client_socket, file_path)
    else:
        # File not found locally, forward the request to Server 2
        print(f"File '{filename}' not found locally. Forwarding request to Server 2.")

        # Create a socket to communicate with Server 2
        server2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server2_socket.connect((SERVER2_HOST, SERVER2_PORT))

        # Send the filename to Server 2
        server2_socket.send(filename.encode())

        # Receive the file from Server 2 and forward it to the client
        with open(file_path, 'wb') as file:
            data = server2_socket.recv(1024)
            while data:
                file.write(data)
                client_socket.send(data)
                data = server2_socket.recv(1024)
        
        print(f"File '{filename}' forwarded from Server 2 and sent to the client.")

        # Close the connection to Server 2
        server2_socket.close()

    # Close the connection to the client
    client_socket.close()

# while True:
#     # Accept the incoming connection
#     client_socket, addr = server.accept()
#     print(f"Connection from {addr}")

#     # Receive the filename from the client
#     filename = client_socket.recv(1024).decode()
#     print(f"Received request for file: {filename}")

#     # Construct the full file path
#     file_path = os.path.join(F_DIRECTORY, filename)  
    
#     # Check if the file exists
#     if os.path.exists(file_path) and os.path.isfile(file_path):
#         # Open and send the file to the client
#         with open(file_path, 'rb') as file:
#             data = file.read(1024)
#             while data:
#                 client_socket.send(data)
#                 data = file.read(1024)
#         print(f"File '{filename}' sent successfully.")
#     else:
#         error_message = f"File '{filename}' not found."
#         client_socket.send(error_message.encode())
#         print(error_message)

#     # Close the connection
#     client_socket.close()

#CLIENT sends a file request with a “filename” to SERVER 1
#SERVER 1 checks its own file system for the file and sends the same file request to SERVER 2
#SERVER 2 returns the file if available
#SERVER 1 then compares the contents of file it found in its directory and the file that is received from SERVER 2
#If there is no difference between the file contents, SERVER1 sends the file to client.
#If there is a difference between the file contents, SERVER1 sends both the files to client.
#If file is available on one of the servers, then the file is returned to client via SERVER 1
#If the file is not available, SERVER 1 should send appropriate message to CLIENT.

if __name__ == "__main__":
    main()


