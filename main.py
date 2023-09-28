import os

# initial_menu
COMPRESSION = 1
RESOLUTION = 2
AUDIO_CONVERSION = 3
GIF_CONVERSION = 4

lines = 30
INPUT_DIRECTORY = "./input"

def line_wrap_print(mes):
    """
        行等に|をつけてprintする
    """
    print("|", end="")
    print(mes)

def print_menu(string_arr):
    """
        配列で渡した文字列を表示する
    """
    print("-" * lines)
    for i in range(len(string_arr)):
        line_wrap_print(string_arr[i])
    print("-" * lines)

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

def print_compression_menu():
    """
        1.動画の圧縮メニュー
    """
    pass

def compression_main():
    """
        対話的に圧縮について聞き出す関数
    """

def print_resolution_menu():
    """
        2.解像度の変更メニュー
    """
    pass

def resolution_main():
    pass

def print_audio_conversion_menu():
    """
        3.音声ファイルへの変換
    """
    pass

def audio_conversion_main():
    pass

def print_gif_conversion_menu():
    """
        4.GIFへの変換
    """
    pass

def gif_conversion_main():
    pass

def list_input_file() -> list:
    """
        inputフォルダの内容を配列にする
    """
    contents = os.listdir(INPUT_DIRECTORY)
    return contents

def intaractive_shell():
    """
        対話的にメニューを表示して、動画の変換を行う
    """
    # メニューを表示する
    select = input_loop_initial_menu()

    if select == COMPRESSION: compression_main()
    elif select == RESOLUTION: resolution_main()
    elif select == AUDIO_CONVERSION: audio_conversion_main()
    elif select == GIF_CONVERSION: gif_conversion_main()


if __name__ == "__main__":
    intaractive_shell()
