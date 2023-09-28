import paramiko

# Define the connection parameters for server1
server1_host = '127.0.0.1'
server1_port = 22
server1_username = 'your_username'
server1_password = 'your_password'  # You can also use SSH keys for authentication

# Define the local file path (file to send)
local_file_path = 'Data/abc.txt'

# Define the remote destination path on server1
remote_file_path = 'Data/abc.txt'

# Create SSH client for server1
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to server1
client.connect(server1_host, server1_port, server1_username, server1_password)

# Create an SCP client for server1
scp = client.open_sftp()

# Transfer the file from the client to server1
scp.put(local_file_path, remote_file_path)

# Close the connections
scp.close()
client.close()

print(f"File '{local_file_path}' has been sent to server1 at '{remote_file_path}'")
