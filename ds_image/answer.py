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
    return np.concatenate([_convert(label) for label in df.iloc[:, 1]], axis=0)

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
        return l.Targets.HIRAGANA.one_hot()
    if label == 'katakana':
        return l.Targets.KATAKANA.one_hot()
    if label == 'latinalphabet':
        return l.Targets.ALPHABET.one_hot()
    
    raise ValueError(label)