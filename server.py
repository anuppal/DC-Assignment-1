import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455

FORMAT="utf-8"
ADDR = (IP,PORT)
SIZE = 1024

def main():
    print("Server is Starting ..!")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()

    print("Server is Listening ..!")

    while True:
        conn, addr = server.accept()
        print(f"Connected to: {addr}")

        filename = conn.recv(SIZE).decode(FORMAT) # Server Received File Name [A]
        print(f"[Server] Received : {filename}")

        file = open(filename,"w") # Server Writing on file [B]  
        conn.send("[Server] Sending..".encode(FORMAT)) # Server Writing on file [B] 

        data = conn.recv(SIZE).decode(FORMAT) # Server Received Data from Client [C]
        print(f"[Server] Received") # Server Received Data from Client [C]

        file.write(data)
        conn.send("File Data Receiecd ..".encode(FORMAT)) # Sending data to Client []
        file.close()
        conn.close()
        print("Connection {addr} Disconnected now..! ")


if __name__ == "__main__":
    main()


