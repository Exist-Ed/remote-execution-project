import socket
import zipfile
import subprocess
from shutil import rmtree
from os import remove

SIZE = 1024
ENCODING_FORMAT = "utf-8"
ARCHIVE_PATH = 'rep_files.zip'
DATA_PATH = '/tmp/rep_data'


def create_server_socket(ip, port, network_layer_protocol=socket.AF_INET,
                         transport_layer_protocol=socket.SOCK_STREAM):
    print("[STARTING] Server is starting.")
    server = socket.socket(network_layer_protocol, transport_layer_protocol)
    server.bind((ip, port))
    print(f'ip:{ip}, port:{port}')
    server.listen()
    print("[LISTENING] Server is listening.")

    return server


def receiving_archive(conn, addr):
    data = bytes()
    while True:
        buffer = conn.recv(SIZE)
        if not buffer:
            break

        data += buffer
    print(f"[RECV] Receiving the data files. ({addr})")

    with open(ARCHIVE_PATH, 'wb') as file:
        file.write(data)
    print(f'[RECV] files received! ({addr})')

    with zipfile.ZipFile(ARCHIVE_PATH, 'r') as archive:
        archive.extractall(DATA_PATH)
    remove(ARCHIVE_PATH)


def run_task(addr):
    subprocess.call('./run_task.sh', shell=True)
    print(f'Task completed! {addr}')


def send_task_output(conn, addr):
    with open(DATA_PATH + '/output.txt', 'r') as output:
        conn.send(output.read().encode(ENCODING_FORMAT))
    print(f'Task output sent to {addr}')


def main():
    server = create_server_socket('127.0.0.1', 10203)

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        receiving_archive(conn, addr)
        run_task(addr)
        send_task_output(conn, addr)

        rmtree(DATA_PATH)

        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")


if __name__ == "__main__":
    main()
