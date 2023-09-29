import subprocess

OUTPUT_DIRECTORY = "tmp"

def convert_mp4_to_mp3(input_file_name, output_file_name):
    """
        mp4をmp3に変換するメソッド
    """
    # command
    # ffmpeg -i input_file_name -vn output_file_name
    command = [
        "ffmpeg",
        "-i",
        input_file_name,
        "-vn",
        output_file_name
    ]

    # コマンドの実行
    subprocess.run(command)


def test_convert_mp4_to_mp3():
    input_file_name = "input/nc53235.mp4"
    output_file_name = "output/output.mp3"
    convert_mp4_to_mp3(input_file_name, output_file_name)

if __name__ == "__main__":
    test_convert_mp4_to_mp3()
