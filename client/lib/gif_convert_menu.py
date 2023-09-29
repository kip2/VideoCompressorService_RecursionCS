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
    # video_size = "300"
    video_size = input_width_size()
    dic["video_size"] = str(video_size)
    
    # フレームレート
    fps = input_fps()
    dic["fps"] = str(fps)

    # 切り取る秒数
    # start_time = "00:00:00"
    # end_time = "10"
    start_time = input_start_time()
    end_time = input_end_time()
    dic["start_time"] = seconds_to_hms(start_time)
    dic["end_time"] = str(end_time)

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

def input_end_time() -> int:
    """
        動画を切り取るエンドタイムを指定してもらう
    """
    while True:
        print("動画を切り取る終了時間を指定してください")
        end_time = int(input("> "))
        # todo: 一旦、マイナスでなければ通るようにした
        # todo: 動画時間を取得して、引数として渡しておく。その時刻と、引数で渡すスタートタイム以下あるいは以上の時刻ならやり直す
        if end_time <= 0 : continue
        else: return end_time


def input_start_time() -> int:
    """
        動画を切り取るスタートタイムを指定してもらう
    """
    while True:
        print("動画を切り取る開始時間を指定してください")
        start_time = int(input("> "))
        # todo: 一旦、マイナスでなければ通るようにした
        # todo: 動画時間を取得して、引数として渡す。その時間-1秒以上なら、ダメとする
        if start_time <= 0 : continue
        else: return start_time

def seconds_to_hms(seconds):
    """
        秒数を00:00:00形式に変換する
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

def input_width_size() -> int:
    """
        固定したい横幅を指定してもらう
    """
    while True:
        print("固定したい横幅を指定してください")
        width = int(input("> "))
        if width <= 0 : continue
        else: return width


def input_fps() -> int:
    """
        変換したいフレームレートを入力してもらう(1~60)
    """
    while True:
        print("変換したいフレームレートを入力してください(1~60)")
        fps = int(input("> "))
        if fps < 1 or 60 < fps: continue
        else: return fps
