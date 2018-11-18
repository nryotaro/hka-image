"""Does basic configuration for the logging system of this package.
"""
import logging


def config(verbose):
    """Set the level of ``ds_image`` logger to py:const:`logging.DEBUG` when ``verbose`` is true.

    Parameters
    ----------
    verbose : bool
        The level gets py:const:`logging.DEBUG` when ``verbose`` is False.
    """
    logging.basicConfig(format='%(levelname)s:%(asctime)s:%(name)s:%(message)s')
    logging.getLogger('ds_image').setLevel(logging.DEBUG if verbose else logging.INFO)