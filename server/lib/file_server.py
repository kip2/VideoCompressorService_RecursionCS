import os

import lib
from lib.tcp_server import *
from lib._header import *

# network socket type
NETWORK_SOCKET_TYPE = lib._address_config.NETWORK_SOCKET_TYPE 
# server address
SERVER_ADDRESS = lib._address_config.SERVER_ADDRESS 
# server port
JSON_SERVER_PORT = lib._address_config.JSON_SERVER_PORT

FILE_DIRECTORY_PATH = "tmp"
JSON_DIRECTORY_PATH = "tmp"

# header size
HEADER_SIZE = JSON_HEADER_SIZE


def send_file_server(filepath, sock):
    """
        filepathのjsonファイルを送信する
    """
    connection, client_address = sock.accept()

    with open(filepath, "rb") as f:
        f.seek(0, os.SEEK_END)
        filesize = f.tell()
        f.seek(0,0)

        if filesize > pow(2, 32):
            raise Exception("File must be below 2GB.")

        filename = os.path.basename(f.name)

        filename_bits = filename.encode(CHARA_CODE)

        header = create_send_json_header(len(filename_bits), 0, filesize)

        connection.send(header)
        connection.send(filename_bits)

        data = f.read(4096)
        while data:
            print("Sending...")
            connection.send(data)
            data = f.read(4096)

def recieve_file_server(sock):
    create_file_directory()

    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)
        header = connection.recv(HEADER_SIZE)

        filename_length, json_length, data_length = json_header_parsing(header)

        stream_rate = 4096

        filename = connection.recv(filename_length).decode(CHARA_CODE)

        if json_length != 0:
            raise Exception("This data is not currently supported.")
        if data_length == 0:
            raise Exception("No data to read from client.")

        with open(os.path.join(FILE_DIRECTORY_PATH, filename), "wb+") as f:
            while data_length > 0:
                data = connection.recv(data_length if data_length <= stream_rate else stream_rate)
                f.write(data)
                # print(f"recieved {len(data)} bytes")
                data_length -= len(data)
                print(data_length)

        print("Finished downloading the file from client.")
    except Exception as e:
        print("Error: " + str(e))
    return filename
        
def create_file_directory():
    """
        file受け渡しをする fileフォルダを作成する
    """
    if not os.path.exists(FILE_DIRECTORY_PATH):
        os.makedirs(FILE_DIRECTORY_PATH)

def create_json_directory():
    """
        json受け渡しをするjsonフォルダを作成する
    """
    if not os.path.exists(JSON_DIRECTORY_PATH):
        os.makedirs(JSON_DIRECTORY_PATH)

if __name__ == "__main__":
    recieve_file_server()
    pass