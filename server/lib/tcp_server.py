import sys
import socket
from ._address_config import *
from ._header import *

class TCP_Server:
    def __init__(self, port):
        self.sock, self.addr, self.port = startup_tcp_server(server_port=port)

    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.sock.close()

def startup_tcp_server(server_address:str = SERVER_ADDRESS, server_port:int = SERVER_PORT, listen=5) -> tuple:
    """
        TCPサーバーを立てる関数
        connect用のsocketと、(IP_address, PORT)のタプルを返す
    """
    try:
        sock = socket.socket(NETWORK_SOCKET_TYPE, socket.SOCK_STREAM) 
        sock.bind((server_address, server_port))
        sock.listen(listen)
        return (sock, server_address, server_port)
    except (socket.timeout, ConnectionRefusedError):
        return

def send_server_message(connection, message):
    """
        connectionに、messageをutf-8にencodeして送る関数
    """
    connection.send(message.encode(CHARA_CODE))

def server_exit(sock):
    """
        serverのソケット終了処理
    """
    sock.close()
    sys.exit(0)
