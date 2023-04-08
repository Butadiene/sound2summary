import os
import openai
from pydub import AudioSegment

# APIキーを設定
# openai.api_key = ""

def transcribe_audio(input_path, initial_prompt=None):
    # 音声ファイルを変換
    audio = AudioSegment.from_file(input_path, format="mp3")
    audio = audio.set_channels(1).set_frame_rate(16000)  # モノラル、16000Hzに変換
    audio.export("temp.mp3", format="mp3")

    # 音声ファイルをアップロード
    with open("temp.mp3", "rb") as f:
        transcript_data = openai.Audio.transcribe(
            file=f,
            model="whisper-1",
            language = "ja",
            prompt = initial_prompt
        )

    return transcript_data["text"]

def process_folder(folder_path, initial_prompt):
    output_file_path = os.path.join(folder_path, "transcription.txt")

    with open(output_file_path, "w") as output_file:
        for i, file in enumerate(sorted(os.listdir(folder_path))):
            if file.endswith(".mp3"):
                input_path = os.path.join(folder_path, file)

                if i == 0:
                    current_prompt = initial_prompt
                else:
                    with open(output_file_path, "r") as f:
                        lines = f.readlines()
                        current_prompt = "".join(lines[-3:])  # 最後の3行をプロンプトとして使用

                transcription = transcribe_audio(input_path, current_prompt)
                output_file.write(transcription)
                print(f"文字起こし完了: {input_path}")

def sound2text(prompt):
    base_folder = "mp3_sounds_split"
    initial_prompt = prompt
    
    for folder in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder)
        if os.path.isdir(folder_path):
            process_folder(folder_path, initial_prompt)
