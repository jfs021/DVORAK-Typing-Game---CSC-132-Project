#####################################################################
# author: Taylor DeMent  
# date: 5/5/2024    
# description: A program that converts QWERTY keystrokes
# to the DVORAK keyboard layout and prints the results 
#####################################################################

import keyboard

# Map out DVORAK keyboard
dvorak_mapping = {
    "q": "'", "w": ",", "e": ".", "r": "p", "t": "y", "y": "f", "u": "g", "i": "c", "o": "r", "p": "l",
    "a": "a", "s": "o", "d": "e", "f": "u", "g": "i", "h": "d", "j": "h", "k": "t", "l": "n", ";": "s",
    "z": ";", "x": "q", "c": "j", "v": "k", "b": "x", "n": "b", "m": "m", ",": "w", ".": "v", "/": "z",
    "backspace": "", "space": " ",
}

# Converting QWERTY input to DVORAK layout
def keyboard_conversion(key):
    if key in dvorak_mapping:
        return dvorak_mapping[key]
    return key

# Function that handles key presses and prints the conversion
def display_conversion(event):
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        dvorak_key = keyboard_conversion(key)
        print(dvorak_key, end='', flush=True)  # Print without newline to accumulate characters

# Listening for key events
keyboard.hook(display_conversion)

# Stops program when pressing "esc"
keyboard.wait('esc')


