"""Implements functions to fit an estimators on generated datasets.
"""
import random
import numpy as np
import ds_image.datasets as d
import ds_image.image as i
import ds_image.classifier as c


def train(x_test, y_test):
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
    random.shuffle(labeled_images)
    labels = np.concatenate([label for _, label in labeled_images], axis=0)
    images = i.vectorize_images([image for image, _ in labeled_images])

    classifier = c.create_classifier()
    classifier.fit(images/255, labels, epochs=20, batch_size=50,
          validation_data=(x_test/255, y_test))

    return classifier 
