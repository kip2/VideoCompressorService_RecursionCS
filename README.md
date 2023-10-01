# VideoCompressorService_RecursionCS

# 概要

clientからmp4ファイルをserverに渡し、変換するプログラムです。

以下の4種類の変換に対応しています。

1. 動画の圧縮
2. 動画の解像度の変更
3. mp4からmp3ファイルへの変更(音声が入った動画のみ)
4. 切り出し時間を指定してgif形式へ変換する

# 使い方

## 準備

### serverアドレス

ハードコードしています。

client/lib/_address_config.py
server/lib/_address_config.py

の両方を編集してください。

### 事前準備

変換にffmpegを使用しています。
ffmpegをインストールしてください。

#### Linux

##### Ubuntu/Debian

```shell
sudo apt update
sudo apt install ffmpeg
```

##### Fedora

```shell
sudo dnf install ffmpeg
```

##### CentOS/RHEL

```shell
sudo yum install epel-release
sudo yum install ffmpeg
```

##### Arch Linux

```shell
sudo pacman -S ffmpeg
```

#### macOS

```shell
brew install ffmpeg
```

#### Windows

1. 公式サイトのダウンロードセクションにアクセスして、Windows版のffmpegをダウンロードします。
2. ダウンロードしたZIPを適当な場所に展開します。
3. 展開したffmpeg.exeのパスをシステムのPATH環境変数に追加します。

##### Chocolatey

```shell
choco install ffmpeg
```

--- 

以下、serverとclientでそれぞれのシェルを立ち上げて作業してください。

## server

1. serverディレクトリをそのまま、server側に設置してください。

2.server.pyを起動してください。

```shell
$ python server.py

# 環境によってはこちら
$ python3 server.py
```

3. server側の準備はこれでOKです。

## client

1. clientディレクトリを設置してください。

2. 変換したいファイルを、inputディレクトリに入れてください
   注意：2GBまでのファイルにしか対応していません。

3. client.pyを起動してください。

```shell
$ python client.py

# 環境によってはこちら
$ python3 client.py
```

4. ファイルの変換、必要なオプションを聞かれるので、質問に答えてください。

5. 変換が行われ、変換後のファイルがoutputディレクトリに入っています。

変換後、クライアントは終了しますが、サーバは待機状態です。
終了する場合はCtrl + cで終了してください。
