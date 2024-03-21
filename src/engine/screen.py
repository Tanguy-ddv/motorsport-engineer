"""The screen of the engine display the content of the game."""

import pygame.display as ds
from .frame import Frame, DynamicFrame
from pygame import Rect

class Screen:
    """The screen is used to display the game content."""

    def __init__(self, width, height, caption) -> None:
        self.__window = ds.set_mode((width, height))
        ds.set_caption(caption)
        self.toggle_fullscreen()
        self.__frames: dict[str, Frame | DynamicFrame] = {}

    def update(self):
        """This function must be called at the end of the game loop."""
        ds.update()
    
    def toggle_fullscreen(self):
        """toggle the fullscreen."""
        ds.toggle_fullscreen()
    
    def add_frame(self, name: str, background_path: str, zoom_level: float = None):
        """Add a new frame to the screen."""
        if zoom_level is None:
            self.__frames[name] = Frame(background_path)
        else:
            self.__frames[name] = DynamicFrame(background_path, zoom_level)
    
    def remove_frame(self, name: str):
        """Delete a frame from the screen."""
        if name in self.__frames:
            del self.__frames[name]
    
    def clean(self):
        """Clean the window"""
        self.__window.fill((255,255,255))

    def blit_background_on_frame(self, frame_name, zoom):
        """Blit the background of the image."""
        frame = self.__frames[frame_name]
        if isinstance(frame, DynamicFrame):
            frame.blit_background(zoom)
        else:
            frame.blit_background()

    def blit_on_frame(self, frame_name, image_name, position, orientation: float = None, alpha: float = None, zoom: bool = False):
        """Blit on image of a frame on the frame."""
        frame = self.__frames[frame_name]
        if isinstance(frame, DynamicFrame):
            frame.blit(image_name, position, orientation, alpha, zoom)
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
            width, height = frame.get_size()
            left, top = focus_x - width//2, focus_y - height//2
            image = frame.zoom_window.subsurface(Rect(left, top, width, height))
            self.__window.blit(image, (left, top))
    