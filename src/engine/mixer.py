"""The mixer is used to mix music and sounds."""
import pygame.mixer as mx

class Mixer:
    """The mixer is used to mix music and sounds."""

    def __init__(self):
        self.__music_loop_start = None
        self.__sounds: dict[str, mx.Sound] = {}
        self.__activated = False

    def play_music(self, path, music_loop_start):
        """Load a music."""
        mx.music.load(path)
        mx.music.play(-1)
        self.__music_loop_start = music_loop_start
        self.__activated = True

    def update(self):
        """Do all the action done every loop."""
        if not mx.music.get_busy() and self.__activated:
            mx.music.set_pos(self.__music_loop_start)
        
    def load_sound(self, sound_name: str, sound_path: str):
        """Load a sound to be played during the game."""
        self.__sounds[sound_name] = mx.Sound(sound_path)
    
    def play_sound(self, sound_name: str):
        """Play a sound when an action is triggered."""
        if sound_name in self.__sounds:
            self.__sounds[sound_name].play()
        else:
            print(f"try to play the sound {sound_name} but is not loaded.")