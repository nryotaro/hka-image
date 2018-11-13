"""Implements functions to fit an estimators on generated datasets.
"""
import ds_image.datasets as d
import ds_image.image as i


def train():
    """Fits the estimater on generated datasets.
    """
    generator = d.create_datasets_generator()
    labeled_images = generator.generate_images()

    train_datasets = [
        (i.vectorize_image(image), label) for image, label \
        in labeled_images]

    estimator = _fit(
        [vec_img for (vec_img, _) in train_datasets],
        [label for (_, label) in train_datasets])

    return estimator

def _fit(x_train, y_train):
    """
    Parameters
    ----------
    x_train : numpy.ndarray
    y_train : int

    Returns
    -------
    estimator
    """
