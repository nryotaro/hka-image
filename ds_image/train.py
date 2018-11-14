"""Implements functions to fit an estimators on generated datasets.
"""
import numpy as np
import ds_image.datasets as d
import ds_image.image as i


def train():
    """Fits the estimater on generated datasets.

    TODO
    ----
    fix
    """
    generator = d.create_datasets_generator()
    labeled_images = generator.generate_images()
    labels = np.array([label for _, label in labeled_images])
    images = i.vectorize_images([image for image, _ in labeled_images])