"""
"""
import itertools
import ds_image.label as l
import ds_image.image as i


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


class DatasetsGenerator:
    """Generates datasets.
    
    Attributes
    ----------
    _image_generator : :py:class:`ds_image.image.ImageGenerator`
        Generates images.
    """

    def __init__(self, image_generator):
       self._image_generator = image_generator

    def generate_images(self):
        """Generates all the images that can be in test datasets.

        Returns 
        -------
        list
            Each item is the tuple that the first element is an image, 
            and the second one represents the writing system of the letter in the image.
        """
        return [(self._image_generator.generate(char, xy, size), label.value) \
                for xy, size, label, char in self.generate_petterns()]

    def generate_petterns(self):
        """Creates the exhaustive patterns.

        Returns
        -------
        list
            Each item is ((int, int), int, :py:class:`ds_image.label.Targets`, str).
        """
        return [(xy, size, label, char) for xy, size, (label, char) in itertools.product(
                exhaustive_xy,
                sizes, 
                list(zip(itertools.repeat(l.Targets.HIRAGANA), hiragana_list)) +
                list(zip(itertools.repeat(l.Targets.KATAKANA), katanaka_list)) +
                list(zip(itertools.repeat(l.Targets.ALPHABET), alphabet_list)))]


def create_datasets_generator():
    """Constructs :py:class:`DatasetsGenerator`

    Returns
    -------
    :py:class:`DatasetsGenerator`
    """
    image_generator = i.create_image_generator()
    return DatasetsGenerator(image_generator)
