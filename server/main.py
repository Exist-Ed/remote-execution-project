import socket
import zipfile
import subprocess
from select import select
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
    print(f"[RECV] Receiving the data files! ({addr})")

    data = bytes()
    while True:
        if select([conn], [], [], 2)[0]:
            buffer = conn.recv(SIZE)
            data += buffer
        else:
            break

    with open(ARCHIVE_PATH, 'wb') as archive:
        archive.write(data)

    with zipfile.ZipFile(ARCHIVE_PATH, 'r') as archive:
        archive.extractall(DATA_PATH)
    remove(ARCHIVE_PATH)

    print(f'[RECV] files received! ({addr})')


def run_task(addr):
    print(f'[TASK] Task execution starts! {addr}')
    subprocess.call('./run_task.sh', shell=True)
    print(f'[TASK] Task completed! {addr}')


def send_task_output(conn, addr):
    with open(DATA_PATH + '/rep_output.txt', 'r') as output:
        data = output.read()
        conn.send(data.encode(ENCODING_FORMAT))
        print(data)
    print(f'[SEND] Task output send to {addr}')


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
