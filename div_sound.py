import os
from pydub import AudioSegment

def split_audio(input_path, base_output_folder, split_duration):
    song = AudioSegment.from_mp3(input_path)
    split_duration_ms = split_duration * 60 * 1000
    output_format = "mp3"

    output_base = os.path.splitext(os.path.basename(input_path))[0]
    output_folder = os.path.join(base_output_folder, f"{output_base}_split")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, start_time in enumerate(range(0, len(song), split_duration_ms)):
        end_time = start_time + split_duration_ms
        output_path = os.path.join(output_folder, f"{output_base}_part{i}.{output_format}")
        song[start_time:end_time].export(output_path, format=output_format)
        print(f"分割完了: {input_path} -> {output_path}")

def div_sound():
    input_folder = "sounds"
    output_folder = "mp3_sounds_split"
    split_duration = 20

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".mp3"):
            input_path = os.path.join(input_folder, file)
            split_audio(input_path, output_folder, split_duration)

