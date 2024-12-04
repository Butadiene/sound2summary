from openai import OpenAI
from div_sound import div_sound
from sound2text import sound2text
from trans_test import trans_test
import json

# read json file
with open("params.json", "r") as f:
    params = json.load(f)

# Set your OpenAI API key
client = OpenAI(api_key=params['api_key'],)

# Set the prompt for sound2text and summarization
prompt_for_sound2text = params['prompt_for_soutnd2text']
prompt_for_summarization = params['prompt_for_summarization']

div_sound()
sound2text(client,prompt_for_sound2text, language="ja")  # "ja": Japanease, "en":English
trans_test(client,prompt_for_summarization, max_tokens=2400)
