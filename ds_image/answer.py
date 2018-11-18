"""
"""
import pandas as pd
import numpy as np
import ds_image.label as l


def read_answer_file(target_file):
    """Reads the file contains the target values of the test datasets into an array.

    Parameters
    ----------
    target_file : str

    Returns
    -------
    numpy.ndarray

    """
    df = pd.read_csv(target_file)
    return np.array([_convert(label).value for label in df.iloc[:, 1]])

def _convert(label):
    """Converts label to an integer.

    Parameters
    ----------
    str
        hiragana, latinalphabet, katakana

    Returns
    -------
    :py:class:`ds_image.label.Targets`
    """
    if label == 'hiragana':
        return l.Targets.HIRAGANA
    if label == 'katakana':
        return l.Targets.KATAKANA
    if label == 'latinalphabet':
        return l.Targets.ALPHABET
    
    raise ValueError(label)