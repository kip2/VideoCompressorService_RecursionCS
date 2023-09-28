import os
from lib.json_tool import *
from lib.print_tool import *
from lib.initial_menu import *
from lib.file_select_tool import *

# initial_menu
COMPRESSION = 1
RESOLUTION = 2
AUDIO_CONVERSION = 3
GIF_CONVERSION = 4

INPUT_DIRECTORY = "./input"
OUTPUT_DIRECTORY = "./output"

TMP_DIRECTORY = "tmp"

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


# todo: 以下、メニューごとに、JSONファイルにするのに必要なことを対話的に聞くようにすること
# todo: とにかくjsonファイルを作る目的でいけばかなり素早くコードが書けると思う
# todo: 全て、4つの関数はjsonを返すようにする。それを持って、あとは受け渡しするためのソケットクライアントを一つだけ作成して、その窓口を通してサーバーに渡すことにする

def print_compression_menu():
    """
        1.動画の圧縮メニュー
        H,M,L
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

def gif_conversion_main():
    """
        4.GIFへの変換
    """
    dic = {}
    # inputファイル
    contents = ls_input_directory()
    input_file = input_target_file(contents)
    dic["input"] = input_file

    # 固定比
    # 横幅に合わせて調整するオプション
    # todo:一旦、ハードコードして返す
    video_size = "300:-1"
    dic["video_size"] = video_size
    
    # フレームレート
    fps = input_fps()
    dic["fps"] = fps

    # 切り取る秒数
    # todo: 一旦、無視するといいかも
    start = "00:00:00"
    end = "10"
    dic["start"] = start
    dic["end"] = end

    # outputファイル名
    output_file_name = input_output_file_name(".gif")
    dic["output"] = output_file_name

    # jsonファイル作成
    json_dic = create_gif_conversion_json(dic)
    return json_dic

def create_gif_conversion_json(dic):
    """
        gif変換用のjsonファイルを作成
    """
    dic["filesize"] = os.stat(dic["input"]).st_size
    dic["type"] = "gif conversion"
    return dic


def input_fps() -> int:
    """
        変換したいフレームレートを入力してもらう(1~60)
    """
    while True:
        print("変換したいフレームレートを入力してください(1~60)")
        fps = int(input("> "))
        if fps < 1 or 60 < fps: continue
        else: return fps


# todo: いずれツール行き
def input_output_file_name(extension) -> str:
    """
        outputファイル名を指定してもらう
    """
    while True:
        print("output時のファイル名を指定してください。(指定ない場合はqを入力)")
        filename = input("> ")
        if filename == "q": return "output" + extension
        return filename

def test_has_input_directory():
    contents = ls_input_directory()
    while True:
        print_menu(contents)
        name = input("> ")
        t = has_input_directory(contents, name)
        if t : break
        print(t)
    print(t)


if __name__ == "__main__":
    # intaractive_shell()
    # print_input_directory()
    # test_has_input_directory()
    # audio_conversion_main()
    input_fps()