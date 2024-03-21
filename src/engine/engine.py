"""The engine is used to manage inputs, sounds and displays."""
import pygame
import pygame.event as ev
from pygame import mouse, key
from pygame import MOUSEBUTTONDOWN, KEYDOWN, QUIT
from .mixer import Mixer
from .screen import Screen

class Engine:
    """An engine is a object used to manage inputs, sounds and to display the image."""

    def __init__(self, caption, width, height, fps) -> None:
        """Create the engine."""
        pygame.init()

        self.screen = Screen(width, height, caption)
        self.mixer = Mixer()
        self.__wait_time = int(1000/fps) # [ms] the waiting time at the end of each frame.

    def __del__(self):
        """This function is called when the engine instance is killed."""
        pygame.quit()

    def end_of_loop(self) -> None:
        """Update the screen at the end of the loop"""
        self.screen.update()
        self.mixer.update()
        pygame.time.wait(self.__wait_time)
    
    def get_input(self) -> dict:
        """Get the user input."""
        inputs = {'mouse' : [], 'key' : [], 'quit' : False}
        for event in ev.get():
            if event.type == MOUSEBUTTONDOWN:
                inputs['mouse'].append((event.button, mouse.get_pos()))
            if event.type == KEYDOWN:
                inputs['key'].append(key.name(event.key))
            if event.type == QUIT:
                inputs['quit'] = True
        return inputs