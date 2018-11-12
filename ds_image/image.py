"""Exposes the function to generate images of the font.
"""
import os
from PIL import ImageFont, ImageDraw, Image


class ImageGenerator:
    """Generates datasets.

    Parameters
    ----------
    :py:class:`PIL.ImageFont.FreeTypeFont`

    """

    def __init__(self, image_font):
        self._image_font = image_font
    
    def generate(self, char, xy, size):
        """
        Parameters
        ----------
        char : str
            The character to draw.
        xy : tuple
            Top left corner of the text.
        size : int
            The size of the char.
        """
        img = Image.new("L", (28,28), 'white')
        draw = ImageDraw.Draw(img)
        draw.text(xy, char, font=self._image_font)
        return img

def create_image_generator():
    """Constructs :py:class:`ImageGenerator`
    """
    font_path = os.path.join(os.path.dirname(__file__), 'mplus-1mn-regular.ttf')
    font = ImageFont.truetype(font_path, 18)
    return ImageGenerator(font)