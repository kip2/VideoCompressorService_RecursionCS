import os
from ._header import *
from .tcp_client import *

def recieve_file_client(directory_path):
    with TCP_Client(SERVER_ADDRESS, SERVER_PORT) as c:
        try:
            header = c.sock.recv(HEADER_SIZE)

            # header のパース
            filename_length, json_length, data_length = json_header_parsing(header)
            stream_rate = 4096

            filename = c.sock.recv(filename_length).decode(CHARA_CODE)

            if json_length != 0:
                raise Exception("This data is not currently supported.")
            if data_length == 0:
                raise Exception("No data to read from client.")

            with open(os.path.join(directory_path, filename), "wb+") as f:

                print("recieved...", end="")
                while data_length > 0:
                    data = c.sock.recv(data_length if data_length <= stream_rate else stream_rate)
                    f.write(data)
                    data_length -= len(data)

            print()
            print("Finished download!")
        except Exception as e:
            print("Error: " + str(e))
    return

def send_file_client(filepath):
    with TCP_Client(SERVER_ADDRESS, SERVER_PORT) as c:

        with open(filepath, "rb") as f:
            f.seek(0, os.SEEK_END)
            filesize = f.tell()
            f.seek(0,0)

            if filesize > pow(2, 32):
                raise Exception("File must be below 2GB.")

            filename = os.path.basename(f.name)

            filename_bits = filename.encode(CHARA_CODE)

            header = create_send_json_header(len(filename_bits), 0, filesize)

            c.sock.send(header)
            c.sock.send(filename_bits)

            data = f.read(4096)
            while data:
                # print("Sending...")
                c.sock.send(data)
                data = f.read(4096)


