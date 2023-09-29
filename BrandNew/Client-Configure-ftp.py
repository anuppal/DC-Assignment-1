from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server():

    # Instantiate a dummy authorizer to manage 'virtual' users

    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')

    authorizer.add_anonymous('.')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a new FTP server on the default address (0.0.0.0) and port (2121)
    server = FTPServer(('172.31.3.159', 2122), handler)

    # Start ftp server
    server.serve_forever()

if __name__ == "__main__":

    start_ftp_server()


