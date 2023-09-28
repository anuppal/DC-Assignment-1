import paramiko

def compare_files(file1 , file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.read()
        content2 = f2.read()
        if content1 == content2:
            return "Files are Identical"
        else:
            return "Files are different"

# Define the connection parameters for server1
server1_host = '127.0.0.1'
server1_port = 22
server1_username = 'your_username'
server1_password = 'your_password'  # You can also use SSH keys for authentication

# Define the connection parameters for server2
server2_host = '127.0.0.1'
server2_port = 22
server2_username = 'your_username'
server2_password = 'your_password'  # You can also use SSH keys for authentication

# Define the local file path and the remote destination path on server2
local_file_path = 'Data/abc.txt'
remote_file_path = 'Data/abc.txt'

# Create SSH client for server1
client1 = paramiko.SSHClient()
client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to server1
client1.connect(server1_host, server1_port, server1_username, server1_password)

# Create SSH client for server2
client2 = paramiko.SSHClient()
client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to server2
client2.connect(server2_host, server2_port, server2_username, server2_password)

# Create an SCP client for server1
scp1 = client1.open_sftp()

# Transfer the file from server1 to server2
scp1.get(local_file_path, remote_file_path)

# Close the connections
scp1.close()
client1.close()
client2.close()

print(f"File '{local_file_path}' has been sent from server1 to server2 at '{remote_file_path}'")
