"""datasets
"""
import pytest
import ds_image.datasets as d 


def test_exhaustive_xy():
    """exhaustive_xy
    """
    assert 25 == len(d.exhaustive_xy)


def test_characters():
    """characters
    """
    assert 'あ' in d.hiragana_list 
    assert 'ア' in d.katanaka_list
    assert 'A' in d.alphabet_list
    assert 'a' in d.alphabet_list

@pytest.mark.skip
def test_emit_patterns():
    """emit_patterns
    """
    d.emit_patterns()