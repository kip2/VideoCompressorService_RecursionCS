import os
from lib._header import *
from lib.json_tool import *
from lib.print_tool import *
from lib.initial_menu import *
from lib.file_select_tool import *
from lib.audio_convert_menu import *
from lib.gif_convert_menu import *
from lib.resolution_convert_menu import *
from lib.compression_convert_menu import *
from lib.file_client import *


def intaractive_shell() -> None:
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


def create_file_path(file_name: str) -> str:
    """
        file保存パスを作成する
    """
    return INPUT_DIRECTORY + "/" + file_name


def crate_json_path(json_name: str) -> str:
    """
        jsonの保存パスを作成する
    """
    return JSON_DIRECTORY + "/" + json_name

def setup_directory() -> None:
    """
        最初に、必要なファイルを生成する
    """
    # input
    if not os.path.isdir(INPUT_DIRECTORY):
        os.mkdir(INPUT_DIRECTORY)

    # json
    if not os.path.isdir(JSON_DIRECTORY):
        os.mkdir(JSON_DIRECTORY)

    # output
    if not os.path.isdir(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)


# ------------------test code--------------------------
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
    filepath = JSON_DIRECTORY + "/" + "audio_convert.json"
    send_file_client(filepath)

def test_audio_conversion_main():
    j, i = audio_conversion_main()

def test_gif_convert_main():
    j, i = gif_conversion_main()
    print("test")

def test_select_ratio():
    # ok
    s = select_ratio()
    print(s)

def test_input_resolution():
    # ok
    w, h = select_resolution()

    print("w:", w, "h:", h)

def test_resolution_main():
    t = resolution_main()
    print(t)

def test_compression_main():
    j, i = compression_main()
    print("test")

def test_input_target_file():
    l = ls_input_directory()
    input_target_file(l)


def test_get_vide_length():
    file = "testmov.mp4"
    video_path = create_file_path(file)
    get_video_length(video_path)


def test_input_time():
    input_file_path = create_file_path("testmov.mp4")
    video_length = get_video_length(input_file_path)
    start_time = input_start_time(video_length)
    end_time = input_end_time(start_time, video_length)
    return 

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
    # test_select_ratio()
    # test_input_resolution()
    # test_resolution_main()
    # test_compression_main()

    # test_input_target_file()
    # intaractive_shell()
    # test_get_vide_length()
    test_input_time()
    pass

