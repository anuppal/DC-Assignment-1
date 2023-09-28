import socket
import os


# Server 1 configuration
HOST = '127.0.0.1'
PORT = 12345
# F_DIRECTORY = 'Data/'
SERV_2_HOST = '127.0.0.1'
SERV_2_PORT = 65530

def main():

    # Create the server-1 socket
    server_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_1.bind((HOST, PORT))
    server_1.listen()
    print(f"Server-1 is Listening on {HOST}:{PORT}")

    while True:

        # Accept incoming connections
        client_socket, addr = server_1.accept()
        print(f"Established Connection from {addr}")
        client_info = identify_client(addr)

        if client_info == "Connection is from Client":
            print(client_info)
            # Receive the filename from the client
            filename = client_socket.recv(1024).decode()
      
            if os.path.isfile(filename):
                    print("Yeeeh !! File Exists on Server-1")
                    file_from_server2 = forward_request_to_server2(filename)
                    if file_from_server2:
                         client_socket.send(file_from_server2)
                    else:
                         client_socket.send("File not found on Server-2".encode())

        elif client_info == "Connection is from Server-1":
            
                print (client_info)

        elif client_info == "Connection is from Server-2":
        
                print (client_info)
        
        else:
       
            print("This is from unknown source")

        # Close the connection to the client
        # client_socket.close()
        # server_1.close()

        


def send_file_to_client(client_socket, file_path):
    # Open and send the file to the client
    # In this code, 'rb' as the second argument in open() is used to open the file in binary read mode. 
    # The read() function is then used to read the entire content of the file into the variable data.
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)
    print(f"File '{file_path}' sent from server-1 successfully.")

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

def forward_request_to_server2(filename):
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server2_socket:
        #   server2_socket.bind((HOST,PORT))
          server2_socket.connect((SERV_2_HOST, SERV_2_PORT))
          server2_socket.send(filename.encode())
        #   server2_socket.send(filepath.encode())

          # receievd a file from server-2
        #   received_data='b'
          while True:
               data = server2_socket.recv(1024)
               if not data:
                    break
            #    received_data += data
               return data
     

if __name__ == "__main__":
    main()