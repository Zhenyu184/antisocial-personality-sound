import sys
import argparse
from pathlib import Path
from pynput import keyboard
from playsound import playsound

SCRIPT_PATH = Path(__file__).resolve()
FOLDER_PATH = SCRIPT_PATH.parent
SOUNDS_PATH = {
    'press':   FOLDER_PATH / '../assets/sound/mechanical_switch /blue-switch-press-1.mp3',
    'release': FOLDER_PATH / '../assets/sound/mechanical_switch /blue-switch-release-1.mp3'
}

def on_press(key: keyboard.Key) -> None:
    # if key == keyboard.KeyCode(char='a'):
    try:
        playsound(SOUNDS_PATH['press'])
    except Exception as err: print(err)

def on_release(key: keyboard.Key) -> None:
    # if key == keyboard.KeyCode(char='a'):
    try:
        playsound(SOUNDS_PATH['release'])
    except Exception as err: print(err)


def parse_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--info', action='store_true', help='info info')
    return parser

def main() -> int:
    parser = parse_arguments()
    args = parser.parse_args()

    if args.info:
        print('info info')

    else: 
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
