import os
from lib.json_tool import *
from lib.print_tool import *
from lib.initial_menu import *
from lib.file_select_tool import *

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

def print_compression_menu():
    """
        1.動画の圧縮メニュー
    """
    pass

def compression_main():
    """
        対話的に圧縮について聞き出す関数
    """

def print_resolution_menu():
    """
        2.解像度の変更メニュー
    """
    pass

def resolution_main():
    pass

def audio_conversion_main() -> str:
    """
        3.音声ファイルへの変換
        音声ファイル変換のメイン対話シェル
        jsonのfilepathを返す
    """
    contents = ls_input_directory()
    file = input_target_file(contents)
    d = create_audio_conversion_json(file)
    filepath = TMP_DIRECTORY+ "/" + create_json_file_name(file)
    save_json(d, filepath)
    return filepath

def create_audio_conversion_json(file):
    """
        音声変換用のjsonファイルを作成
    """
    json_dict = {}
    json_dict["input"] = file + ".mp4"
    json_dict["filesize"] = os.stat(file).st_size
    json_dict["output"] = "output_" + file + ".mp3"
    json_dict["type"] = "audio conversion"
    return json_dict

def print_gif_conversion_menu():
    """
        4.GIFへの変換
    """
    pass

def gif_conversion_main():
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
    audio_conversion_main()