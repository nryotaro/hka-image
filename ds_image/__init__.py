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
    y_test = a.read_answer_file(opts.answerfile)
    x_test = i.read_images(opts.imagedir)
    t.train(opts.logdir, x_test, y_test)