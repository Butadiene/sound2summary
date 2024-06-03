import openai
from div_sound import div_sound
from sound2text import sound2text
from trans_test import trans_test
import json

#* read json file
with open("key.json", "r") as f:
    params = json.load(f)

# Set your OpenAI API key
openai.api_key = params['api_key']

prompt_for_sound2text = "この音声は地球極域からの大気流失に関する研究のセミナー発表において，冒頭に分野の概要を簡単に紹介するショートトークの内容を録音したものです。大学院の研究室で行われており、多数の参加者がいます。"
prompt_for_summarization = "この文章は、地球極域からの大気流失に関する研究のセミナー発表の冒頭で，分野の概要を簡単に紹介するショートトークの内容をWhisperを用いて文字起こしを行ったものです。ホームページの掲載用に，ショートトークの文字起こしの内容を要約してください。"

div_sound()
sound2text(prompt_for_sound2text, language="ja")  # "ja": Japanease, "en":English
trans_test(prompt_for_summarization, max_tokens=2400)
