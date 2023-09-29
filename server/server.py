from lib.ffmpeg_tool import * 
from lib._header import *
from lib.json_tool import *
from lib.json_server import *
from lib.file_server import *

import shutil

import time

def main():
    # jsonの受け取り
    json_file_name = json_receive()

    time.sleep(1)

    # fileの受け取り
    recieved_file_name = file_receive()

    # jsonのfileパスを作成する
    json_filepath = "tmp/" + json_file_name
    # 受け取ったfile本体のパスを作成
    recieved_filepath = "tmp/" + recieved_file_name

    # jsonのパース
    command = json_parser(json_filepath)
    
    # 処理を行う
    run_ffmpeg(command)

    # JSONの送信処理
    
    # fileの送信処理

    # 最後に、受け取ったJSONと受け取ったファイルを削除する処理がいる
    clear_tmp_directory()
    pass

def clear_tmp_directory():
    """
        tmpディレクトリを削除する処理
    """
    target_dir = "tmp"
    shutil.rmtree(target_dir)

def json_receive():
    """
        jsonを受け取る処理
    """
    return recieve_json_server()

def json_parser(filepath:str) -> list:
    """
        parseしたJSONからコマンドを作成する
    """
    # json load
    json_dict = load_json(filepath)

    # 変換タイプの指定
    convert_type = json_dict["type"]
    # ffmpegで使うコマンドに直す
    if convert_type == TYPE_AUDIO_CONVERSION:
        command = command_generation_audio_conversion(json_dict)
    elif convert_type == TYPE_GIF_CONVERSION:
        command = command_generation_gif_conversion(json_dict)

    return command

def file_receive():
    """
        fileを受け取る処理
    """
    return recieve_file_server()

def send_converted_file(filepath):
    pass
    

#---------------------------------------------------------
def test_json_parser():
    # OK
    filepath = "tmp/" + "audio_convert.json"
    command = json_parser(filepath)
    return command

def test_command_run():
    # OK
    command = test_json_parser()
    run_ffmpeg(command)

def test_json_server():
    # OK
    recieve_json_server()

if __name__ == "__main__":
    # test_command_run()
    # test_command_generation_gif_conversion()
    # test_gif_convert()
    # test_json_server()
    main()
    # clear_tmp_directory()