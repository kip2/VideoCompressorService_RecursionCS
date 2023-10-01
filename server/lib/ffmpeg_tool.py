import subprocess

OUTPUT_DIRECTORY = "tmp"

def command_generation_compression(json_dict: dict) -> list:
    """
        mp4を圧縮するコマンドを生成
    """
    # dictをパースする
    input_file_path = "tmp/" + json_dict["input"]
    output_file_path = "tmp/" + json_dict["output"]
    video_codec = json_dict["video codec"]
    audio_codec = json_dict["audio codec"]
    tune = json_dict["tune"]
    preset = json_dict["preset"]
    crf = json_dict["crf"]
    bit_rate = json_dict["bit rate"]

    # commandを作成
    # 以下、一例
    # ffmpeg -i input.mp4 -c:v libx264 -tune zerolatency -preset ultrafast -crf 40 -c:aac -b:a 32k output.mp4
    command = [
        "ffmpeg",
        "-i",
        input_file_path,
        # ビデオのコーデックを指定
        "-c:v",
        video_codec,
        # 最適化
        "-tune",
        tune,
        # プリセット
        "-preset",
        preset,
        # CRF(Constant Rate Factor)
        "-crf",
        crf,
        # オーディオのコーデック
        "-c:a",
        audio_codec,
        # オーディオのビットレート
        "-b:a",
        bit_rate,
        output_file_path
    ]
    return command


def command_generation_resolution(json_dict: dict) -> list:
    """
        mp4の解像度を変更するコマンドを生成
    """
    # dictをパースする
    input_file_path = "tmp/" + json_dict["input"]
    output_file_path = "tmp/" + json_dict["output"]
    scale = json_dict["width"] + ":" + json_dict["height"]

    # commandを作成
    # ffmpeg -i input.mp4 -filter:v scale=1280:720 -c:a copy output.mp4
    command = [
        "ffmpeg",
        "-i",
        input_file_path,
        "-vf" ,
        "scale=" + scale,       # 変換するvideoの解像度
        "-c:a",
        "copy",        # オーディオの変換は行わず、そのままオーディオを新しいファイルで使う
        output_file_path
    ]
    return command


def command_generation_audio_conversion(json_dict: dict) -> list:
    """
        mp4をmp3に変換するffmpegコマンドを作成する
    """
    # dictをパースする
    input_file_path = "tmp/" + json_dict["input"]
    output_file_path = "tmp/" + json_dict["output"]

    # commandを作成
    # ffmpeg -i input_file_name -vn output_file_name
    command = [
        "ffmpeg",
        "-y",
        "-i",
        input_file_path,
        "-vn",
        output_file_path
    ]
    return command

def command_generation_gif_conversion(json_dict:dict) -> list:
    """
        mp4をgifに変換するffmpegコマンドを作成する
    """

    # dictをパースする
    input_file_path = "tmp/" + json_dict["input"]
    output_file_path = "tmp/" + json_dict["output"]
    start_time = json_dict["start_time"]
    end_time = json_dict["end_time"]
    fps = json_dict["end_time"]
    scale = "scale="+json_dict["video_size"]+":-1"

    # commandを作成
    # ffmpeg -ss 00:00:20 -i input.mp4 -to 10 -r 10 -vf scale=300:-1 output.gif
    command = [
        "ffmpeg",
        "-y",
        "-ss",
        start_time,
        "-i",
        input_file_path,
        "-to",
        end_time,
        "-r",
        fps,
        "-vf",
        scale,
        output_file_path
    ]
    return command

def run_ffmpeg(command):
    """
        コマンドを受け取り、ffmpegを実行する
    """
    # コマンドの実行
    subprocess.run(command)

#------------------------------------------------------------

def test_compression():
    mock_dict = {
        "input": "testmov.mp4",
        "output": "output.mp4",
        "video codec": "libx264",
        "audio codec": "aac",
        "tune": "fastdecode",
        "preset":"ultrafast",
        "crf": "28",
        "bit rate": "32k",
        "filesize": 5934367,
        "type": "compression"
        
    }
    command = command_generation_compression(mock_dict)
    print(command)
    run_ffmpeg(command)

def test_resolution():
    mock_dict = {
        "input": "nc53235.mp4",
        "output": "output.mp4",
        "width": "1280",
        "height": "720",
        "filesize": 5934367,
        "type": "resolution"
    }
    command = command_generation_resolution(mock_dict)
    print(command)
    run_ffmpeg(command)


def test_convert_mp4_to_mp3():
    input_file_name = "input/nc53235.mp4"
    output_file_name = "output/output.mp3"
    # convert_mp4_to_mp3(input_file_name, output_file_name)

def mock_audio_dict():
    mock_dict = {
        "input": "nc53235.mp4",
        "output": "test_gif.gif",
        "video_size": "300",
        "fps": "10",
        "start_time": "00:00:05",
        "end_time": "10"
    }
    return mock_dict

def mock_gif_dict():
    mock_dict = {
        "input": "testmov.mp4",
        "output": "test_gif.gif",
        "video_size": "300",
        "fps": "10",
        "start_time": "00:00:05",
        "end_time": "10"
    }
    return mock_dict

def test_command_generation_gif_conversion():
    # OK
    mock_dict = mock_gif_dict()
    command_generation_gif_conversion(mock_dict)

def test_gif_convert():
    # OK
    mock_dict = mock_gif_dict()
    command = command_generation_gif_conversion(mock_dict)
    run_ffmpeg(command)


if __name__ == "__main__":
    # test_convert_mp4_to_mp3()
    # test_resolution()
    test_compression()
    pass

