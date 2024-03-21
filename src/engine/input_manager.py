"""The input managers manage the inputs of the users: keyboard and mouse."""

import pygame.event as ev
from pygame import mouse, key
from pygame import MOUSEBUTTONDOWN, KEYDOWN

class InputManager:
    """The input managers manage the inputs of the users: keyboard and mouse."""

    def __get_click(self) -> dict:
        """Return the value of the position of the click if the user clikced."""
        for event in ev.get():
            if event.type == MOUSEBUTTONDOWN:
                return (event.button, mouse.get_pos())
    
    def __get_key(self) -> dict:
        """Return the value of the key pressed."""
        for event in ev.get():
            if event.type == KEYDOWN:
                return key.name(event.key)
    
    def get_input(self) -> dict:
        """Get the user input."""
        inputs = {}
        click = self.__get_click()
        if click:
            inputs['mouse'] = click
        key = self.__get_key()
        if key:
            inputs['key'] = key
        return inputs
