from lib.file_select_tool import *

RATIO_4_3 = 1
RATIO_16_9 = 2

def resolution_main():
    """
        2.解像度を変換
        解像度変更用のメイン対話シェル

    """
    dic = {}

    # inputファイル
    contents = ls_input_directory()
    input_file = input_target_file(contents)
    dic["input"] = input_file
    input_file_path = create_file_path(input_file)

    # outputファイル名
    output_file_name = input_output_file_name(".mp4")

    # 解像度を選択してもらう
    input_resolution()

    pass

def input_resolution():

    # select ratio
    ratio = select_ratio()

    # 4:3
    if ratio == RATIO_4_3:
        pass

    # 16:9
    elif ratio == RATIO_16_9:
        pass

    pass


def select_ratio() -> int:
    """
        画面の比率を選択する
    """
    menu = [
        "1. 4:3",
        "2. 16:9"
    ]
    
    while True:
        print_menu(menu)
        print("解像度の縦横比を数字で選択してください")
        select = input("> ")
        # 空白ならもう一度聞く
        if select == "": continue

        # 文字列ならもう一度聞く
        if not select.isdigit(): continue

        if int(select) == RATIO_4_3: return RATIO_4_3
        elif int(select) == RATIO_16_9: return RATIO_16_9

def create_file_path(file_name):
    """
        file保存パスを作成する
    """
    return INPUT_DIRECTORY + "/" + file_name

