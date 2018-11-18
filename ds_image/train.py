"""Implements functions to fit an estimators on generated datasets.
"""
import numpy as np
import ds_image.datasets as d
import ds_image.image as i
import ds_image.classifier as c


def train(log_dir, x_test,  y_test):
    """Fits the estimater on generated datasets.

    Parameters
    ----------
    x_test : numpy.ndarray

    y_test : numpy.ndarray

    Returns
    -------
    :py:class:`ds_image.classifier.Classifier`
    """
    generator = d.create_datasets_generator()
    labeled_images = generator.generate_images()
    labels = np.concatenate([label for _, label in labeled_images], axis=0)
    images = i.vectorize_images([image for image, _ in labeled_images])

    classifier = c.Classifier(log_dir, 32, 64, 50)
    classifier.prepare()
    classifier.fit(images, labels, x_test, y_test)
    return classifier 