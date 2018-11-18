# -*- coding: utf-8 -*-
"""Exposes the labels
"""
import enum as e
import numpy as np

class Targets(e.Enum):
    """Represents the classes into which characters are classified.
    """
    HIRAGANA = 0
    KATAKANA = 1 
    ALPHABET = 2 

    def one_hot(self):
        if self.value == 0:
            return np.array([[1,0,0]])
        if self.value == 1:
            return np.array([[0,1,0]])
        if self.value == 2:
            return np.array([[0,0,1]])