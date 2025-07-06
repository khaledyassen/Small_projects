import ftplib
import getpass

ftp_server = input("Enter the FTP server?? ")
ftp_username = input("Enter FTP username?? ")
ftp_password = getpass.getpass("Enter the FTP Password?? ")

ftp = ftplib.FTP(ftp_server)
ftp.login(ftp_username, ftp_password)

try:
  # Create an FTP object and connect to the server
  ftp = FTP(ftp_server)
  ftp.login(ftp_username, ftp_password)
except:
  print("Loggin failed try again..")

# List files in the current directory
ftp.dir()
ftp.get('test.txt')

ftp.quit()
