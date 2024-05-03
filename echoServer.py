# server.py
import socket

# define server address and port to listen on
HOST = "127.0.0.1"
PORT = 65432

# Create an IPv4 TCP socket object associate it with a network interface and port number using the bind method. Enable the server to accept connections using the listen method (make it a listening socket). When a client connects (the accept method), it returns a new socket object representing the connection and a tuple (host, port) holding the address of the client. An infinite while loop is used to loop over blocking calls to conn.recv() which reads the data the client has sent and echoes it back using conn.sendall(). If conn.recv() recieves an empty bytes object, that signals that the client has closed the connection and the loop is terminated. The with statement is used with conn automatically close the socket at the end of the block.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
