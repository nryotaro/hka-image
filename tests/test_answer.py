"""Tests of answer modules.
"""
import os
import ds_image.answer as a


def test_read_answer_file():
    """
    """
    answer = os.path.join(os.path.dirname(__file__), '..', 'answer.csv') 
    sheet = a.read_answer_file(answer)
    assert sheet.shape == (5000, 3) 


def test_load_test_datasets():
    """
    """
    image_dir = os.path.join(os.path.dirname(__file__), 'images') 
    answer_file = os.path.join(os.path.dirname(__file__), 'answer.csv') 
    x_test, y_test = a.load_test_datasets(image_dir, answer_file)

    assert x_test.shape == (3, 784)
    assert y_test.shape == (3, 3)
