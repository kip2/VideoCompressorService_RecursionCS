import time
import os
from lib.json_tool import *
from lib.print_tool import *
from lib.initial_menu import *
from lib.file_select_tool import *
from lib.audio_convert_menu import *
from lib.gif_convert_menu import *
from lib.json_client import *
from lib.file_client import *

# initial_menu
COMPRESSION = 1
RESOLUTION = 2
AUDIO_CONVERSION = 3
GIF_CONVERSION = 4

INPUT_DIRECTORY = "input"
OUTPUT_DIRECTORY = "output"

# JSON_DIRECTORY = "tmp"
JSON_DIRECTORY = "json"

def intaractive_shell():
    """
        対話的にメニューを表示して、動画の変換を行う
    """

    # 必要なディレクトリを作成する
    setup_directory()

    # メニューを表示する
    select = input_loop_initial_menu()

    # 分岐して、変換対象のファイルパスと、jsonのパスを作成
    if select == COMPRESSION: 
        json_file_path, input_file_path = compression_main()
    elif select == RESOLUTION: 
        json_file_path, input_file_path = resolution_main()
    elif select == AUDIO_CONVERSION:
        json_file_path, input_file_path = audio_conversion_main()
    elif select == GIF_CONVERSION:
        json_file_path, input_file_path = gif_conversion_main()

    # jsonファイルを送信
    send_file_client(json_file_path)

    # 変換ファイルを送信
    send_file_client(input_file_path)

    # 変換後のファイルを受け取る
    recieve_file_client(OUTPUT_DIRECTORY)

# todo: 以下、メニューごとに、JSONファイルにするのに必要なことを対話的に聞くようにすること
# todo: とにかくjsonファイルを作る目的でいけばかなり素早くコードが書けると思う
# todo: 全て、4つの関数はjsonを返すようにする。それを持って、あとは受け渡しするためのソケットクライアントを一つだけ作成して、その窓口を通してサーバーに渡すことにする

def print_compression_menu():
    """
        1.動画の圧縮メニュー
        H,M,L
    """

    pass

def compression_main():
    """
        対話的に圧縮について聞き出す関数
    """
    pass

def print_resolution_menu():
    """
        2.解像度の変更メニュー
    """
    pass

def create_file_path(file_name):
    """
        file保存パスを作成する
    """
    return INPUT_DIRECTORY + "/" + file_name


def crate_json_path(json_name):
    """
        jsonの保存パスを作成する
    """
    return JSON_DIRECTORY + "/" + json_name

def setup_directory():
    """
        最初に、必要なファイルを生成する
    """
    # input
    if not os.path.isdir(INPUT_DIRECTORY):
        os.mkdir(INPUT_DIRECTORY)

    # json
    if not os.path.isdir(JSON_DIRECTORY_PATH):
        os.mkdir(JSON_DIRECTORY_PATH)

    # output
    if not os.path.isdir(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

def test_has_input_directory():
    contents = ls_input_directory()
    while True:
        print_menu(contents)
        name = input("> ")
        t = has_input_directory(contents, name)
        if t : break
        print(t)
    print(t)

def test_send_json_file():
    # OK
    # jsonディレクトリはclient内にないといけない
    filepath = JSON_DIRECTORY_PATH + "/" + "audio_convert.json"
    send_file_client(filepath)

def test_send_file():
    filepath = INPUT_DIRECTORY_PATH + "/" + "nc53235.mp4"
    send_file_client(filepath)

def test_audio_conversion_main():
    j, i = audio_conversion_main()

def test_gif_convert_main():
    j, i = gif_conversion_main()
    print("test")

if __name__ == "__main__":
    # intaractive_shell()
    # print_input_directory()
    # test_has_input_directory()
    # audio_conversion_main()
    # input_fps()
    # test_send_json_file()
    # main()
    # setup_directory()
    # test_audio_conversion_main()
    # test_gif_convert_main()
    intaractive_shell()
    pass

