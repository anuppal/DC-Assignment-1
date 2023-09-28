import paramiko

# Define the connection parameters for server2
server2_host = '127.0.0.1'
server2_port = 22
server2_username = 'your_username'
server2_password = 'your_password'  # You can also use SSH keys for authentication

# Define the connection parameters for server2
server2_host = '127.0.0.1'
server2_port = 22
server2_username = 'your_username'
server2_password = 'your_password'  # You can also use SSH keys for authentication

# Define the local file path and the remote destination path on server2
local_file_path = 'Data/abc.txt'
remote_file_path = 'Data/abc.txt'

# Create SSH client for server2
client1 = paramiko.SSHClient()
client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to server2
client1.connect(server2_host, server2_port, server2_username, server2_password)

# Create SSH client for server2
client2 = paramiko.SSHClient()
client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to server2
client2.connect(server2_host, server2_port, server2_username, server2_password)

# Create an SCP client for server2
scp1 = client1.open_sftp()

# Transfer the file from server2 to server1
scp1.get(local_file_path, remote_file_path)

# Close the connections
scp1.close()
client1.close()
client2.close()

print(f"File '{local_file_path}' has been sent from server2 to server2 at '{remote_file_path}'")
