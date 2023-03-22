import os
import subprocess

def convert_to_mp3(input_file):
    output_file = os.path.splitext(input_file)[0] + ".mp3"
    subprocess.call(["ffmpeg", "-i", input_file, "-codec:a", "libmp3lame", "-b:a", "320k", "-map_metadata", "0", "-id3v2_version", "3", "-write_id3v1", "1", "-metadata:s:v", "title='Album cover'", "-metadata:s:v", "comment='Cover (front)'", output_file])
    os.remove(input_file)

def convert_folder_to_mp3(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".flac"):
                input_file = os.path.join(root, file)
                convert_to_mp3(input_file)

convert_folder_to_mp3("/Users/ghaithnotvertigo/Projects/Code/file-converter/music")