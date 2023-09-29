import os
from lib.json_tool import *
from lib.print_tool import *
from lib.file_select_tool import *

TMP_DIRECTORY = "tmp"

def gif_conversion_main() -> str:
    """
        4.GIFへの変換
        jsonのファイルパスを返す
    """
    dic = {}
    # inputファイル
    contents = ls_input_directory()
    input_file = input_target_file(contents)
    dic["input"] = input_file

    # 固定比
    # 横幅に合わせて調整するオプション
    # todo:一旦、ハードコードして返す
    video_size = "300"
    dic["video_size"] = video_size
    
    # フレームレート
    fps = input_fps()
    dic["fps"] = fps

    # 切り取る秒数
    # todo: 一旦、無視するといいかも
    start_time = "00:00:00"
    end_time = "10"
    dic["start_time"] = start_time
    dic["end_time"] = end_time

    # outputファイル名
    output_file_name = input_output_file_name(".gif")
    dic["output"] = output_file_name

    # jsonファイル作成
    json_dic = create_gif_conversion_json(dic)
    filepath = TMP_DIRECTORY+ "/" + create_json_file_name("gif_convert")
    save_json(json_dic, filepath)
    return filepath

def create_gif_conversion_json(dic) -> dict:
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
