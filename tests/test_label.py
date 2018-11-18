"""label
"""
import numpy as np
import ds_image.label as l


def test_targets():
    """Targets
    """
    assert l.Targets.HIRAGANA.value == 0
    assert l.Targets.KATAKANA.value == 1
    assert l.Targets.ALPHABET.value == 2

    assert (l.Targets.HIRAGANA.one_hot() == np.array([[1, 0, 0]])).all()