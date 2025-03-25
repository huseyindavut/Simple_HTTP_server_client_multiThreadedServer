README – Simple Python HTTP Server & Client Project


This project demonstrates a basic HTTP server and client system using Python’s socket programming. It includes three Python scripts:

webserver.py – a simple single-threaded HTTP server

multi_threaded_webserver.py – an improved server that handles multiple clients using threads

webclient.py – a basic HTTP client that sends GET requests to the server

🔧 How It Works

1. webserver.py
This script is a very simple HTTP server that listens on port 8000. It accepts one client at a time. When a client connects and sends an HTTP GET request, it tries to find the requested file in the server’s directory. If the file exists, it sends back the file with a 200 OK header. If not, it responds with a 404 Not Found HTML message. It’s good for learning the basics of sockets and how HTTP requests are parsed.

2. multi_threaded_webserver.py
This version is more advanced. It still does the same job as webserver.py, but it can handle multiple client connections at the same time by using threads. Every new client connection runs in its own thread, so the server doesn’t block while waiting for one client to finish. It listens on port 8080 and is better for testing real-world behavior.

3. webclient.py
This is a client that sends HTTP GET requests to a server. You run it from the terminal with the -i, -p, and -f arguments, where you provide the server IP, port, and filename you want to request. It prints the full server response (including headers and HTML) to the terminal. If the file doesn’t exist on the server, it will show the 404 error message returned by the server.

🚀 How to Run

1- Start the server:

python3 multi_threaded_webserver.py


2- From another terminal or another Mininet node, run the client:


python3 webclient.py -i <SERVER_IP> -p 8080 -f index.html
