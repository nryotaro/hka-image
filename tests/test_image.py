"""test image
"""
import os
import pytest
import numpy as np
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