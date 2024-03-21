
from pygame import Surface
import pygame.transform as tf
from .frame import Frame
from pygame.font import Font


def __zoom_image(image: Surface, zoom_level) -> Surface:
    """Rescale the image by zooming."""
    w, h = image.get_size()
    return tf.scale(image, (w*zoom_level, h*zoom_level))

class DynamicFrame(Frame):
    """A Frame where we can zoom, put alpha and rotate component."""

    def __init__(self, background_path: str, font: Font, zoom_level: float):
        super().__init__(background_path, font)
        self._zoom_level = zoom_level
        self._zoom_background = __zoom_image(self._background, zoom_level)
        self.zoom_window = Surface(self._zoom_background.get_size())
    
    def blit_background(self, zoom: bool):
        """Bilt the background on the window."""
        if zoom:
            self.zoom_window.blit(self._zoom_background, (0,0))
        else:
            self.window.blit(self._background,(0,0))
        
    def load_image(self, image_name, path):
        """Load an image"""
        super().load_image(image_name, path)
        self._images[image_name + 'zoom'] = __zoom_image(self._images[image_name], self._zoom_level)
    
    def blit(
            self,
            image_name: str,
            position: tuple[int,int],
            orientation: float,
            alpha: float,
            zoom: bool,
        ):
        """Blit an image on the screen."""
        if zoom:
            image_name = image_name + 'zoom'
            position = position[0]*self._zoom_level, position[1]*self._zoom_level
        image = self._images[image_name]
        image_tr = tf.rotate(image, orientation)
        image_tr.set_alpha(alpha)
        rect = image.get_rect()
        blit_x, blit_y = position[0] - rect.width//2, position[1] - rect.height//2
        if zoom:
            self.window.blit(image,(blit_x,blit_y))
        else:
            self.zoom_window.blit(image,(blit_x,blit_y))
        