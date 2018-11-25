"""ds_image
"""
import sys
import ds_image.log as l
import ds_image.parser as p
import ds_image.train as t
import ds_image.answer as a
import ds_image.image as i

def main():
    """The entry point of this program.
    """
    opts = p.parse(sys.argv[1:])

    l.config(opts.verbose)
    x_test, y_test = a.load_test_datasets(opts.imagedir, opts.answerfile)
    t.train(x_test, y_test)
