import pygame
import numpy as np
import keyboard
from tendo import singleton

me = singleton.SingleInstance()
left_side_keys = 'qwerasdfzxcv'
right_side_keys = "uiopjklm,<.>/?;:'\"[]\{\}"

# Flag to track whether the listener is active
listener_active = True

# Initialize pygame mixer
pygame.mixer.init()

sound_map = {
    # Letters with `press` and `release` values swapped
    'a': {'press': './audios/01-0.wav', 'release': './audios/01-1.wav'},
    'b': {'press': './audios/02-0.wav', 'release': './audios/02-1.wav'},
    'c': {'press': './audios/03-0.wav', 'release': './audios/03-1.wav'},
    'd': {'press': './audios/04-0.wav', 'release': './audios/04-1.wav'},
    'e': {'press': './audios/05-0.wav', 'release': './audios/05-1.wav'},
    'f': {'press': './audios/06-0.wav', 'release': './audios/06-1.wav'},
    'g': {'press': './audios/07-0.wav', 'release': './audios/07-1.wav'},
    'h': {'press': './audios/08-0.wav', 'release': './audios/08-1.wav'},
    'i': {'press': './audios/09-0.wav', 'release': './audios/09-1.wav'},
    'j': {'press': './audios/0a-0.wav', 'release': './audios/0a-1.wav'},
    'k': {'press': './audios/0b-0.wav', 'release': './audios/0b-1.wav'},
    'l': {'press': './audios/0c-0.wav', 'release': './audios/0c-1.wav'},
    'm': {'press': './audios/0d-0.wav', 'release': './audios/0d-1.wav'},
    'n': {'press': './audios/0e-0.wav', 'release': './audios/0e-1.wav'},
    'o': {'press': './audios/0f-0.wav', 'release': './audios/0f-1.wav'},
    'p': {'press': './audios/10-0.wav', 'release': './audios/10-1.wav'},
    'q': {'press': './audios/11-0.wav', 'release': './audios/11-1.wav'},
    'r': {'press': './audios/12-0.wav', 'release': './audios/12-1.wav'},
    's': {'press': './audios/13-0.wav', 'release': './audios/13-1.wav'},
    't': {'press': './audios/14-0.wav', 'release': './audios/14-1.wav'},
    'u': {'press': './audios/15-0.wav', 'release': './audios/15-1.wav'},
    'v': {'press': './audios/16-0.wav', 'release': './audios/16-1.wav'},
    'w': {'press': './audios/17-0.wav', 'release': './audios/17-1.wav'},
    'x': {'press': './audios/18-0.wav', 'release': './audios/18-1.wav'},
    'y': {'press': './audios/19-0.wav', 'release': './audios/19-1.wav'},
    'z': {'press': './audios/1a-0.wav', 'release': './audios/1a-1.wav'},

    # Numbers with `press` and `release` values swapped
    '1': {'press': './audios/21-0.wav', 'release': './audios/21-1.wav'},
    '2': {'press': './audios/22-0.wav', 'release': './audios/22-1.wav'},
    '3': {'press': './audios/23-0.wav', 'release': './audios/23-1.wav'},
    '4': {'press': './audios/24-0.wav', 'release': './audios/24-1.wav'},
    '5': {'press': './audios/25-0.wav', 'release': './audios/25-1.wav'},
    '6': {'press': './audios/26-0.wav', 'release': './audios/26-1.wav'},
    '7': {'press': './audios/27-0.wav', 'release': './audios/27-1.wav'},
    '8': {'press': './audios/28-0.wav', 'release': './audios/28-1.wav'},
    '9': {'press': './audios/29-0.wav', 'release': './audios/29-1.wav'},
    '0': {'press': './audios/20-0.wav', 'release': './audios/20-1.wav'},

    # Special keys with `press` and `release` values swapped
    'space': {'press': './audios/30-0.wav', 'release': './audios/30-1.wav'},
    'enter': {'press': './audios/31-0.wav', 'release': './audios/31-1.wav'},
    'esc': {'press': './audios/32-0.wav', 'release': './audios/32-1.wav'},
    'backspace': {'press': './audios/33-0.wav', 'release': './audios/33-1.wav'},
    'tab': {'press': './audios/34-0.wav', 'release': './audios/34-1.wav'},
    'shift': {'press': './audios/35-0.wav', 'release': './audios/35-1.wav'},
    'ctrl': {'press': './audios/36-0.wav', 'release': './audios/36-1.wav'},
    'alt': {'press': './audios/37-0.wav', 'release': './audios/37-1.wav'},
    'left': {'press': './audios/38-0.wav', 'release': './audios/38-1.wav'},
    'right': {'press': './audios/39-0.wav', 'release': './audios/39-1.wav'},
    'up': {'press': './audios/3a-0.wav', 'release': './audios/3a-1.wav'},
    'down': {'press': './audios/3b-0.wav', 'release': './audios/3b-1.wav'},
    # Add additional key mappings as needed
    '[': {'press': './audios/21-0.wav', 'release': './audios/21-1.wav'},
    '{': {'press': './audios/21-0.wav', 'release': './audios/21-1.wav'},
    ']': {'press': './audios/22-0.wav', 'release': './audios/22-1.wav'},
    '}': {'press': './audios/22-0.wav', 'release': './audios/22-1.wav'},
    ';': {'press': './audios/23-0.wav', 'release': './audios/23-1.wav'},
    ':': {'press': './audios/23-0.wav', 'release': './audios/23-1.wav'},
    "'": {'press': './audios/24-0.wav', 'release': './audios/24-1.wav'},
    '"': {'press': './audios/24-0.wav', 'release': './audios/24-1.wav'},
    ',': {'press': './audios/27-0.wav', 'release': './audios/27-1.wav'},
    '<': {'press': './audios/27-0.wav', 'release': './audios/27-1.wav'},
    '.': {'press': './audios/26-0.wav', 'release': './audios/26-1.wav'},
    '>': {'press': './audios/26-0.wav', 'release': './audios/26-1.wav'},
    '/': {'press': './audios/25-0.wav', 'release': './audios/25-1.wav'},
    '\\': {'press': './audios/25-0.wav', 'release': './audios/25-1.wav'},
    '?': {'press': './audios/25-0.wav', 'release': './audios/25-1.wav'},
    '-': {'press': './audios/28-0.wav', 'release': './audios/28-1.wav'},
    '_': {'press': './audios/28-0.wav', 'release': './audios/28-1.wav'},
    '=': {'press': './audios/29-0.wav', 'release': './audios/29-1.wav'},
    '+': {'press': './audios/29-0.wav', 'release': './audios/29-1.wav'},
    '*': {'press': './audios/20-0.wav', 'release': './audios/20-1.wav'},
}


def split_stereo_to_mono(sound_file):
    """Splits stereo sound into two mono sounds (left and right channels)."""
    stereo_sound = pygame.mixer.Sound(sound_file)
    stereo_array = pygame.sndarray.array(stereo_sound)

    # Create left and right channel arrays
    left_channel = np.zeros_like(stereo_array)
    right_channel = np.zeros_like(stereo_array)
    left_channel[:, 0] = stereo_array[:, 0]  # Left channel
    right_channel[:, 1] = stereo_array[:, 1]  # Right channel

    return pygame.sndarray.make_sound(left_channel), pygame.sndarray.make_sound(right_channel)


def play_sound(sound_file, pan, duration=95):
    left_sound, right_sound = split_stereo_to_mono(sound_file)

    # Adjust the volume according to the pan
    left_sound.set_volume(pan[0])
    right_sound.set_volume(pan[1])

    # Play both sounds simultaneously
    left_sound.play(loops=0, maxtime=duration)
    right_sound.play(loops=0, maxtime=duration)


def on_key_event(event):
    global listener_active
    key = event.name.lower()

    # Check if the event has a corresponding sound in the sound_map
    if keyboard.is_pressed('alt') and event.name == 'm':
        listener_active = not listener_active

    if listener_active:
        if key in sound_map:
            sound_type = 'press' if event.event_type == 'down' else 'release'

            if key in left_side_keys:  # Example for left side keys
                pan = (1.0, 0.5)  # Full left, no right
            elif key in right_side_keys:  # Example for right side keys
                pan = (0.5, 1.0)  # No left, full right
            else:
                pan = (0.5, 0.5)  # Centered

            play_sound(sound_map[key][sound_type], pan)


keyboard.hook(on_key_event)

print("Press keys to play sounds. Press Ctrl + ESC to exit.")
keyboard.wait('ctrl + esc')
pygame.quit()