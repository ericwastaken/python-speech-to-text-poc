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


def capture_audio():
    # Check if GPU is available
    using_gpu = check_gpu()

    # Suppress specific warnings if using CPU
    if not using_gpu:
        warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

    # Initialize the recognizer
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  # Adjust based on ambient noise levels
    recognizer.pause_threshold = 0.8  # Time to wait before considering speech has ended

    # Load the Whisper model and move it to the GPU if available
    device = "cuda" if using_gpu else "cpu"
    model = whisper.load_model("base").to(device)

    while True:
        try:
            # Use the microphone as the audio source
            with sr.Microphone() as source:
                print("Please say something:")
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=1)
                # Listen for the first phrase and extract it into audio data
                audio_data = recognizer.listen(source)

            # Save the audio data to a temporary WAV file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav_file:
                temp_wav_file.write(audio_data.get_wav_data())
                temp_wav_file_path = temp_wav_file.name

            # Start timing the transcription process
            start_time = time.time()

            # Transcribe the audio file using Whisper
            result = model.transcribe(temp_wav_file_path)

            # End timing the transcription process
            end_time = time.time()

            # Print the transcribed text
            print("You said:", result["text"])

            # Print the time taken for the transcription
            print(f"Time taken for transcription: {end_time - start_time:.2f} seconds")

            # Remove the temporary file
            os.remove(temp_wav_file_path)

        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Exiting...")
            break


if __name__ == "__main__":

    try:
        capture_audio()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(0)
