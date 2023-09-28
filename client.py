import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455

ADDR = (IP,PORT)
FORMAT = "utf-8"
SIZE=1024

def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)

    file = open("Data/abc.txt","r")
    data = file.read()

    client.send("abc.txt".encode(FORMAT)) # Client Sending File name to Server [A] 

    msg = client.recv(SIZE).decode(FORMAT) # Client Received file from server [B] 
    print(f"[Client] Received {msg}") # Client Received file from server [B] 

    client.send(data.encode(FORMAT)) # Client Sending Data to Server [C]

    msg = client.recv(SIZE).decode(FORMAT) # Receving data from Server [D]
    print(f"[Client] Received : {msg}") # Receving data from Server [D]

    file.close()
    client.close()
    


if __name__ == "__main__":
    main()


