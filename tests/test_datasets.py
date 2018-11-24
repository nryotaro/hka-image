"""datasets
"""
import pytest
import ds_image.datasets as d
import ds_image.label as l


def test_exhaustive_xy():
    """exhaustive_xy
    """
    assert 25 == len(d.exhaustive_xy)


def test_characters():
    """characters
    """
    for target in ['ゔ', 'ゃ', 'ゕ', 'ゖ']:
        assert target in d.hiragana_list

    for target in ['ヴ', 'ヵ', 'ヶ','ヷ', 'ヸ', 'ヹ', 'ヺ']:
        assert target in d.katanaka_list

    for target in ['A', 'a']:
        assert target in d.alphabet_list


class TestDatasetsGenerator:
    """DatasetsGenerator
    """

    def test_generate_patterns(self):
        """generate_patterns
        """
        datasets_generator = d.create_datasets_generator()
        patterns = datasets_generator.generate_petterns()

        assert len(patterns) == 17100

        for pattern in [((4,4), 16, l.Targets.ALPHABET, 'a')]:
            assert pattern in patterns

    def test_generate_images(self):
        """
        """
        datasets_generator = d.create_datasets_generator()
        assert len(datasets_generator.generate_images()) == 17100


    def test_calc_positions(self):
        """_calc_positions
        """
        datasets_generator = d.create_datasets_generator()
        positions = datasets_generator._calc_positions(17)
        assert len(positions) == 25
        for position in [(3.5, 3.5), (6.5, 5.5), (5.5, 5.5), (7.5, 7.5)]:
            assert position in positions
