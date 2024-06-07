#!/bin/bash

# Define the Python version to install
PYTHON_VERSION="3.11"

# Check if Homebrew is installed
if command -v brew &> /dev/null; then
    echo "Homebrew is installed. Installing packages..."

    # Update Homebrew
    brew update

    # Install Python
    if brew list python@$PYTHON_VERSION &> /dev/null; then
        echo "Python $PYTHON_VERSION is already installed."
    else
        brew install python@$PYTHON_VERSION
    fi

    # Verify Python installation and create virtual environment if it doesn't exist
    if command -v python$PYTHON_VERSION &> /dev/null; then
        echo "Python $PYTHON_VERSION exists."
        if [ ! -d ".venv" ]; then
            # Create virtual environment in .venv
            python$PYTHON_VERSION -m venv .venv
            echo "Virtual environment created in .venv"
        else
            echo "Virtual environment already exists in .venv"
        fi

        # Activate the virtual environment
        source .venv/bin/activate

        # Install dependencies from requirements.txt if it exists
        if [ -f "requirements.txt" ]; then
            pip install -r requirements.txt
            echo "Dependencies installed from requirements.txt"
        else
            echo "requirements.txt not found. No dependencies installed."
        fi

        # Deactivate the virtual environment
        deactivate
    else
        echo "Python $PYTHON_VERSION installation failed."
    fi

    # Install PortAudio
    if brew list portaudio &> /dev/null; then
        echo "PortAudio is already installed."
    else
        brew install portaudio
    fi

    # Install FLAC
    if brew list flac &> /dev/null; then
        echo "FLAC is already installed."
    else
        brew install flac
    fi

    # Install FFmpeg
    if brew list ffmpeg &> /dev/null; then
        echo "FFmpeg is already installed."
    else
        brew install ffmpeg
    fi

    echo "All specified packages are installed."
else
    echo "Homebrew is required. Please install Homebrew first."
fi