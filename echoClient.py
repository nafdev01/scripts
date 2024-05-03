# client.py
import socket

# define server address and port to listen on
HOST = "127.0.0.1"
PORT = 65432

# create an IPv4 TCP socket object and connect to the server using the specified host address and port. Use sendall() to send a message and call recv() to recieve the server's reply.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, World")
    data = s.recv(1024)

print(f"recieved {data!r}")
