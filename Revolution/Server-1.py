import socket
import os
import filecmp

# Server Configuration
host = '127.0.0.1'
port = 12344    
SERVER2_HOST = '127.0.0.1'
SERVER2_PORT = 12346


def compare_files(file1, file2):
    # Compare two files and return the result
    return filecmp.cmp(file1, file2)


def main():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)

        print(f"Server listening on {host}:{port}")

        while True:
            # Accept Client Connection
            client_connection, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")


            with client_connection:
                # Receive the file name from the client
                filename = client_connection.recv(1024).decode('utf-8')

                if not filename:
                    break 
                # Receive the file from the client
                with open(filename, 'wb') as file:
                    while True:
                        data = client_connection.recv(1024)
                        if not data:
                            break
                        file.write(data)

                # Compare the received file with a reference file
                reference_file = 'reference.txt'
                result = compare_files(filename, reference_file)

                # Send the comparison result to the client
                client_connection.sendall(str(result).encode('utf-8'))



if __name__ == "__main__":
    main()

