"""
FTP port 21 = File Transfer Protocol
It is used to exchange files between the client and server.
It is a clear text protocol. Hence, it is not secure.

SFTP port 22 = Secure File Transfer Protocol

"""
from ftplib import FTP

FTP_SERVER_URL = 'ftp.be.debian.org'

with FTP(FTP_SERVER_URL) as ftp:
    ftp.login()
    ftp.dir()

