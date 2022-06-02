import socket
from zipfile import ZipFile
from os import remove
from os.path import basename

ENCODING_FORMAT = 'utf-8'
ARCHIVE_PATH = 'rep_files.zip'
ORCHESTRATION_SCRIPT_PATH = 'rep_orchestration_script.sh'
SIZE = 1024


def create_client_socket(ip, port,
                         network_layer_protocol=socket.AF_INET,
                         transport_layer_protocol=socket.SOCK_STREAM):
    client = socket.socket(network_layer_protocol, transport_layer_protocol)
    try:
        client.connect((ip.strip(), port))
        return client
    except Exception as e:
        print(e)
        return None


def creating_archive_of_files(filepaths: list, orchestration_script: str):
    zip_archive = ZipFile(ARCHIVE_PATH, 'w')

    with open(ORCHESTRATION_SCRIPT_PATH, 'w') as orch_script:
        orch_script.write(orchestration_script)
    zip_archive.write(ORCHESTRATION_SCRIPT_PATH)
    remove(ORCHESTRATION_SCRIPT_PATH)

    for path in filepaths:
        zip_archive.write(path, basename(path))

    zip_archive.close()


def send_archive(client):
    with open(ARCHIVE_PATH, "br") as file:
        data = file.read()
    client.send(data)
    remove(ARCHIVE_PATH)


def receive_output(client):
    output = bytes()
    while True:
        buffer = client.recv(SIZE)
        if not buffer:
            break

        output += buffer

    return output


def main(ip: str, port: int, filepaths: list, orchestration_script: str):
    client = create_client_socket(ip, port)
    if not client:
        return 'Connection error!'

    creating_archive_of_files(filepaths, orchestration_script)
    send_archive(client)
    output = receive_output(client)

    client.close()

    return output.decode(ENCODING_FORMAT)
