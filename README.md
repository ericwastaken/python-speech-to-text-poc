# Speech to Text POC

This is a proof of concept for a speech to text application using the Python SpeechRecognition library. The application is designed to take audio input from the microphone and convert it to text. The text is then displayed to the user in real-time.

This project includes several scripts that demonstrate different techniques and models. The scripts are designed to be run from the command line.

On certain systems, on the first run, you will need to grant microphone access to the application. This is a one-time operation.

On all systems, on first run, the application will download the necessary language models. This is also a one-time operation and it does require internet for this first load. After this, the models are cached locally and no internet is needed for performing the transcriptions.

## Scripts

- `mic-transcript-openai-whisper.py` uses the OpenAI Whisper library locally (no internet needed) to transcribe the audio input. Loops until the user stops with CTRL+C.

## Requirements

**Mandatory Requirements**

> **Note:** See the list of bootstrap scripts explained below for automated installation of the requirements.

- Python 3.11
  macOS: `brew install python@3.11`
- Python dependencies in **requirements.txt**.
- Homebrew (macOS) or Chocolatey (Windows) for package management.
- PyAudio
  macOS: `brew install portaudio`
  Windows: Only python dependencies.
  Debian/Ubuntu: `sudo apt-get install python-pyaudio python3-pyaudio`
- Flac Encoder
  macOS: `brew install flac`
  Windows: `choco install flac` (if not already installed)
  Debian/Ubuntu: `sudo apt-get install flac` (if not already installed)
- ffmpeg
  macOS: `brew install ffmpeg`
  Windows: `choco install ffmpeg` (if not already installed)
  Debian/Ubuntu: `sudo apt-get install ffmpeg` (if not already installed)

**Bootstrap Scripts**
- `bootstrap-macos.sh` for macOS
- TODO: Write a bootstrap script for Windows.

**Optional Requirements**

If running on a supported NVIDIA GPU (not supported in Apple Silicon), the following are also necessary:

- [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
- `pip install torch torchvision torchaudio`

## First Time Setup

Assuming you have Python 3.8+ installed, the following steps will get you started:

1. Clone the repository.
2. Install the project requirements above. Use a bootstrap script if available for your system.
3. If on a system with an NVIDIA GPU, install the optional requirements as well.
4. Activate the Python virtual environment: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows).
5. Install the Python dependencies: `pip install -r requirements.txt`.
6. Run the script of your choice with `python <script_name>.py`.

