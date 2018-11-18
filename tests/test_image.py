"""test image
"""
import os
import pytest
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import ds_image.image as i


class TestImageGenerator:
    """ImageGenerator
    """

    def test_generate(self, tmpdir):
        """generate
        """
        generator = i.create_image_generator()

        image = generator.generate('a', (5, 5), 18)
        
        font_path = os.path.join(
            os.path.dirname(__file__), '..', 'ds_image', 'mplus-1mn-regular.ttf')
        font = ImageFont.truetype(font_path, 18)
        expected_img = Image.new("L", (28, 28), 'white')
        draw = ImageDraw.Draw(expected_img)
        draw.text((5, 5), 'a', font=font)

        img_file = os.path.join(tmpdir, 'a.png')
        image.save(img_file) 
        persisted_img = np.array(Image.open(img_file), 'f')

        assert (np.array(image, 'f') == np.array(expected_img, 'f')).all()
        assert (persisted_img == np.array(image, 'f')).all()

def generate_a_image():
    font_path = os.path.join(
        os.path.dirname(__file__), '..', 'ds_image', 'mplus-1mn-regular.ttf')
    font = ImageFont.truetype(font_path, 18)
    image = Image.new("L", (28, 28), 'white')
    ImageDraw.Draw(image).text((5, 5), 'a', font=font)
    return image

def test_vectorize_image():
    """vectorize_image
    """
    image = generate_a_image()
    array = i.vectorize_image(image)

    assert array.shape == (1, 784)

def test_vectorize_images():
    """vectorize_images
    """
    image0, image1 = generate_a_image(), generate_a_image()
    assert i.vectorize_images([image0, image1]).shape == (2, 784)

def test_read_images():
    """read_images
    """
    image_dir = os.path.join(os.path.dirname(__file__), 'images')
    images_array = i.read_images(image_dir)
    assert images_array.shape == (3, 784)
