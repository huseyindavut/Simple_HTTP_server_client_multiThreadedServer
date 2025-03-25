# 🖥️ Simple Python HTTP Server & Client Project

This project demonstrates a basic HTTP server and client system using Python’s socket programming. It includes three Python scripts:

- **`webserver.py`** – A simple single-threaded HTTP server
- **`multi_threaded_webserver.py`** – A multi-threaded server that handles multiple clients
- **`webclient.py`** – A basic HTTP client that sends GET requests to the server

---

## 🔧 How It Works

### 📌 `webserver.py`
- A basic HTTP server that listens on **port 8000**.
- Accepts **one client at a time**.
- If a client sends an HTTP **GET request**, it looks for the requested file in the server’s directory.
- If the file exists, it returns the file with a **200 OK** header.
- If the file does **not** exist, it returns a **404 Not Found** HTML message.
- Great for learning the basics of sockets and HTTP request handling.

### 📌 `multi_threaded_webserver.py`
- An advanced version of `webserver.py` that handles **multiple clients** using threads.
- Each client connection runs in **its own thread**, allowing simultaneous requests.
- Listens on **port 8080**.
- More realistic for testing real-world HTTP server behavior.

### 📌 `webclient.py`
- A simple HTTP client that sends **GET requests** to a server.
- Run it from the terminal using `-i`, `-p`, and `-f` arguments:
  - **`-i`** : Server IP
  - **`-p`** : Port number
  - **`-f`** : Filename to request
- Prints the full server response (including headers and HTML) in the terminal.
- If the requested file does **not** exist on the server, it displays the **404 error message**.

---

## 🚀 How to Run

### 1️⃣ Start the Server:
```sh
python3 multi_threaded_webserver.py
```

### 2️⃣ Run the Client:
```sh
python3 webclient.py -i <SERVER_IP> -p 8080 -f index.html
```

⚡ Replace `<SERVER_IP>` with the actual server IP address.

---

## 📌 Example Usage

```sh
python3 webclient.py -i 127.0.0.1 -p 8080 -f index.html
```

This will request `index.html` from the **multi-threaded web server** running on localhost (`127.0.0.1`) at port `8080`.

---

