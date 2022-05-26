import socket

SIZE = 1024
FORMAT = "utf-8"


def create_server_instance(ip, port, network_layer_protocol=socket.AF_INET,
                           transport_layer_protocol=socket.SOCK_STREAM):
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    print(f'ip:{ip}, port:{port}')
    server.listen()
    print("[LISTENING] Server is listening.")

    return server


def main():
    server = create_server_instance(socket.gethostbyname(socket.gethostname()), 10203)

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename {filename}")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the client. """
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))

        """ Closing the file. """
        file.close()

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")


if __name__ == "__main__":
    main()
