import os
from pydub import AudioSegment

def convert_m4a_to_mp3(input_path, output_path):
    audio = AudioSegment.from_file(input_path, format="m4a")
    audio.export(output_path, format="mp3")

def main():
    input_folder = "./m4a_sounds"
    output_folder = "./sounds"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".m4a"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".m4a", ".mp3"))
            convert_m4a_to_mp3(input_path, output_path)
            print(f"変換完了: {input_path} -> {output_path}")

if __name__ == "__main__":
    main()
