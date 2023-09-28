import socket
import os

# Server 2 configuration
HOST = 'localhost'
PORT = 65530
F_DIRECTORY = 'Content/'
SERV_1_HOST = 'localhost'
SERV_1_PORT = 12345

# Create the server-2 socket
server_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_2.bind((HOST, PORT))
server_2.listen()
print(f"Server 2 listening on {HOST}:{PORT}")

def main():
    # Accept incoming connections
    client_socket, addr = server_2.accept()
    print(f"Connection from {addr}")

    # Receive the filename from the client
    filename = client_socket.recv(1024).decode()
    print(f"Received request for file: {filename}")

    # Construct the full file path
    file_path = os.path.join(F_DIRECTORY, filename)

     # Check if the file exists locally
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print("Yeeeh !! File Exists on Server-2")
        # send_file_to_client(client_socket, file_path)

        # Create a socket to communicate with Server 1
        # Create the server-1 socket
        server_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # server_1.bind((HOST, PORT))
        # server_1.listen()
        server_1.connect((SERV_1_HOST, SERV_1_PORT))
        print(f"Server 1 listening on {SERV_1_HOST}:{SERV_1_PORT}")

        client_socket.send("File found on Server-2".encode())
        # Send the filename to Server 1
        server_1.send(filename.encode())

        # Receive the file from Server 1 and forward it to the client
        with open(file_path, 'wb') as file:
            data = server_1.recv(1024)
            while data:
                file.write(data)
                client_socket.send(data)
                data = server_1.recv(1024)
        print(f"File '{filename}' forwarded from Server 1 and sent to the client.")


    else:
        # File not found locally, forward the request to Server 1
        print(f"Oops..! File '{filename}' not found locally. Forwarding request to Server 1.")

        # Create a socket to communicate with Server 1
        # Create the server-1 socket
        server_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # server_1.bind((HOST, PORT))
        # server_1.listen()
        server_1.connect((SERV_1_HOST, SERV_1_PORT))
        print(f"Server 1 listening on {SERV_1_HOST}:{SERV_1_PORT}")

        # Send the filename to Server 1
        server_1.send(filename.encode())
        

        # Receive the file from Server 1 and forward it to the client
        with open(file_path, 'wb') as file:
            data = server_1.recv(1024)
            while data:
                file.write(data)
                client_socket.send(data)
                data = server_1.recv(1024)
        print(f"File '{filename}' forwarded from Server 1 and sent to the client.")

    # Close the connection to Server 2
    server_1.close()

    # Close the connection to the client
    client_socket.close()


def send_file_to_client(client_socket, file_path):
    # Open and send the file to the client
    # In this code, 'rb' as the second argument in open() is used to open the file in binary read mode. 
    # The read() function is then used to read the entire content of the file into the variable data.
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)
    print(f"File '{file_path}' sent from server-2 successfully.")

if __name__ == "__main__":
    main()