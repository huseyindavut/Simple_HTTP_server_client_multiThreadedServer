import socket
import threading
import sys

# In this part, I'm importing the basic libraries I need.
# socket is for network stuff, threading so I can handle multiple clients at once,
# and sys just in case I wanna exit the program properly or handle something later.

def handle_client(connectionSocket, addr):
    '''
    Description:
        This function handles a single HTTP client request in a separate thread.

    Arguments:
        connectionSocket: the socket connected to the client
        addr: client address

    Returns:
        None

    Exceptions:
        Handles IOError for missing files, sends 404 Not Found
    '''
    try:
        # Here I just print which client is connecting, just to keep track of things.
        print(f"Handling request from {addr}")

        # So I receive the HTTP request from the client and decode it so I can read it as text.
        message = connectionSocket.recv(1024).decode()
        print("Received message:\n", message)

        # This line extracts the file name from the GET request line.
        # I split by space and take the second item, which is usually like /index.html
        filename = message.split()[1]

        # The filename comes with a '/' at the start, so I remove it here to match actual file name
        filepath = filename[1:]

        # I try to open the requested file and read its content.
        # If it's found, I prepare a 200 OK response and send both header and content back.
        with open(filepath, 'r') as f:
            content = f.read()

        # This is just a basic HTTP header saying everything's OK and the content is HTML.
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(content.encode())

    except IOError:
        # If the file wasn't found or can't be opened, then I catch the error and
        # send back a simple 404 Not Found response to the client.
        error_msg = "HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
        connectionSocket.send(error_msg.encode())

    finally:
        # No matter what happens, I close the connection at the end so we don't leave it hanging.
        connectionSocket.close()

def start_threaded_server(port):
    '''
    Description:
        Starts a multi-threaded HTTP server that accepts and handles multiple clients simultaneously.

    Arguments:
        port: Port number to listen on

    Returns:
        None
    '''
    # So first, I create a socket for the server using IPv4 and TCP.
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Then I bind this socket to the given port so it can start listening.
    # '' means all interfaces, like localhost or whatever IP the machine has.
    serverSocket.bind(('', port))

    # I tell it to listen for incoming connections. 5 is the max number of queued connections.
    serverSocket.listen(5)

    # Just a log to let me know the server is up and running.
    print(f"[THREAD-SERVER] Running on http://127.0.0.1:{port}")

    try:
        while True:
            # This part waits for a new client to connect.
            # When it happens, I accept the connection and get their address.
            connectionSocket, addr = serverSocket.accept()

            # I create a new thread to handle this client so the main server can keep listening.
            client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
            client_thread.start()

    except KeyboardInterrupt:
        # If I press Ctrl+C to stop the server manually, I print this message.
        print("\n[!] Server shutting down.")

    finally:
        # Either way, I always close the socket and exit cleanly when done.
        serverSocket.close()
        sys.exit()

# This is the main entry point of the program.
# If I run this file directly, it'll start the server on port 8080.
if __name__ == "__main__":
    start_threaded_server(8080)
