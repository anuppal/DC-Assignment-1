import socket
import os

# Server 2 configuration
HOST = '127.0.0.1'
PORT = 65530
# F_DIRECTORY = 'Content/'
SERV_1_HOST = '127.0.0.1'
SERV_1_PORT = 12345

def main():

    # Create the server-2 socket
    server_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_2.bind((HOST, PORT))
    server_2.listen()
    print(f"Server 2 listening on {HOST}:{PORT}")

    while True:

        # Accept incoming connections
        client_socket, addr = server_2.accept()
        print(f"Established Connection from {addr}")
        filename = client_socket.recv(1024).decode()
        print(f"Received request for file: {filename}")
        # pathName = client_socket.recv(1024).decode()
        # print(f"Received request for file: {filename} and path {F_DIRECTORY}")

         # Construct the full file path
        # file_path = os.path.join(F_DIRECTORY, filename)
        client_socket.send(filename.encode())
        send_file_to_client(client_socket,filename)

       
        # Close the connection to the client
        # client_socket.close()


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

def receive_file(client_socket, filename):
    with open(filename, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

def compare_files(file1 , file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.read()
        content2 = f2.read()
        if content1 == content2:
            return "Files are Identical"
        else:
            return "Files are different"
        
def identify_client(client_address):
    # Checking if the Server-1 IP Matches
    server1_ip = '127.0.0.1'
    server1_port = 12345
    if client_address[0] == server1_ip and client_address[1] == server1_port:
        return "Connection is from Server-1"
    
     # Checking if the Server-2 IP Matches
    server2_ip = '127.0.0.1'
    server2_port = 65530
    if client_address[0] == server2_ip and client_address[1] == server2_port:
        return "Connection is from Server-2"
    
    # Checking if the Client IP Matches
    client_ip = '127.0.0.1'
    client_port = 32178
    if client_address[0] == client_ip and client_address[1] == client_port:
        return "Connection is from Client"
    
    return "Connection is from unknown source"


def forward_request_to_server1(filename):
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server1_socket:
          server1_socket.connect((SERV_1_HOST, SERV_1_PORT))
          server1_socket.send(filename.encode())
        #   server2_socket.send(F_DIRECTORY.encode())

          # receievd a file from server-1
          received_data='b'
          while True:
               data = server1_socket.recv(1024)
               if not data:
                    break
               received_data += data
               return received_data

if __name__ == "__main__":
    main()