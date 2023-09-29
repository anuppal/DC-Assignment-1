from ftplib import FTP



def send_file_to_ftp_server(filename):

    # Instantiate FTP object
    ftp = FTP()
    # Connect to the FTP server
    ftp.connect('172.31.5.237', 2120)
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

    send_file_to_ftp_server("data/same-s2.txt")

