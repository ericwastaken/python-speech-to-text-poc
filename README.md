# Speech to Text POC

This is a proof of concept for an OFFLINE speech to text application using the [Python SpeechRecognition library](https://github.com/Uberi/speech_recognition#readme) and [OpenAI Whisper](https://github.com/openai/whisper). The application is designed to take audio input from any one microphone on your system and convert it to text. The text is then displayed to the user.

This project includes several scripts that demonstrate different techniques and models. The scripts are designed to be run from the command line.

On certain systems, on the first run, you will need to grant microphone access to the application. This is a one-time operation, though it might be necessary after you switch microphones.

On all systems, on the first run, the application will download the necessary language models. This is also a one-time operation, and it does require internet for this first load. After this, the models are cached locally and no internet is needed for performing the transcriptions.

## Python Scripts

- `mic-transcribe-openai-whisper.py` uses the OpenAI Whisper library locally (no internet needed) to transcribe the audio input. Loops until the user stops with CTRL+C.
- `check-torch-and-cuda.py` checks if PyTorch is installed with CUDA support. This is applicable for systems with NVIDIA GPUs where CUDA is supported.

## Requirements

**Mandatory Requirements**

> **Note:** See the list of bootstrap scripts explained below for automated installation of the requirements.

- Python 3.11
  - macOS: `brew install python@3.11`
- Python dependencies in **requirements.txt**.
- Homebrew (macOS) or Chocolatey (Windows) for package management.
- PyAudio
  - macOS: `brew install portaudio`
  - Windows: Only python dependencies.
  - Debian/Ubuntu: `sudo apt-get install python-pyaudio python3-pyaudio`
- Flac Encoder
  - macOS: `brew install flac`
  - Windows: In an admin shell, run `choco install flac` (if not already installed)
  - Debian/Ubuntu: `sudo apt-get install flac` (if not already installed)
- ffmpeg
  - macOS: `brew install ffmpeg`
  - Windows: In an admin shell, run `choco install ffmpeg` (if not already installed)
  - Debian/Ubuntu: `sudo apt-get install ffmpeg` (if not already installed)

**Bootstrap Scripts**

- `bootstrap-macos.sh` for macOS
- TODO: Write a bootstrap script for Windows.

**Optional Requirements**

If running on a supported NVIDIA GPU (not supported in Apple Silicon), the following are also necessary:

- [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
  - CUDA Toolkit also requires [Visual Studio for Windows](https://visualstudio.microsoft.com/) in order to install all components correctly.
- PyTorch needs to use a special version with CUDA support. Install it with the following commands:
  `pip uninstall torch torchvision torchaudio`
  `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`

You can run the test script `check-torch-and-cuda.py` to verify the installation of PyTorch with CUDA support.

## First Time Setup

Assuming you have Python 3.8+ installed, the following steps will get you started:

1. Clone the repository.
2. Install the project requirements above. Use a bootstrap script if available for your system.
3. If on a system with an NVIDIA GPU, install the optional requirements.
4. Activate the Python virtual environment: 
   - macOS/Linux: `source venv/bin/activate` 
   - Windows: `venv\Scripts\activate`
5. With the virtual environment active, install the Python dependencies: `pip install -r requirements.txt`.
6. Run the script of your choice with `python <script_name>.py`.

## Roadmap

- [ ] Add more scripts to demonstrate different models and techniques.
- [ ] Add a script for transcribing audio files passed as arguments.
- [ ] Add a bootstrap script for Windows.
- [ ] Consider implementing [insenely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper) for Apple Silicon GPU support.