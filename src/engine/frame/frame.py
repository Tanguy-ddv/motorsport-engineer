"""A frame represent a part of the screen."""

from pygame import Surface
import pygame.image as im
from pygame.font import Font

class Frame:
    """A frame is a part of the screen."""

    def __init__(self, background_path, font: Font):
        self._background = im.load(background_path)
        self._images: dict[str, Surface] = {}
        self.window = Surface(self._background.get_size())
        self._font = font
    
    def get_size(self):
        """Return the size of the frame, that is the size of the background"""
        return self.window.get_size()
    
    def load_image(self, image_name, path):
        """Load an image"""
        self._images[image_name] = im.load(path)
    
    def blit_background(self):
        """Bilt the background on the window."""
        self.window.blit(self._background, (0,0))
    
    def write(self, text: str, position: tuple[int, int], antialias: bool, color: tuple[int, int, int]):
        """Write something on the screen."""
        if self._font is None:
            raise TypeError("This frame don't have any font.")
        text_image = self._font.render(text, antialias, color)
        rect = text_image.get_rect()
        blit_x, blit_y = position[0] - rect.width//2, position[1] - rect.height//2
        self.window.blit(text_image,(blit_x,blit_y))
    
    def blit(self, image_name: str, position: tuple[int,int]):
        """Blit an image on the screen."""
        image = self._images[image_name]
        rect = image.get_rect()
        blit_x, blit_y = position[0] - rect.width//2, position[1] - rect.height//2
        self.window.blit(image,(blit_x,blit_y))