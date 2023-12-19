import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load the drum sound (ensure the path is correct and use a WAV file)
drum_sound = pygame.mixer.Sound('/Users/ernesti/Desktop/aixart/public/TR808Clap.mp3')

# Play the sound
drum_sound.play()

# Keep the program running long enough to hear the sound
pygame.time.delay(5000)  # Delay in milliseconds (2000ms = 2 seconds)
