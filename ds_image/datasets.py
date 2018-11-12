"""
"""
import itertools
import ds_image.label as l


#: All the possible top left corners of characters.
exhaustive_xy = list(itertools.product(range(3, 8), range(3, 8)))

#: Contains the hiragana characters.
hiragana_list = [chr(i) for i in range(12353, 12436)]

#: Contains the katakana characters.
katanaka_list = [chr(i) for i in range(12449, 12532+1)]

#: Contains the alphabet characters.
alphabet_list = [chr(i) for i in list(range(65, 65+26)) + list(range(97, 97+26))]

#: All the possive fontsizes in test datasets.
sizes = list(range(16, 19))


def generate_patterns():
    """Generates the possible patterns in datasets.

    Returns
    -------
    ((int, int), int, :py:class:`ds_image.label.Targets`, str)

    """
    for xy, size, (label, char) in itertools.product(
        exhaustive_xy,
        sizes, 
        list(zip(itertools.repeat(l.Targets.HIRAGANA), hiragana_list)) +
        list(zip(itertools.repeat(l.Targets.KATAKANA), katanaka_list)) +
        list(zip(itertools.repeat(l.Targets.ALPHABET), alphabet_list))):
        yield (xy, size, label, char)


def generate(train_dir, labels):
    """

    Parameters
    ----------

    Returns
    -------
    None
        Returns None.
    """