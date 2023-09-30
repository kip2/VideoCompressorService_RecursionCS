import os
from lib.json_tool import *
from lib.file_select_tool import *
from client_main import *

TMP_DIRECTORY = "json"

def audio_conversion_main() -> str:
    """
        3.音声ファイルへの変換
        音声ファイル変換のメイン対話シェル
        jsonのfilepathを返す
    """
    # inputディレクトリの内容を取得
    contents = ls_input_directory()
    # inputディレクトリから変換対象を選ばせる
    input_file = input_target_file(contents)
    # jsonファイル用辞書を作成
    d = create_audio_conversion_json(input_file)
    # jsonファイルを作成する
    json_filepath = TMP_DIRECTORY+ "/" + create_json_file_name("audio_convert")
    save_json(d, json_filepath)

    # 変換対象のファイルパスを作成
    input_file_path = create_file_path(input_file)

    # サーバーにJSONを渡す
    
    # サーバーにfileを渡す

    return json_filepath

def create_audio_conversion_json(file):
    """
        音声変換用のjsonファイルを作成
    """
    json_dict = {}
    json_dict["input"] = file 
    json_dict["filesize"] = os.stat(file).st_size
    json_dict["output"] = "output_" + file + ".mp3"
    json_dict["type"] = "audio conversion"
    return json_dict
