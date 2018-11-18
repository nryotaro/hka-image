"""parser
"""
import ds_image.parser as p



class TestParse:
    """parse
    """


    def test_parse(self):
        """
        """
        opts = p.parse(['-v', 'lg', 'imgd', 'ans'])
        assert opts.logdir == 'lg'
        assert opts.imagedir == 'imgd'
        assert opts.answerfile == 'ans'
        assert opts.verbose