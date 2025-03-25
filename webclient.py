import socket
import argparse

# Here I imported the socket and argparse libraries.
# I'm using socket to create the network connection,
# and argparse so I can grab the IP, port, and filename from the terminal input.

def send_get_request(ip, port, filename):
    '''
    Description:
        This function connects to a given IP and port, sends an HTTP GET request
        for the specified filename, and prints the response from the server.

    Arguments:
        ip: IP address of the server (e.g., 127.0.0.1)
        port: Port number of the server (e.g., 8000)
        filename: The file to request from the server (e.g., index.html)

    Returns:
        None

    Exceptions:
        Prints error message if connection fails or server doesn't respond.
    '''
    try:
        # In this line, I created a client socket to make a TCP connection.
        # I'm using stream mode because web traffic is based on TCP anyway.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Then I connected this socket to the server.
        # The IP and port are coming from user input already.
        client_socket.connect((ip, port))

        # Now here I manually build a simple HTTP GET request.
        # Something like: GET /index.html HTTP/1.1
        # I also added the Host line just to make it more proper—some servers require it.
        request = f"GET /{filename} HTTP/1.1\r\nHost: {ip}:{port}\r\n\r\n"

        # I sent this request to the server. Used encode() to convert it to bytes.
        client_socket.send(request.encode())

        # Now I’m receiving the server’s response here. 4096 bytes is usually enough.
        # Then I decode it so it’s readable text again.
        response = client_socket.recv(4096).decode()

        # I printed the full response to the terminal. It includes the header and the body.
        print("----- Server Response -----")
        print(response)

        # After all that, I closed the connection. No need to leave it open.
        client_socket.close()

    except Exception as e:
        # If something goes wrong—like server not reachable or whatever—it ends up here.
        # Then I just show a simple error message to the user.
        print(f"Connection failed: {e}")


if __name__ == "__main__":
    # I'm using argparse here to grab command line arguments.
    # The user needs to provide IP, port, and the file name.
    parser = argparse.ArgumentParser(description="Simple HTTP Client")

    # Here I defined three arguments. All of them are required.
    parser.add_argument("-i", "--ip", type=str, required=True, help="Server IP address")
    parser.add_argument("-p", "--port", type=int, required=True, help="Server port number")
    parser.add_argument("-f", "--file", type=str, required=True, help="Filename to request")

    # With this line, I parse and collect all the arguments.
    args = parser.parse_args()

    # Then I use the arguments to call the function that sends the GET request.
    send_get_request(args.ip, args.port, args.file)
