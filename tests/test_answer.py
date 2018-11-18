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