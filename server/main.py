import socket

SIZE = 1024
ENCODING_FORMAT = "utf-8"


def create_server_socket(ip, port, network_layer_protocol=socket.AF_INET,
                         transport_layer_protocol=socket.SOCK_STREAM):
    print("[STARTING] Server is starting.")
    server = socket.socket(network_layer_protocol, transport_layer_protocol)
    server.bind((ip, port))
    print(f'ip:{ip}, port:{port}')
    server.listen()
    print("[LISTENING] Server is listening.")

    return server


def main():
    server = create_server_socket('127.0.0.1', 10203)

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(ENCODING_FORMAT)
        print(f"[RECV] Receiving the filename {filename}. ({addr})")

        """ Receiving the file data from the client. """
        data = bytes()
        while True:
            buffer = conn.recv(SIZE)
            if not buffer:
                break

            data += buffer
        print(f"[RECV] Receiving the file data. ({addr})")

        with open(filename.split('/')[-1], 'wb') as file:
            file.write(data)
        print(f'[RECV] file received! ({addr})')

        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")


if __name__ == "__main__":
    main()
