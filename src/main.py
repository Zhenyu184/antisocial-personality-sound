import sys
import pygame
import argparse
from pathlib import Path
from pynput import keyboard

SCRIPT_PATH = Path(__file__).resolve()
FOLDER_PATH = SCRIPT_PATH.parent
SOUNDS_PATH = FOLDER_PATH / '../assets/sound/gun/gunfire.mp3'

def load_sound(path: Path) -> None:
    pygame.mixer.music.load(path)

def on_press(key: keyboard.Key) -> None:
    match key:
        case keyboard.KeyCode(char='a'):
            pygame.mixer.music.play()
        case _:
            pass

def on_release(key: keyboard.Key) -> None:
    pass

def parse_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', action='store_true', help='list all sound style')
    parser.add_argument('-s', '--start', action='store_true', help='start listen keyboard')
    return parser

def main() -> int:
    Parser = parse_arguments()
    Args = Parser.parse_args()

    if Args.list:
        print("verbosity turned on")

    elif Args.start:
        pygame.mixer.init()
        load_sound(SOUNDS_PATH)

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    else: Parser.print_help()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())



