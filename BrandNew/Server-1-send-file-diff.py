from ftplib import FTP
import filecmp

def send_file_to_ftp_server(filename, folder):

    # Instantiate FTP object
    ftp = FTP()

    # Connect to the FTP server
    ftp.connect('172.31.3.159', 2122)

    # Login to the FTP server
    ftp.login('user', '12345')

    # Change the current working directory to the specific folder
    # ftp.cwd(folder)
    # Open the file in binary mode and send it to the FTP server
    with open(filename, 'rb') as file:
        ftp.storbinary('STOR ' + filename, file)

    file.close()
    # Quit and close the connection
    ftp.quit()

if __name__ == "__main__":

	status = filecmp.cmp("data/server1.txt","data/server2.txt")
	if status ==False:
		send_file_to_ftp_server("data/server2.txt", "/home/labuser/Assignment-1/data/")

		send_file_to_ftp_server("data/server1.txt", "/home/labuser/Assignment-1/data/")
	else:
		send_file_to_ftp_server("data/server1.txt", "/home/labuser/Assignment-1/data/")