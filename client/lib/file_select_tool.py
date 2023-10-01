import sys
import os
from lib._header import *
from lib.print_tool import *

def ls_input_directory() -> list:
    """
        inputフォルダの内容を配列にする
    """
    contents = os.listdir(INPUT_DIRECTORY)
    return contents

def input_target_file(contents: list) -> str:
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

def has_input_directory(contents: list, name: str) -> bool:
    """
        指定のファイルがinputフォルダにあるか確認する
    """
    return name in contents

def input_output_file_name(extension:str) -> str:
    """
        outputファイル名を指定してもらう
    """
    while True:
        print("output時のファイル名を指定してください。(指定ない場合はqを入力)")
        filename = input("> ")
        if filename == "": continue
        if filename == "q": return "output" + "." + extension
        return filename

