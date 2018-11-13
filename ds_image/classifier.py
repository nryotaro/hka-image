"""Implements the classifier that predicts writing system of letters. 
"""
import tensorflow as tf

class Classifier:
    """Predicts writing system of letters.

    Attributes
    ----------
    log_dir : str
        Writes logs into files inside the directory.
    """
    def __init__(self, log_dir):
        self._log_dir = log_dir

    def prepare_model(self):
        """Constructs the newral
        """
        with tf.Graph().as_default():
            # prepare_model
            self._construct_network()
            self._prepare_session()
    
    def _construct_network(self):
        """
        """
        raise NotImplementedError
    
    def _prepare_session(self):
        """
        """
        sess = tf.Session()
        sess.run(tf.initialize_all_variables())
        summary = tf.merge_all_summaries()
        writer = tf.train.SummaryWriter(self._log_dir, sess.graph)
        self.sess = sess
        self.summary = summary
        self.writer = writer