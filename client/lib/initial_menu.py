from print_tool import *

# initial_menu
COMPRESSION = 1
RESOLUTION = 2
AUDIO_CONVERSION = 3
GIF_CONVERSION = 4

def print_initial_menu():
    """
        基本的なメニューを表示する
    """
    arr = ["1.動画を圧縮",
            "2.解像度を変更",
            "3.音声ファイルに変換",
            "4.GIFへの変換",
            ]
    print_menu(arr)

def input_loop_initial_menu():
    """
        initial_menuの項目をループして問い合わせる
    """
    while True:
        print_initial_menu()
        ipt = input("> ")

        # 数字でない
        if not ipt.isdigit(): continue

        # 数字に変換
        ipt = int(ipt)
        if ipt == COMPRESSION: return COMPRESSION
        elif ipt == RESOLUTION: return RESOLUTION
        elif ipt == AUDIO_CONVERSION: return AUDIO_CONVERSION
        elif ipt == GIF_CONVERSION: return GIF_CONVERSION