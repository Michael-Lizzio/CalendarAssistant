import socket
import json


class JSONDuplexer:
    def __init__(self, connection: socket.socket):
        """
        Initialize the JSONDuplexer with a given socket connection.
        """
        self.connection = connection
        self.reader = self.connection.makefile('r')
        self.writer = self.connection.makefile('w')

    def send(self, data: dict):
        """
        Send JSON-encoded data to the connected socket.
        """
        message = json.dumps(data)
        print(f">> {message}")
        self.writer.write(message + '\n')
        self.writer.flush()

    def receive(self) -> dict:
        """
        Receive JSON-encoded data from the connected socket.
        """
        message = self.reader.readline().strip()
        print(f"<< {message}")
        return json.loads(message)

    def close(self):
        """
        Clean up and close the socket and file objects.
        """
        try:
            self.reader.close()
            self.writer.close()
            self.connection.close()
        except Exception as e:
            print(f"Error closing resources: {e}")


# Example usage
if __name__ == "__main__":
    HOST = "localhost"
    PORT = 65432

    # Example client
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        duplexer = JSONDuplexer(sock)

        # Send JSON data
        duplexer.send({"type": "greeting", "message": "Hello, Server!"})

        # Receive JSON response
        response = duplexer.receive()
        print("Received:", response)

        duplexer.close()
