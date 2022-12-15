import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = "192.168.1.11"
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
# print(socket.gethostname())

ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(connection, address):
    print("[NEW CONNECTION] {address} connected.")

    connected = True
    while connected:
        message_length = connection.recieve(HEADER).decode(FORMAT)
        message_length = int(message_length)
        message = connection.recieve(message_length).decode(FORMAT)
        print(f"[{address}] {message}")

def start():
    server.listen()
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print(f"[STARTING] server is starting...")
start()