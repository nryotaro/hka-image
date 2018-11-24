"""
"""
import csv
import os.path
import pandas as pd
import numpy as np
import ds_image.label as l
import ds_image.image as i



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


def load_test_datasets(image_dir, target_file):
    """

    Parameters
    ----------
    image_dir : str

    target_file : str

    Returns
    -------
    x_test, y_test

    x_test : numpy.ndarray

    y_test : numpy.ndarray
    """

    with open(target_file) as targetf:
        rows = [row for row in csv.DictReader(targetf)]
        y_test = np.concatenate([_convert(row['label'])  for row in rows], axis=0) 
        x_test = np.concatenate(
            [i.read_image(os.path.join(image_dir, row['filename'])) for row in rows], axis=0)

        return x_test, y_test


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
