import socket
from duplexer import JSONDuplexer  # Assuming your JSONDuplexer is implemented as above

HOST = "localhost"
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is listening...")

conn, addr = server.accept()  # Accept a client connection
print(f"Connection from {addr}")

# Pass the client connection socket (conn) to the Duplexer
duplexer = JSONDuplexer(conn)

# Receive JSON data
received_data = duplexer.receive()
print(f"Received: {received_data}")

# Send JSON data
duplexer.send({"all_good": 123})

# Clean up
duplexer.close()
server.close()
