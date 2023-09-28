import socket

def main():
    host = '127.0.0.1'
    port = 12344

    #Create a Socket 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    Filename = input("Enter the pathname of the file you want to request: ")

    # Sending the file pathname to the server
    client_socket.sendall(Filename.encode('utf-8'))


    # Send the file to the server
    with open(Filename, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

 # Receive and print the comparison result from the server
    result = client_socket.recv(1024).decode('utf-8')
    print(f"File comparison result: {result}")

    #client_socket.close()

if __name__ == "__main__":
    main()
