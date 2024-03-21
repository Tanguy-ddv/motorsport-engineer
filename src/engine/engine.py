"""The engine is used to manage inputs, sounds and displays."""
import pygame
from .mixer import Mixer
from .screen import Screen
from .input_manager import InputManager

class Engine:
    """An engine is a object used to manage inputs, sounds and to display the image."""

    def __init__(self, caption, width, height, fps) -> None:
        """Create the engine."""
        pygame.init()

        self.screen = Screen(width, height, caption)
        self.mixer = Mixer()
        self.input_manager= InputManager()

        self.__wait_time = int(1000/fps) # [ms] the waiting time at the end of each frame.

    def __del__(self):
        """This function is called when the engine instance is killed."""
        pygame.quit()

    def end_of_loop(self) -> None:
        """Update the screen at the end of the loop"""
        self.screen.update()
        self.mixer.update()
        pygame.time.wait(self.__wait_time)

    def user_quit(self) -> bool:
        """Verify if the player want to leave the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False