import ctypes
import pygame
import keyboard
import threading

# Initialize pygame mixer
ctypes.windll.user32.ShowWindow(
    ctypes.windll.kernel32.GetConsoleWindow(), 0)  # hide
pygame.mixer.init()

sound_map = {
    # Letters mapped to files ending with `1` (key press) and `0` (key release)
    'a': {'press': './audios/01-1.wav', 'release': './audios/01-0.wav'},
    'b': {'press': './audios/02-1.wav', 'release': './audios/02-0.wav'},
    'c': {'press': './audios/03-1.wav', 'release': './audios/03-0.wav'},
    'd': {'press': './audios/04-1.wav', 'release': './audios/04-0.wav'},
    'e': {'press': './audios/05-1.wav', 'release': './audios/05-0.wav'},
    'f': {'press': './audios/06-1.wav', 'release': './audios/06-0.wav'},
    'g': {'press': './audios/07-1.wav', 'release': './audios/07-0.wav'},
    'h': {'press': './audios/08-1.wav', 'release': './audios/08-0.wav'},
    'i': {'press': './audios/09-1.wav', 'release': './audios/09-0.wav'},
    'j': {'press': './audios/0a-1.wav', 'release': './audios/0a-0.wav'},
    'k': {'press': './audios/0b-1.wav', 'release': './audios/0b-0.wav'},
    'l': {'press': './audios/0c-1.wav', 'release': './audios/0c-0.wav'},
    'm': {'press': './audios/0d-1.wav', 'release': './audios/0d-0.wav'},
    'n': {'press': './audios/0e-1.wav', 'release': './audios/0e-0.wav'},
    'o': {'press': './audios/0f-1.wav', 'release': './audios/0f-0.wav'},
    'p': {'press': './audios/10-1.wav', 'release': './audios/10-0.wav'},
    'q': {'press': './audios/11-1.wav', 'release': './audios/11-0.wav'},
    'r': {'press': './audios/12-1.wav', 'release': './audios/12-0.wav'},
    's': {'press': './audios/13-1.wav', 'release': './audios/13-0.wav'},
    't': {'press': './audios/14-1.wav', 'release': './audios/14-0.wav'},
    'u': {'press': './audios/15-1.wav', 'release': './audios/15-0.wav'},
    'v': {'press': './audios/16-1.wav', 'release': './audios/16-0.wav'},
    'w': {'press': './audios/17-1.wav', 'release': './audios/17-0.wav'},
    'x': {'press': './audios/18-1.wav', 'release': './audios/18-0.wav'},
    'y': {'press': './audios/19-1.wav', 'release': './audios/19-0.wav'},
    'z': {'press': './audios/1a-1.wav', 'release': './audios/1a-0.wav'},

    # Numbers mapped to files ending with `1` (key press) and `0` (key release)
    '1': {'press': './audios/21-1.wav', 'release': './audios/21-0.wav'},
    '2': {'press': './audios/22-1.wav', 'release': './audios/22-0.wav'},
    '3': {'press': './audios/23-1.wav', 'release': './audios/23-0.wav'},
    '4': {'press': './audios/24-1.wav', 'release': './audios/24-0.wav'},
    '5': {'press': './audios/25-1.wav', 'release': './audios/25-0.wav'},
    '6': {'press': './audios/26-1.wav', 'release': './audios/26-0.wav'},
    '7': {'press': './audios/27-1.wav', 'release': './audios/27-0.wav'},
    '8': {'press': './audios/28-1.wav', 'release': './audios/28-0.wav'},
    '9': {'press': './audios/29-1.wav', 'release': './audios/29-0.wav'},
    '0': {'press': './audios/20-1.wav', 'release': './audios/20-0.wav'},

    # Special keys mapped to files ending with `1` (key press) and `0` (key release)
    'space': {'press': './audios/30-1.wav', 'release': './audios/30-0.wav'},
    'enter': {'press': './audios/31-1.wav', 'release': './audios/31-0.wav'},
    'esc': {'press': './audios/32-1.wav', 'release': './audios/32-0.wav'},
    'backspace': {'press': './audios/33-1.wav', 'release': './audios/33-0.wav'},
    'tab': {'press': './audios/34-1.wav', 'release': './audios/34-0.wav'},
    'shift': {'press': './audios/35-1.wav', 'release': './audios/35-0.wav'},
    'ctrl': {'press': './audios/36-1.wav', 'release': './audios/36-0.wav'},
    'alt': {'press': './audios/37-1.wav', 'release': './audios/37-0.wav'},
    'left': {'press': './audios/38-1.wav', 'release': './audios/38-0.wav'},
    'right': {'press': './audios/39-1.wav', 'release': './audios/39-0.wav'},
    'up': {'press': './audios/3a-1.wav', 'release': './audios/3a-0.wav'},
    'down': {'press': './audios/3b-1.wav', 'release': './audios/3b-0.wav'},
    # Add additional key mappings as needed
}


def play_sound(sound_file, pan, duration=95):
    # Load the sound
    sound = pygame.mixer.Sound(sound_file)

    # Create two mono sound instances
    left_channel = pygame.mixer.Sound(sound_file)
    right_channel = pygame.mixer.Sound(sound_file)

    # Adjust the volumes for left and right channels
    left_channel.set_volume(pan[0])
    right_channel.set_volume(pan[1])

    # Play the sound on separate channels
    left_channel.play(loops=0, maxtime=duration)
    right_channel.play(loops=0, maxtime=duration)

    # Stop the sound after the specified duration
    threading.Timer(duration / 1000.0, stop_sound,
                    [left_channel, right_channel]).start()


def stop_sound(left_channel, right_channel):
    left_channel.stop()
    right_channel.stop()


def on_key_event(event):
    # Normalize key names to lowercase
    key = event.name.lower()

    # Check if the event has a corresponding sound in the sound_map
    if key in sound_map:
        # Determine if it's a key press or key release
        sound_type = 'press' if event.event_type == 'down' else 'release'

        # Determine pan based on key position
        if key in 'asdfghjkl':  # Example for left side keys
            pan = (1.0, 0.5)  # Full left, half right
        elif key in 'qwertyuiop':  # Example for right side keys
            pan = (0.5, 1.0)  # Half left, full right
        else:
            pan = (0.5, 0.5)  # Centered

        play_sound(sound_map[key][sound_type], pan)


# Set up a hook to capture keyboard events
keyboard.hook(on_key_event)

# Keep the script running
print("Press keys to play sounds. Press ESC to exit.")
keyboard.wait('ctrl + esc')
pygame.quit()
