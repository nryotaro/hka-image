"""
"""
import argparse


def parse(args):
    """
    Parameters
    ----------
    args : list

    Returns
    -------
    Namespace
    """
    parser = argparse.ArgumentParser(
        description='A classifier that estimates writing system of images.')
    parser.add_argument('imagedir', help='A directory images are put.')
    parser.add_argument('answerfile', help='The file in  CSV format contains target labels.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Be verbose.')

    return parser.parse_args(args)
