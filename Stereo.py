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
    'esc': {'press': './audios/01-0.wav', 'release': './audios/01-1.wav'},
    '1': {'press': './audios/02-0.wav', 'release': './audios/02-1.wav'},
    '2': {'press': './audios/03-0.wav', 'release': './audios/03-1.wav'},
    '3': {'press': './audios/04-0.wav', 'release': './audios/04-1.wav'},
    '4': {'press': './audios/05-0.wav', 'release': './audios/05-1.wav'},
    '5': {'press': './audios/06-0.wav', 'release': './audios/06-1.wav'},
    '6': {'press': './audios/07-0.wav', 'release': './audios/07-1.wav'},
    '7': {'press': './audios/08-0.wav', 'release': './audios/08-1.wav'},
    '8': {'press': './audios/09-0.wav', 'release': './audios/09-1.wav'},
    '9': {'press': './audios/0a-0.wav', 'release': './audios/0a-1.wav'},
    '0': {'press': './audios/0b-0.wav', 'release': './audios/0b-1.wav'},
    '-': {'press': './audios/0c-0.wav', 'release': './audios/0c-1.wav'},
    '=': {'press': './audios/0d-0.wav', 'release': './audios/0d-1.wav'},
    'backspace': {'press': './audios/0e-0.wav', 'release': './audios/0e-1.wav'},
    'tab': {'press': './audios/0f-0.wav', 'release': './audios/0f-1.wav'},
    'q': {'press': './audios/10-0.wav', 'release': './audios/10-1.wav'},
    'w': {'press': './audios/11-0.wav', 'release': './audios/11-1.wav'},
    'e': {'press': './audios/12-0.wav', 'release': './audios/12-1.wav'},
    'r': {'press': './audios/13-0.wav', 'release': './audios/13-1.wav'},
    't': {'press': './audios/14-0.wav', 'release': './audios/14-1.wav'},
    'y': {'press': './audios/15-0.wav', 'release': './audios/15-1.wav'},
    'u': {'press': './audios/16-0.wav', 'release': './audios/16-1.wav'},
    'i': {'press': './audios/17-0.wav', 'release': './audios/17-1.wav'},
    'o': {'press': './audios/18-0.wav', 'release': './audios/18-1.wav'},
    'p': {'press': './audios/19-0.wav', 'release': './audios/19-1.wav'},
    '[': {'press': './audios/1a-0.wav', 'release': './audios/1a-1.wav'},
    ']': {'press': './audios/1b-0.wav', 'release': './audios/1b-1.wav'},
    'enter': {'press': './audios/1c-0.wav', 'release': './audios/1c-1.wav'},
    'left_ctrl': {'press': './audios/1d-0.wav', 'release': './audios/1d-1.wav'},
    'a': {'press': './audios/1e-0.wav', 'release': './audios/1e-1.wav'},
    's': {'press': './audios/1f-0.wav', 'release': './audios/1f-1.wav'},
    'd': {'press': './audios/20-0.wav', 'release': './audios/20-1.wav'},
    'f': {'press': './audios/21-0.wav', 'release': './audios/21-1.wav'},
    'g': {'press': './audios/22-0.wav', 'release': './audios/22-1.wav'},
    'h': {'press': './audios/23-0.wav', 'release': './audios/23-1.wav'},
    'j': {'press': './audios/24-0.wav', 'release': './audios/24-1.wav'},
    'k': {'press': './audios/25-0.wav', 'release': './audios/25-1.wav'},
    'l': {'press': './audios/26-0.wav', 'release': './audios/26-1.wav'},
    ';': {'press': './audios/27-0.wav', 'release': './audios/27-1.wav'},
    "'": {'press': './audios/28-0.wav', 'release': './audios/28-1.wav'},
    '`': {'press': './audios/29-0.wav', 'release': './audios/29-1.wav'},
    'left_shift': {'press': './audios/2a-0.wav', 'release': './audios/2a-1.wav'},
    '\\': {'press': './audios/2b-0.wav', 'release': './audios/2b-1.wav'},
    'z': {'press': './audios/2c-0.wav', 'release': './audios/2c-1.wav'},
    'x': {'press': './audios/2d-0.wav', 'release': './audios/2d-1.wav'},
    'c': {'press': './audios/2e-0.wav', 'release': './audios/2e-1.wav'},
    'v': {'press': './audios/2f-0.wav', 'release': './audios/2f-1.wav'},
    'b': {'press': './audios/30-0.wav', 'release': './audios/30-1.wav'},
    'n': {'press': './audios/31-0.wav', 'release': './audios/31-1.wav'},
    'm': {'press': './audios/32-0.wav', 'release': './audios/32-1.wav'},
    ',': {'press': './audios/33-0.wav', 'release': './audios/33-1.wav'},
    '.': {'press': './audios/34-0.wav', 'release': './audios/34-1.wav'},
    '/': {'press': './audios/35-0.wav', 'release': './audios/35-1.wav'},
    'right_shift': {'press': './audios/36-0.wav', 'release': './audios/36-1.wav'},
    'keypad_*': {'press': './audios/37-0.wav', 'release': './audios/37-1.wav'},
    'left_alt': {'press': './audios/38-0.wav', 'release': './audios/38-1.wav'},
    'space': {'press': './audios/39-0.wav', 'release': './audios/39-1.wav'},
    'caps_lock': {'press': './audios/3a-0.wav', 'release': './audios/3a-1.wav'},
    'f1': {'press': './audios/3b-0.wav', 'release': './audios/3b-1.wav'},
    'f2': {'press': './audios/3c-0.wav', 'release': './audios/3c-1.wav'},
    'f3': {'press': './audios/3d-0.wav', 'release': './audios/3d-1.wav'},
    'f4': {'press': './audios/3e-0.wav', 'release': './audios/3e-1.wav'},
    'f5': {'press': './audios/3f-0.wav', 'release': './audios/3f-1.wav'},
    'f6': {'press': './audios/40-0.wav', 'release': './audios/40-1.wav'},
    'f7': {'press': './audios/41-0.wav', 'release': './audios/41-1.wav'},
    'f8': {'press': './audios/42-0.wav', 'release': './audios/42-1.wav'},
    'f9': {'press': './audios/43-0.wav', 'release': './audios/43-1.wav'},
    'f10': {'press': './audios/44-0.wav', 'release': './audios/44-1.wav'},
    'num_lock': {'press': './audios/45-0.wav', 'release': './audios/45-1.wav'},
    'scroll_lock': {'press': './audios/46-0.wav', 'release': './audios/46-1.wav'},
    'keypad_7': {'press': './audios/47-0.wav', 'release': './audios/47-1.wav'},
    'keypad_8': {'press': './audios/48-0.wav', 'release': './audios/48-1.wav'},
    'keypad_9': {'press': './audios/49-0.wav', 'release': './audios/49-1.wav'},
    'keypad_-': {'press': './audios/4a-0.wav', 'release': './audios/4a-1.wav'},
    'left_arrow': {'press': './audios/4b-0.wav', 'release': './audios/4b-1.wav'},
    'keypad_5': {'press': './audios/4c-0.wav', 'release': './audios/4c-1.wav'},
    'right_arrow': {'press': './audios/4d-0.wav', 'release': './audios/4d-1.wav'},
    'keypad_+': {'press': './audios/4e-0.wav', 'release': './audios/4e-1.wav'},
    'end': {'press': './audios/4f-0.wav', 'release': './audios/4f-1.wav'},
    'down_arrow': {'press': './audios/50-0.wav', 'release': './audios/50-1.wav'},
    'page_down': {'press': './audios/51-0.wav', 'release': './audios/51-1.wav'},
    'insert': {'press': './audios/52-0.wav', 'release': './audios/52-1.wav'},
    'delete': {'press': './audios/53-0.wav', 'release': './audios/53-1.wav'},
    'non_us_<': {'press': './audios/56-0.wav', 'release': './audios/56-1.wav'},
    'f11': {'press': './audios/57-0.wav', 'release': './audios/57-1.wav'},
    'f12': {'press': './audios/58-0.wav', 'release': './audios/58-1.wav'},

    '+': {'press': './audios/62-0.wav', 'release': './audios/62-1.wav'},
    'left windows': {'press': './audios/5b-0.wav', 'release': './audios/5b-1.wav'},
    'right windows': {'press': './audios/5b-1.wav', 'release': './audios/5b-1.wav'},
    'right alt': {'press': './audios/61-0.wav', 'release': './audios/61-1.wav'},
    'alt': {'press': './audios/61-0.wav', 'release': './audios/61-1.wav'},
    'menu': {'press': './audios/63-0.wav', 'release': './audios/63-1.wav'},
    'shift': {'press': './audios/64-0.wav', 'release': './audios/64-1.wav'},
    'right shift': {'press': './audios/64-0.wav', 'release': './audios/64-1.wav'},
    '*': {'press': './audios/66-0.wav', 'release': './audios/66-1.wav'},
    'right ctrl': {'press': './audios/67-0.wav', 'release': './audios/67-1.wav'},
    'ctrl': {'press': './audios/67-0.wav', 'release': './audios/67-1.wav'},
    'decimal': {'press': './audios/68-0.wav', 'release': './audios/68-1.wav'},
    'caps lock': {'press': './audios/69-0.wav', 'release': './audios/69-1.wav'},

    'up': {'press': './audios/6a-0.wav', 'release': './audios/6a-1.wav'},
    'down': {'press': './audios/6b-0.wav', 'release': './audios/6b-1.wav'},
    'right': {'press': './audios/6c-0.wav', 'release': './audios/6c-1.wav'},
    'left': {'press': './audios/6d-0.wav', 'release': './audios/6d-1.wav'},

    'num lock': {'press': './audios/6e-0.wav', 'release': './audios/6e-1.wav'},
    'print screen': {'press': './audios/6f-0.wav', 'release': './audios/6f-1.wav'},
    'unknown_7d': {'press': './audios/7d-0.wav', 'release': './audios/7d-1.wav'},

    'unknown_ff': {'press': './audios/ff-0.wav', 'release': './audios/ff-1.wav'},

    'pause': {'press': './audios/77-0.wav', 'release': None}
}

pressed_keys = set()  # Tracks currently pressed keys


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

    if keyboard.is_pressed('alt') and key == 'm':  # a little tricky :)
        listener_active = not listener_active

    # Prevent repeated actions for held keys
    if event.event_type == 'down':
        if key in pressed_keys:
            return  # Ignore repeated press
        pressed_keys.add(key)
    elif event.event_type == 'up':
        pressed_keys.discard(key)

    if listener_active:
        # Check if the event has a corresponding sound in the sound_map
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
