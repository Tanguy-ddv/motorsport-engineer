"""A dynamic frame is a frame where objects can be rotated, changed transparancy, and which window can be zoomed on. """


from pygame import Surface
import pygame.transform as tf
import pygame.image as im
from .frame import Frame
from pygame.font import Font

def _zoom_image(image: Surface, zoom_level) -> Surface:
    """Rescale the image by zooming."""
    w, h = image.get_size()
    return tf.scale(image, (w*zoom_level, h*zoom_level))

class DynamicFrame(Frame):
    """A Frame where we can zoom, put alpha and rotate component."""

    def __init__(self, background_path: str, font: Font, zoom_level: float, zoom_background_path: str=None):
        """
        Create a dynamic frame.

        brackground_path: The path to the background image.
        font: the pygame.font.Font object to display text. If set to None, no text can be displayed on this frame.
        zoom_level: a float representing the level of zoom.
        zoom_background_path: if the zoom image already exist in the assets folder, you can load it instead of resizing the small one.
        """
        super().__init__(background_path, font)
        # There is two versions of the window, the zoomed one and the normal.
        self._zoom_level = zoom_level
        if zoom_background_path is not None:
            self._zoom_background = im.load(zoom_background_path) # In case the image with a better resolution already exists.
        self._zoom_background = _zoom_image(self._background, zoom_level)
        self.zoom_window = Surface(self._zoom_background.get_size())
    
    def get_zoom_level(self):
        return self._zoom_level

    def get_size(self, zoom: bool = False):
        """
        return the size of the background.
        
        if zoom = True, return the size of the zoom background, i.e size()*zoom_level
        """
        if zoom:
            return self._zoom_background.get_size()
        else:
            return self._background.get_size()
    
    def write(self, text: str, position: tuple[int, int], antialias: bool, color: tuple[int, int, int], zoom: bool = False):
        """Write something on the screen."""
        if not zoom:
            super().write(text, position, antialias, color)
        else:
            if self._font is None:
                raise TypeError("This frame don't have any font.")
            text_image = self._font.render(text, antialias, color)
            rect = text_image.get_rect()
            blit_x, blit_y = position[0]*self._zoom_level - rect.width//2, position[1]*self._zoom_level - rect.height//2
            self.zoom_window.blit(text_image, (blit_x,blit_y))

    def blit_background(self, zoom: bool):
        """Bilt the background on the window."""
        if zoom:
            self.zoom_window.blit(self._zoom_background, (0,0))
        else:
            self.window.blit(self._background,(0,0))
        
    def load_image(self, image_name, path):
        """Load an image"""
        super().load_image(image_name, path)
        self._images[image_name + 'zoom'] = _zoom_image(self._images[image_name], self._zoom_level)
    
    def blit(
            self,
            image_name: str,
            position: tuple[int,int],
            orientation: float,
            alpha: float,
            zoom: bool,
            zoom_image: bool = True
        ):
        """
        Blit an image on the screen.
    
        image_name : the name of the image previously loaded.
        position: the position of the center of the image.
        orientation: the orientation of the image, must be float in radians.
        alpha: The alpha component of the image to make transparent.
        zoom: bool. If true, the image is bilt on the zoom window, else on the normal window.
        zoom_image: If true, the image bilt on the zoom background is the zoom image, else it is the normal one.
        use zoom_image = False when the image loaded is made only to be plotted on the zoom image, and the size matches.
        """
        if zoom:
            position = position[0]*self._zoom_level, position[1]*self._zoom_level
            if zoom_image:
                image_name = image_name + 'zoom'
        image = self._images[image_name]
        image_tr = tf.rotate(image, orientation)
        image_tr.set_alpha(alpha)
        rect = image.get_rect()
        blit_x, blit_y = position[0] - rect.width//2, position[1] - rect.height//2
        if zoom:
            self.zoom_window.blit(image,(blit_x,blit_y))
        else:
            self.window.blit(image,(blit_x,blit_y))