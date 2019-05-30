import socket


s = socket.socket()
host = socket.gethostname()
print(host)
host = "127.0.0.1"

port = 8080
s.bind((host, port))

s.listen(1)
print("waiting for any incoming connections")

conn, addr = s.accept()
print(addr, "has connected to the server ")

filename = input(str("Please enter the filename of the file : "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transferred successfully")


