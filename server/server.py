from lib.ffmpeg_tool import * 
from lib._header import *
from lib.json_tool import *
from lib.file_server import *

import shutil

import time

def main():
    with TCP_Server(SERVER_PORT) as s:
        # socket
        sock = s.sock
        try:
            # jsonの受け取り
            json_file_name = recieve_file_server(sock)

            # fileの受け取り
            recieved_file_name = recieve_file_server(sock)

            # jsonのfileパスを作成する
            json_filepath = "tmp/" + json_file_name

            # jsonのパース
            command = json_parser(json_filepath)
            output_file_name = "tmp/" + get_output_file_name(json_filepath)
            
            # 処理を行う
            run_ffmpeg(command)

            # JSONの送信処理 <- いる？
            
            # fileの送信処理
            send_file_server(output_file_name, sock)
            # send_converted_file(output_file_name, sock)
        finally:
            # 最後に、受け取ったJSONと受け取ったファイルを削除する処理がいる
            clear_tmp_directory()

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

def get_output_file_name(filepath: str) -> str:
    """
        outputファイル名を取得する
    """
    # json load
    json_dict = load_json(filepath)
    return json_dict["output"]


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
    """
        変換したファイルを受けとる
    """
    

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