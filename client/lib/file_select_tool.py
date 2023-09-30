import sys
import os
from lib.print_tool import *

INPUT_DIRECTORY = "input"

JSON_DIRECTORY = "json"

def ls_input_directory() -> list:
    """
        inputフォルダの内容を配列にする
    """
    contents = os.listdir(INPUT_DIRECTORY)
    return contents

def input_target_file(contents):
    """
        変換対象のファイルを取得
    """
    # todo: mp4でなければ弾く処理がいる
    while True:
        if len(contents) == 0:
            print("inputフォルダにファイルがありません")
            sys.exit(1)
        print_menu(contents)
        print("変換するfile名を指定してください")
        file = input("> ")
        if has_input_directory(contents, file):
            return file

def has_input_directory(contents, name):
    """
        指定のファイルがinputフォルダにあるか確認する
    """
    for item in contents:
        if name == item: return True
    return False

def input_output_file_name(extension) -> str:
    """
        outputファイル名を指定してもらう
    """
    while True:
        print("output時のファイル名を指定してください。(指定ない場合はqを入力)")
        filename = input("> ")
        if filename == "": continue
        if filename == "q": return "output" + extension
        return filename