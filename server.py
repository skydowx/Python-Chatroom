import argparse
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        clients.append(client)
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    while True:
        try: 
            msg = client.recv(BUFSIZ)

            if msg.decode():
                send_message(msg, client)

            else: 
                # message may have no content if the connection 
                # is broken, in this case we remove the connection
                remove(client)
                print("Removed a client")

        except: 
            continue


def send_message(msg, connection):
    """Broadcasts a message to all the clients."""
    for client in clients:
        if client!=connection:
            try:
                client.send(msg)
            except:
                # Close a broken connection
                client.close()
                remove(client)

def remove(connection):
    clients.remove(connection)

clients = []

parser = argparse.ArgumentParser(description="Python-Chatroom")

parser.add_argument(
    '--host',
    help='Host IP',
    default="127.0.0.1"
)

parser.add_argument(
    '--port',
    help='Port Number',
    default=8000
)

server_args = parser.parse_args()


HOST = server_args.host
PORT = int(server_args.port)
BUFSIZ = 2048
ADDR = (HOST, PORT)

stop_server = False

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    try:
        SERVER.listen(5)
        print("Server Started at {}:{}".format(HOST, PORT))
        print("Waiting for connection...")
        ACCEPT_THREAD = Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        SERVER.close()
    except KeyboardInterrupt:
        print("Closing...")
        ACCEPT_THREAD.interrupt()
