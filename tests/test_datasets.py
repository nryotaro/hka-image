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


class TestDatasetsGenerator:
    """DatasetsGenerator
    """


    def test_generate_patterns(self):
        """generate_patterns
        """
        datasets_generator = d.create_datasets_generator()
        assert len(datasets_generator.generate_petterns()) == 16425
    
    def test_generate_images(self):
        """
        """
        datasets_generator = d.create_datasets_generator()
        assert len(datasets_generator.generate_images()) == 16425