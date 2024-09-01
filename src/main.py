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
    playsound(SOUNDS_PATH['press'])

def on_release(key: keyboard.Key) -> None:
    # if key == keyboard.KeyCode(char='a'):
    playsound(SOUNDS_PATH['release'])

def parse_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', action='store_true', help='list all sound styles')
    parser.add_argument('-s', '--start', action='store_true', help='start listening to keyboard')
    return parser

def main() -> int:
    parser = parse_arguments()
    args = parser.parse_args()

    if args.list:
        print("verbosity turned on")

    elif args.start:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    else: parser.print_help()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
