"""classifier
"""
import numpy as np
import ds_image.classifier as c


class TestClassifier:
    """Classifier
    """


    def test_batch(self):
        """batch
        """
        target = c.Classifier(None, None, None, 2)
        
        x_cycle, y_cycle = target._batch(
            np.array([[1, 2], [3, 4], [5, 6]]), np.array([1, 2, 3]))
        
        assert (next(x_cycle) == np.array([[1, 2], [3, 4]])).all()
        assert (next(x_cycle) == np.array([[5, 6]])).all()
        assert (next(y_cycle) == np.array([1, 2])).all()
        assert (next(y_cycle) == np.array([3])).all()
