"""train
"""
from unittest.mock import MagicMock, patch, call
import ds_image.train as t


@patch('ds_image.datasets.create_datasets_generator')
@patch('ds_image.image.vectorize_image')
@patch('ds_image.train._fit')
def test_train(fit, vectorize_image, create_datasets_generator):

    generator = create_datasets_generator.return_value
    image0, image1 = MagicMock(), MagicMock()
    vec_image0, vec_image1 = MagicMock(), MagicMock()
    labeles_images = [(image0, 0), (image1, 1)] 
    generator.generate_images.return_value = labeles_images

    def mock_vectorize_image(image):
        if image0 == image:
            return vec_image0
        if image1 == image:
            return vec_image1
        raise ValueError

    vectorize_image.side_effect = mock_vectorize_image

    estimator = t.train()

    assert create_datasets_generator.call_args_list == [call()]
    assert generator.generate_images.call_args_list == [call()]
    assert vectorize_image.call_args_list == [
        call(image0), call(image1)]
    assert fit.call_args_list == [call([vec_image0, vec_image1], [0, 1])]
    assert estimator == fit.return_value



    