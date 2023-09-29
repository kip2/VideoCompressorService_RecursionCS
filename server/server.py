from lib.ffmpeg_tool import * 
from lib._header import *
from lib.json_tool import *

def json_receive():
    pass

def json_parser(filepath) -> list:
    """
        parseしたJSONからコマンドを作成する
    """
    # json load
    json_dict = load_json(filepath)

    convert_type = json_dict["type"]
    # ffmpeg形式に直す
    if convert_type == TYPE_AUDIO_CONVERSION:
        command = command_generation_audio_conversion(json_dict)
    elif convert_type == TYPE_GIF_CONVERSION:
        command = command_generation_gif_conversion(json_dict)

    return command

def command_generation_audio_conversion(json_dict: dict) -> list:
    """
        mp4をmp3に変換するffmpegコマンドを作成する
    """
    # dictをパースする
    input_file_path = "input/" + json_dict["input"]
    output_file_path = "output/" + json_dict["output"]

    # command
    # ffmpeg -i input_file_name -vn output_file_name
    command = [
        "ffmpeg",
        "-i",
        input_file_path,
        "-vn",
        output_file_path
    ]
    return command

def command_generation_gif_conversion():
    pass

def file_receive():
    pass

def send_converted_file(filepath):
    pass
    
def test_json_parser():
    # OK
    filepath = "tmp/" + "audio_convert.json"
    command = json_parser(filepath)
    return command

def test_command_run():
    # OK
    command = test_json_parser()
    run_ffmpeg(command)


if __name__ == "__main__":
    test_command_run()
    pass