import os
from lib.json_tool import *
from lib.print_tool import *
from lib.initial_menu import *
from lib.file_select_tool import *
from lib.audio_convert_menu import *
from lib.gif_convert_menu import *

# initial_menu
COMPRESSION = 1
RESOLUTION = 2
AUDIO_CONVERSION = 3
GIF_CONVERSION = 4

INPUT_DIRECTORY = "./input"
OUTPUT_DIRECTORY = "./output"

TMP_DIRECTORY = "tmp"

def intaractive_shell():
    """
        対話的にメニューを表示して、動画の変換を行う
    """
    # メニューを表示する
    select = input_loop_initial_menu()

    if select == COMPRESSION: compression_main()
    elif select == RESOLUTION: resolution_main()
    elif select == AUDIO_CONVERSION: audio_conversion_main()
    elif select == GIF_CONVERSION: gif_conversion_main()

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

def resolution_main():
    pass

def test_has_input_directory():
    contents = ls_input_directory()
    while True:
        print_menu(contents)
        name = input("> ")
        t = has_input_directory(contents, name)
        if t : break
        print(t)
    print(t)


if __name__ == "__main__":
    # intaractive_shell()
    # print_input_directory()
    # test_has_input_directory()
    # audio_conversion_main()
    # input_fps()
    pass
