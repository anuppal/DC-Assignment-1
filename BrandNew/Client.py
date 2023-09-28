import socket

def main():
    host = '127.0.0.1'
    port = 12344
    # SERVER1_HOST = '127.0.0.1'
    # SERVER1_PORT = 12344

    # AF_INET refers to the address-family ipv4

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    pathname = input("Enter the pathname of the file you want to request: ")

    client_socket.send(pathname.encode('utf-8'))

    data = client_socket.recv(1024)

    if data == b'File not found':
        print("File not found on the servers.")
    else:
        with open('received_file', 'wb') as file:
            while data:
                file.write(data)
                data = client_socket.recv(1024)

        print("File received successfully as 'received_file'.")

    client_socket.close()

if __name__ == "__main__":
    main()
