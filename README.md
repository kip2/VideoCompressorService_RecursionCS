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

config.jsonにサーバのアドレスとポート番号が設定してあります。

#### 変更方法

server、client、それぞれで config.py を実行して、指示に従って変更してください

```shell
python config.py

# 環境によってはこちら
python3 config.py
```

---

### 事前準備

変換にffmpegを使用しています。
ffmpegをインストールしてください。

#### Linux

##### Ubuntu

```shell
sudo apt update
sudo apt install ffmpeg
```

#### macOS

```shell
brew install ffmpeg
```

#### Windows

1. 公式サイトのダウンロードセクションにアクセスして、Windows版のffmpegをダウンロードします。
2. ダウンロードしたZIPを適当な場所に展開します。
3. 展開したffmpeg.exeのパスをシステムのPATH環境変数に追加します。

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

4. 対話形式で質問されるので、ファイルをどのように変換するかを答えてください。

5. 変換が行われ、outputディレクトリに変換後の保存されます。

変換後、クライアントは終了しますが、サーバは待機状態です。
終了する場合はCtrl + cで終了してください。
