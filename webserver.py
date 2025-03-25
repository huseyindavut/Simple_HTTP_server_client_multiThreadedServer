from socket import *
import sys
import os

# At the top here I imported some basic modules.
# socket is obviously for networking, sys is there so I can cleanly shut down the program,
# and I threw in os just in case I need it for file stuff later.

def start_server(port):
    '''
    Description:
        This function creates a simple HTTP server that handles one request at a time.
        It accepts connections, reads HTTP GET requests, and responds with a file or 404 error.

    Arguments:
        port: the port number on which the server will listen

    Returns:
        None

    Exceptions:
        Handles IOError if the requested file is not found
    '''

    # So right here I’m creating the server’s TCP socket.
    # I'm using IPv4 (AF_INET) and streaming (SOCK_STREAM) since HTTP runs on TCP.
    serverSocket = socket(AF_INET, SOCK_STREAM)

    try:
        # This line binds the socket to the specified port.
        # I used an empty string for the IP so it listens on all interfaces.
        serverSocket.bind(('', port))

        # Now I’m telling the server to start listening for incoming connections.
        # Just one at a time here, since this is a basic single-threaded setup.
        serverSocket.listen(1)
        print(f"Server is ready to serve at http://127.0.0.1:{port}")

        while True:
            # Here I'm waiting for a client to connect.
            # Once someone connects, I grab the connection and their address.
            print("Waiting for a connection...")
            connectionSocket, addr = serverSocket.accept()
            print(f"Connection received from {addr}")

            try:
                # When the client sends their request, I read it and decode it from bytes to text.
                message = connectionSocket.recv(1024).decode()
                print("Received request:\n", message)

                # Then I extract the requested file name from the HTTP request.
                # It usually looks like '/index.html', so I remove the leading slash.
                filename = message.split()[1]  # e.g. /index.html
                filepath = filename[1:]  # remove leading '/'

                # I try to open the file and read its content.
                # If it's there, I send it back with a proper 200 OK response.
                with open(filepath, 'r') as f:
                    content = f.read()

                # Just building a very simple HTTP header and sending it first.
                header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                connectionSocket.send(header.encode())
                connectionSocket.send(content.encode())

            except IOError:
                # If something goes wrong while reading the file (like it's missing),
                # I just send back a 404 error with a little HTML message.
                error_msg = "HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
                connectionSocket.send(error_msg.encode())

            # And no matter what happens, I close the connection after the request is handled.
            connectionSocket.close()

    except Exception as e:
        # In case the server crashes for some reason, I print the error.
        print(f"Server error: {e}")

    finally:
        # Before exiting, I make sure to close the server socket and clean up properly.
        serverSocket.close()
        sys.exit()

# This is the starting point.
# If I run this file directly, it starts the server on port 8000.
if __name__ == "__main__":
    start_server(8000)
