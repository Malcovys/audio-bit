import os
import wave
import io
from pydub import AudioSegment

def removeTempFiles(path):
    # Supprime tous les fichiers dans un répertoire donné
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))

tempPath = "./temp"
destinationPath = "C:/Users/malco/Music"

if __name__ == '__main__':
    print("begin conversion...")

    for file in os.listdir(tempPath):
        # Formate le fichier audio en utilisant pydub
        audio = AudioSegment.from_file(os.path.join(tempPath, file))

        # Retire l'extension du fichier audio
        index = file.find(".")
        if index != -1:
            file_name = file[:index]

        # Exporte le fichier audio formaté dans la mémoire
        wav_data = audio.export(format='wav').read()

        try:
            # Crée un fichier wave en mémoire
            with wave.open(io.BytesIO(wav_data), 'rb') as inAudio:
                # Crée le fichier wave de destination
                with wave.open(os.path.join(destinationPath, f"{file_name}.wav"), 'wb') as outAudio:
                    # Copie les paramètres du fichier source
                    outAudio.setnchannels(inAudio.getnchannels())
                    outAudio.setsampwidth(inAudio.getsampwidth())
                    outAudio.setframerate(inAudio.getframerate())
                    outAudio.writeframes(wav_data)

        except Exception as e:
            print(e)

    # Supprime le(s) fichier temporaire
    print("clear temp directory...")
    removeTempFiles(tempPath)

    print("success")
    print("files at " + destinationPath)
