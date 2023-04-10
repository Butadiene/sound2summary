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

## how to use

First, put sounds file on sounds directory (mp3 file)

Second, edit run.py

you have to edit api key, and prompt
（プロンプトは2種類あります。文字起こし用と要約用です。より簡潔に、ただしより状況がわかりやすいようにプロンプトを書けば書くほど文字起こしの精度や、要約の精度があがります。）
（文字起こし用のプロンプトは動画の言語に合わせてください。）
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
