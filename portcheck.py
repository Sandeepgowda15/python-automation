import socket

host = "127.0.0.1"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex((host, port))

if result == 0:
    print("Port is OPEN")
else:
    print("Port is CLOSED")

s.close()
