# from google.cloud import speech
#
import speech_recognition as sr

#for whisper
import numpy
import soundfile
import torch



def analyzeAudio(path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Open the audio file
    with sr.AudioFile(path) as source:
        # Record the audio data
        audio_data = recognizer.record(source)

        try:
            # Recognize the speech
            text = recognizer.recognize_google(audio_data, language="he-IL")   #Works good
            print("Recognized speech: ", text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from service; {e}")
    return text
