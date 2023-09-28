import os
from lib.print_tool import *

INPUT_DIRECTORY = "./input"

TMP_DIRECTORY = "tmp"

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
    while True:
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