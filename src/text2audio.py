import os

import pyttsx3
from flask_ml.flask_ml_server.models import FileInput
from pydub import AudioSegment


class Text2AudioModel:

    # Convert text files into audio files and save in Output folder
    def convert_text_to_audio(self, file_path):

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set properties for the voice
        voices = engine.getProperty("voices")
        num_voices = len(voices)
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 130)

        # parse the given file and separate each line of conversation
        conversations = []
        persons = {}
        unique_persons = 0
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            # Split each line by the colon to separate the name and the conversation
            if ":" in line:
                individual, convo = line.split(":", 1)
                conversations.append((convo, individual))
                if individual not in persons:
                    persons[individual] = unique_persons
                    unique_persons += 1

        # Create an empty wav file
        temp_wav_file = "temp_audio.wav"
        engine.save_to_file("", temp_wav_file)
        engine.runAndWait()
        combined_sound = AudioSegment.from_wav(temp_wav_file)

        # Iterate through all texts, create audio with unique voice and append each one to the combined sound
        for i in range(0, len(conversations)):
            text = conversations[i][0]
            index = (persons[conversations[i][1]]) % num_voices
            engine.setProperty("voice", voices[index].id)
            engine.save_to_file(text, temp_wav_file)
            engine.runAndWait()
            new_sound = AudioSegment.from_wav(temp_wav_file)
            combined_sound += new_sound

        # Create Output Directory if not exists and output file path
        os.makedirs("../Outputs", exist_ok=True)
        print(str(os.path.splitext(os.path.basename(file_path))[0]))
        output_file_path = (
            "../Outputs/" + str(os.path.splitext(os.path.basename(file_path))[0]) + ".mp3"
        )

        # Export the combined sound to MP3
        combined_sound.export(output_file_path, format="mp3")
        os.remove(temp_wav_file)

        return output_file_path

    # Get list of files and returns list of audio files
    def convert(self, data: list[FileInput]):
        results = []
        for dp in data:
            result = self.convert_text_to_audio(dp.file_path)
            temp = {"file_path": dp.file_path, "result": result}
            results.append(temp)
        return results
