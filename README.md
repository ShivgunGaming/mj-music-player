# 🎵 Michael Jackson Songs Player 🕺

This Python program allows you to play some of the best songs by Michael Jackson using pygame.

## Prerequisites

1. Python installed on your system.
2. pygame library installed. You can install it using pip:
    ```
    pip install pygame
    ```

## How to Use

1. Run the program.
2. You'll be presented with a list of Michael Jackson songs available in the program.
3. Enter the name of the song you want to play.
4. The program will play the selected song.

## Program Structure

- `import os`: Used for file operations.
- `import pygame`: Used for playing audio files.
- `pygame.init()`: Initializes the pygame module.
- `play_audio(audio_file)`: Function to play the audio.
- `michael_jackson_songs`: Dictionary containing Michael Jackson songs with their file paths.
- The program lists the available songs and prompts the user to choose one.
- If the chosen song exists, it checks if the corresponding audio file exists, then plays the song.

## Adding More Songs

- To add more songs, simply add them to the `michael_jackson_songs` dictionary with their file paths.
- Ensure the audio files are in the correct format and placed in the same directory as the program.

## Notes

- Ensure that your system's audio output is functional and the volume is adjusted appropriately.
