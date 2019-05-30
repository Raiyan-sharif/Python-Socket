import socket

s = socket.socket()
host = input(str("Enter the host address of the sender : "))
port = 8080
s.connect((host, port))
print("Connected ...")

filename = input(str("Please enter a filename for incoming file : "))
file = open(filename, "wb")
file_date = s.recv(1024)
file.write(file_date)
file.close()
print("File has been received successfully.")
