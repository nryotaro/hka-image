# -*- coding: utf-8 -*-
"""Exposes the labels
"""
import enum as e

class Targets(e.Enum):
    """Represents the classes into which characters are classified.
    """
    HIRAGANA = 0
    KATAKANA = 1
    ALPHABET = 2