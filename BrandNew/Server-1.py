import socket
import os

def send_file(connection, filename):
    try:
        with open(filename, 'rb') as file:
            data = file.read(1024)
            while data:
                connection.send(data)
                data = file.read(1024)
    except FileNotFoundError:
        connection.send(b'File not found')

def compare_files(file1 , file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.read()
        content2 = f2.read()
        if content1 == content2:
            return "Files are Identical"
        else:
            return "Files are different"

def split_filename_from_path(filepath):
    # Use os.path.basename to get the filename from the path
    filename = os.path.basename(filepath)
    return filename

def main():
    host = '127.0.0.1'
    port = 12344    
    SERVER2_HOST = '127.0.0.1'
    SERVER2_PORT = 12346

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_connection, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        pathname = client_connection.recv(1024).decode('utf-8')
        print(f"Received file request for {pathname}")

        # send_file(client_connection, pathname)
        # Check if the file exists on Server 1
        if os.path.exists(pathname):
            print(f"File '{pathname}' found on Server 1.")
            send_file(client_connection, pathname)
        else:
            print(f"File '{pathname}' not found on Server 1. Sending request to Server 2.")
            # Forward the request to SERVER 2
            server2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server2_socket.connect((SERVER2_HOST, SERVER2_PORT))
            server2_socket.send(pathname.encode('utf-8'))

            # Receive the file from SERVER 2 and send it to the client
            data = server2_socket.recv(1024)
            data1 = server2_socket.recv(1024).decode('utf-8')
            if data == b'File not found':
                client_connection.send(b'File not found')
            else:
                # client_connection.send(data)

                # a = split_filename_from_path(pathname)
                # b = split_filename_from_path(data)

                result = compare_files(pathname,data)

                if result == "Files are Identical":
                    send_file(client_connection, result)
                else:
                    send_file(client_connection, result)
                   

            server2_socket.close()

        client_connection.close()

        client_connection.close()

if __name__ == "__main__":
    main()
