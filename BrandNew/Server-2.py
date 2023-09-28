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

def main():
    host = '127.0.0.1'
    port = 12346
    SERVER1_HOST = '127.0.0.1'
    SERVER1_PORT = 12344

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
        # Check if the file exists on Server 2
        if os.path.exists(pathname):
            print(f"File '{pathname}' found on Server 2.")
            send_file(client_connection, pathname)
            client_connection.send(pathname.encode('utf-8'))
        else:
            print(f"File '{pathname}' not found on Server 2. Sending request to Server 1.")
            client_connection.send(b'File not found')
            # # Forward the request to SERVER 2
            # server2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # server2_socket.connect((SERVER1_HOST, SERVER1_PORT))
            # server2_socket.send(pathname.encode('utf-8'))

            # # Receive the file from SERVER 1 and send it to the client
            # data = server2_socket.recv(1024)
            # if data == b'File not found':
            #     client_connection.send(b'File not found')
            # else:
            #     client_connection.send(data)

            # server2_socket.close()

        # client_connection.close()

        client_connection.close()

if __name__ == "__main__":
    main()
