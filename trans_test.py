import openai
import os
import re

# APIキーを設定
# openai.api_key = "

# 分割サイズを設定（ここでは2048文字に設定）
split_size = 2048


def split_text(text, size):
    split_texts = []
    current_chunk = ''
    for sentence in re.split('(?<=[。.?！])', text):
        if len(current_chunk) + len(sentence) <= size:
            current_chunk += sentence
        else:
            split_texts.append(current_chunk)
            current_chunk = sentence
    if current_chunk:
        split_texts.append(current_chunk)
    return split_texts


def summarize(conversation, text, max_tokens=150):
    conversation[1]['content'] = text
    # print(conversation)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    summarized_text = response.choices[0].message['content'].strip()
    conversation[2]['content'] = summarized_text
    return summarized_text


def process_folder(folder_path, initial_prompt, max_tokens):
    input_filename = os.path.join(folder_path, "transcription.txt")
    output_filename = os.path.join(folder_path, "summarized_minutes.txt")

    with open(input_filename, "r", encoding="utf-8") as f:
        text = f.read()

    # テキストを分割
    split_texts = split_text(text, split_size)

    # 分割数を表示
    print(f"議事録を{len(split_texts)}分割しました。")

    # 分割したテキストを要約
    summarized_texts = []
    conversation = [{"role": "system", "content": initial_prompt}, {"role": "user", "content": ""}, {"role": "assistant", "content": ""}]
    for i, part in enumerate(split_texts):
        summarized_part = summarize(conversation, part, max_tokens)
        summarized_texts.append(summarized_part)
        print(f"{i + 1}/{len(split_texts)}分割目が要約されました。")

    # 要約を結合
    summarized_text = "\n".join(summarized_texts)

    # 要約をファイルに書き込む
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(summarized_text)

    with open(output_filename, 'r') as f:
        lines = f.readlines()

    # 改行を削除した行を含むリストを作成
    lines = [line.rstrip('\n') for line in lines]

    # ファイルに書き込みなおします
    with open(output_filename, 'w') as f:
        for line in lines:
            f.write(line)

    print(f"要約が完了しました。出力ファイル名: {output_filename}")


def trans_test(prompt, max_tokens):
    base_folder = "mp3_sounds_split"

    for folder in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder)
        if os.path.isdir(folder_path):
            process_folder(folder_path, prompt, max_tokens)
