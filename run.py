import openai
from div_sound import div_sound
from sound2text import sound2text
from trans_test import trans_test

openai.api_key = "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"

prompt_for_sound2text = "この音声はプラズマ物理学についての教科書を輪読している際のものです。大学院の研究室で行われており、多数の参加者がいます。"
prompt_for_summarization = "この文章は、プラズマ物理学についての講義をWhisperを用いて文字起こしを行ったものです。講義の内容を要約してください。"

div_sound()
sound2text(prompt_for_sound2text)
trans_test(prompt_for_summarization)