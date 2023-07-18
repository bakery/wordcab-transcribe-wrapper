import json
import os
import subprocess

SOURCE = "./audio"
DESTINATION = "./transcriptions"

def file_exists(file_path):
    return os.path.exists(file_path)

def load_and_parse_json(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        return json_data

def curl(url, file_path):
    output = subprocess.check_output(['curl', '-F', 'alignment=true', '-F', 'diarization=true', '-F', 'dual_channel=false', '-F', 'source_lang=en', '-F', 'timestamps=s', '-F', 'word_timestamps=true', '-F', f"file=@{file_path}", url])
    return output.decode("utf-8")

def transcribe(source, destination, api_server_url=os.environ['WORDCAB_TRANSCRIBE_SERVER']):
  d = curl(f"{api_server_url}/api/v1/audio", source)
  with open(destination, "w", encoding="utf-8") as f:
      f.write(d)

def find_audio_files(directory, extensions=['.mp3', '.wav']):
    for root, dir, files in os.walk(directory):
        for file in files:
            root, extension = os.path.splitext(file)
            if extension in extensions:
                yield os.path.join(directory, file) 
def main():
    for audio_file in find_audio_files(SOURCE):
        audio_file_name_without_extension = os.path.splitext(os.path.basename(audio_file))[0]
        source = audio_file
        destination = f"{DESTINATION}/{audio_file_name_without_extension}.json"

        if file_exists(destination):
            print(f"transcription already exists for {audio_file}, skipping")
            continue

        print(f"gonna transcribe {source} => {destination}")

        transcribe(source, destination)

    print("🎉 [DONE]")

if __name__ == '__main__':
    main()
