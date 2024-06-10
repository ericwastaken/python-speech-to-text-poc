import speech_recognition as sr
import whisper
import warnings
import time
import torch
import sys
import tempfile
import os


def check_gpu():
    if torch.cuda.is_available():
        print("Compatible GPU detected. Using GPU for transcription.")
        return True
    else:
        print("No compatible GPU detected. Using CPU for transcription.")
        return False

def list_microphones():
    print("Available microphones:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}: {name}")

def capture_audio(mic_index):
    # Check if GPU is available
    using_gpu = check_gpu()

    # Suppress specific warnings if using CPU
    if not using_gpu:
        warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

    # Initialize the recognizer
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  # Adjust based on ambient noise levels
    recognizer.dynamic_energy_threshold = True # Adjust energy threshold dynamically
    recognizer.pause_threshold = 0.6  # Time to wait before considering speech has ended

    # Whisper model name
    model_name = "base"  # model can be any of tiny, base, small, medium, large, tiny.en, base.en, small.en, medium.en. See https://github.com/openai/whisper for more details.

    # Load the Whisper model and move it to the GPU if available
    device = "cuda" if using_gpu else "cpu"
    model = whisper.load_model("base").to(device)

    while True:
        try:
            # Use the microphone as the audio source
            with sr.Microphone(device_index=mic_index) as source:
                print("Please say something:")
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=1)
                # Listen for the first phrase and extract it into audio data
                audio_data = recognizer.listen(source)

            # Start timing the transcription process
            start_time = time.time()

            # Transcribe the audio using Whisper
            result = recognizer.recognize_whisper(audio_data, model=model_name)


            # End timing the transcription process
            end_time = time.time()

            # Print the transcribed text
            print("You said:", result)

            # Print the time taken for the transcription
            print(f"Time taken for transcription: {end_time - start_time:.2f} seconds")

        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Whisper; {e}")

        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Exiting...")
            break

if __name__ == "__main__":
    list_microphones()
    mic_index = int(input("Select the microphone index you want to use: "))
    try:
        capture_audio(mic_index)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(0)
