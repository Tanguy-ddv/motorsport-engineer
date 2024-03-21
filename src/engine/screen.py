"""The screen of the engine display the content of the game."""

import pygame.display as ds
from .frame import Frame, DynamicFrame
from pygame import Rect
from pygame.font import Font

class Screen:
    """The screen is used to display the game content."""

    def __init__(self, width, height, caption) -> None:
        self.__window = ds.set_mode((width, height))
        self.__dimensions = (width, height)
        ds.set_caption(caption)
        #self.toggle_fullscreen()
        self.__frames: dict[str, Frame | DynamicFrame] = {}

    def update(self):
        """This function must be called at the end of the game loop."""
        ds.update()
    
    def toggle_fullscreen(self):
        """toggle the fullscreen."""
        ds.toggle_fullscreen()
    
    def add_frame(self, name: str, background_path: str, font : Font = None, zoom_level: float = None):
        """Add a new frame to the screen."""
        if zoom_level is None:
            self.__frames[name] = Frame(background_path, font)
        else:
            self.__frames[name] = DynamicFrame(background_path, font, zoom_level)
    
    def remove_frame(self, name: str):
        """Delete a frame from the screen."""
        if name in self.__frames:
            del self.__frames[name]
    
    def clean(self):
        """Clean the window"""
        self.__window.fill((255,255,255))

    def blit_background_on_frame(self, frame_name, zoom = False):
        """Blit the background of the image."""
        frame = self.__frames[frame_name]
        if isinstance(frame, DynamicFrame):
            frame.blit_background(zoom)
        else:
            frame.blit_background()
        
    def write_on_frame(self, frame_name: str, text:str, position: tuple[int, int], antialias: bool, color: tuple[int,int,int], zoom):
        """Write something on a frame"""
        frame = self.__frames[frame_name]
        if isinstance(frame, DynamicFrame):
            frame.write(text, position, antialias, color, zoom)
        else:
            frame.write(text, position, antialias, color)
    
    def load_image_on_frame(self, frame_name, image_name, path):
        """Load an image on the frame."""
        self.__frames[frame_name].load_image(image_name, path)

    def blit_on_frame(self, frame_name, image_name, position, orientation: float = 0, alpha: int = 255, zoom: bool = False, zoom_image = False):
        """Blit on image of a frame on the frame."""
        frame = self.__frames[frame_name]
        if isinstance(frame, DynamicFrame):
            frame.blit(image_name, position, orientation, alpha, zoom, zoom_image)
        else:
            frame.blit(image_name, position)
    
    def blit_frame(self, name: str, left: int = 0, top: int = 0, focus: tuple[int, int]= None):
        """
        Blit the frame on the window.
        
        name: the name of the frame that is blit
        left, top: the coordinate of the upper left point of the frame in the window
        focus: the coordinates of the center of the frame. If there is no zoom, need to be None
        """
        if focus is None:
            # There is no zoom made.
            self.__window.blit(self.__frames[name].window, (left, top))
        else:
            focus_x, focus_y = focus
            frame = self.__frames[name]
            zoom_level = frame.get_zoom_level()
            focus_x, focus_y = focus_x*zoom_level, focus_y*zoom_level
            frame_width, frame_height = frame.get_size(False)
            background_width, background_height = frame.get_size(True)
            window_left = focus_x - frame_width//2
            window_top = focus_y - frame_height//2
            if window_left < 0:
                window_left = 0
            if window_top < 0:
                window_top = 0
            if window_left > background_width - frame_width:
                window_left = background_width - frame_width
            if window_top > background_height - frame_height:
                window_top = background_height - frame_height
            image = frame.zoom_window.subsurface(Rect(window_left, window_top, frame_width, frame_height))
            self.__window.blit(image, (left, top))
    