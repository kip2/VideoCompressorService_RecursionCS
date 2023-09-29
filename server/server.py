from lib.ffmpeg_tool import * 
from lib._header import *
from lib.json_tool import *
from lib.json_server import *
from lib.file_server import *

def main():
    filename = json_receive()

    # filepathを作成する
    filepath = "tmp/" + filename

    # jsonのパース
    command = json_parser(filepath)

    pass

def json_receive():
    """
        jsonを受け取る処理
    """
    recieve_json_server()

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
    filename = recieve_file_server()
    
    pass

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
    recieve_json_server()

if __name__ == "__main__":
    # test_command_run()
    # test_command_generation_gif_conversion()
    # test_gif_convert()
    test_json_server()
    pass