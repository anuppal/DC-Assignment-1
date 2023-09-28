import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455

ADDR = (IP,PORT)
FORMAT = "utf-8"
SIZE=1024

# File request
filename = 'abc.txt'

def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)

    # CLIENT sends a file request with a “pathname” to SERVER 1
    # Send the filename to the server
    client.send(filename.encode())

    # Receive the file content from the server
    with open(filename, 'wb') as file:
        data = client.recv(1024)
        while data:
            file.write(data)
            data = client.recv(1024)
    print(f"File '{filename}' received successfully.")

    # Close the connection
    client.close()

if __name__ == "__main__":
    main()


