"""Exposes the function to generate images of the font.
"""
import os
from PIL import ImageFont, ImageDraw, Image
import numpy as np


class ImageGenerator:
    """Generates datasets.

    Attributes
    ----------
    _image_font : :py:class:`PIL.ImageFont.FreeTypeFont`
        Use the font to draw characters.
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

        Returns
        -------
        PIL.Image
            The image with the given properties.
        """
        img = Image.new("L", (28,28), 'white')
        draw = ImageDraw.Draw(img)
        draw.text(xy, char, font=self._image_font)
        return img

def create_image_generator():
    """Constructs :py:class:`ImageGenerator`
    """
    font_path = os.path.join(
        os.path.dirname(__file__), 'mplus-1mn-regular.ttf')
    font = ImageFont.truetype(font_path, 18)
    return ImageGenerator(font)

def vectorize_image(image):
    """Converts an image to a numpy.ndarray.

    Parameters
    ----------
    image : PIL.Image
        an image.

    Returns
    -------
    numpy.ndarray
        The shape is (1, -1).
    """
    return np.array(image, 'f').reshape(1, -1)

def vectorize_images(images):
    """Convers images to numpy.ndarray.

    Parameters
    ----------
    images : list
        Each item is an :py:class:`PIL.Image` object.

    Returns
    -------
    numpy.ndarray
        The length of the row is that of images.
    """
    return np.concatenate([vectorize_image(image) for image in images], axis=0)

def read_image(image_file):
    """
    """

    image = Image.open(image_file)
    vec_img = vectorize_image(image)
    image.close()
    return vec_img


def read_images(image_dir):
    """Reads images in the specified directory into np.ndarray.

    images are converted to numpy.ndarray.

    Parameters
    ----------
    image_dir : str
        directory path.

    Returns
    -------
    numpy.ndarray
    """
    img_vecs = []
    for img_path in [os.path.join(image_dir, image_file) for image_file in sorted(os.listdir(image_dir)) if image_file.endswith('.png')]:
        image = Image.open(img_path)
        img_vecs.append(vectorize_image(image))
        image.close()

    cat = np.concatenate(img_vecs, axis=0)
    return cat
