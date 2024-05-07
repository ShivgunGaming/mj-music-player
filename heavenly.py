import os
import pygame

# Initialize pygame
pygame.init()

# Function to play the audio
def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

# Dictionary of Michael Jackson songs with their file paths
michael_jackson_songs = {
    "Who is it": "who-is-it.mp3",
    "Remember the time": "remember-the-time.mp3",
    "Baby be mine": "baby-be-mine.mp3",
    # Add more songs as needed
}

# List the songs
print("Some of the best Michael Jackson songs:")
for song in michael_jackson_songs:
    print("-", song)

# Prompt the user to choose a song
chosen_song = input("Enter the name of the song you want to play: ")

# Check if the chosen song exists in the dictionary
if chosen_song in michael_jackson_songs:
    audio_file = michael_jackson_songs[chosen_song]
    if os.path.exists(audio_file):
        play_audio(audio_file)
        # Wait for the song to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print("File not found.")
else:
    print("Song not found.")
