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

prompt_for_sound2text = "この音声はプラズマ物理学という分野についての授業を録音したものです。大学院の研究室で行われており、多数の参加者がいます。"
prompt_for_summarization = "この文章は、プラズマ物理学という分野についての授業をWhisperを用いて文字起こしを行ったものです。講義の内容を要約してください。"

div_sound()
sound2text(prompt_for_sound2text, language="ja")  # "ja": Japanease, "en":English
trans_test(prompt_for_summarization, max_tokens=300)
