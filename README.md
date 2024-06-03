# Sound2Summary

## library
- openai
- pydub

### how to install
e.g.,

```
pip install pydub
pip install openai
```

if you want to use virtual environment, you can use requirement.txt

(in virtual environment,)

```
python3 -m pip install -r requirement.txt
```

## How to use

### First, put sounds file on sounds directory (mp3 file)
If you have only m4a file and don't have mp3 file, you shold put m4a file on 'm4a_souds' directory and run 'convert_m4a2mp3.py'. (Zoom recoding data may be m4a format data.)
You get result as 'sounds/hoge.mp3'.

### Second, edit run.py

You have to edit api key, and prompt
- apiキーがgitHub上で公開されるのを防ぐため，ignoreされた'key.json'ファイル中にapiキーを記載する方式にしています．'key_template.json'の書き方にしたがって'key.json'ファイルを作成してください．
- （プロンプトは2種類あります。文字起こし用と要約用です。より簡潔に、ただしより状況がわかりやすいようにプロンプトを書けば書くほど文字起こしの精度や、要約の精度があがります。）
- （文字起こし用のプロンプトは動画の言語に合わせてください。）
Finally, run run.py

You get result at sound2summary/mp3_sounds_split/[sounds flile name]/summarized_minutes.txt

# Options

In sound2text, we assumption that conversation is **Japanese

if you want to transcript english sounds, please edit run.py, language option
if you want to customize output length, please edit run.py, max token option

~~If your sounds file is copmposed of other language, you edit sound2text.py, line 19.~~

~~language = "ja",~~


~~Similarly, you want to edit length of summary text, you edit trans_test.py, line 29.~~

~~max_tokens=150,~~
