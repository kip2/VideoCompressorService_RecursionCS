import os
from lib.json_tool import *
from lib.file_select_tool import *

TMP_DIRECTORY = "tmp"

def audio_conversion_main() -> str:
    """
        3.音声ファイルへの変換
        音声ファイル変換のメイン対話シェル
        jsonのfilepathを返す
    """
    contents = ls_input_directory()
    file = input_target_file(contents)
    d = create_audio_conversion_json(file)
    filepath = TMP_DIRECTORY+ "/" + create_json_file_name("audio_convert")
    save_json(d, filepath)
    return filepath

def create_audio_conversion_json(file):
    """
        音声変換用のjsonファイルを作成
    """
    json_dict = {}
    # json_dict["input"] = file + ".mp4"
    json_dict["input"] = file 
    json_dict["filesize"] = os.stat(file).st_size
    json_dict["output"] = "output_" + file + ".mp3"
    json_dict["type"] = "audio conversion"
    return json_dict