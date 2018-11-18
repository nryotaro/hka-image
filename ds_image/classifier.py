"""Implements the classifier that predicts writing system of letters. 
"""
import itertools
from logging import getLogger
import numpy as np
import tensorflow as tf


_LOGGER = getLogger(__name__)


class Classifier:
    """Predicts writing system of letters.

    Attributes
    ----------
    log_dir : str
        Writes logs into files inside the directory.
    """
    def __init__(self, log_dir, num_filters1, num_filters2, batch_size):
        self._log_dir = log_dir
        self._num_filters1 = num_filters1
        self._num_filters2 = num_filters2
        self._batch_size = batch_size

    def prepare(self):
        """Constructs the newral
        """
        with tf.Graph().as_default():
            # prepare_model
            self._construct_network()
            self._prepare_session()
    
    def fit(self, x_train, y_train, x_test, y_test):
        """
        Parameters
        ----------
        x_train : numpy.ndarray
            Each item is a numpy.ndarray that the shape is (1, 784)
        y_train : numpy.ndarray
            Each item is 1, 2, or 3 that represents the label of the corresponding element in x_train.
        x_test : numpy.ndarray

        y_test : numpy.ndarray

        TODO
        ----
        """
        x_train_iter, y_train_iter = self._batch(x_train, y_train)
        for index in range(20000):
            x_batch, y_batch = next(x_train_iter), next(y_train_iter)
            self.sess.run(
                self.train_step, 
                feed_dict={self.x:x_batch, self.t:y_batch, self.keep_prob:0.5})

            if index % 500 == 0:
                loss_val, acc_val = self.sess.run(
                    [self.loss, self.accuracy],
                    feed_dict={self.x: x_test, self.t: y_test, self.keep_prob:1.0})
                _LOGGER.info('Step: %d, Loss: %f, Accuracy: %f' % (index, loss_val, acc_val))
    
    def _batch(self, x_train, y_train):
        """
        Parameters
        ----------
        x_train : numpy.ndarray

        y_train : numpy.ndarray
        """
        return itertools.cycle(np.array_split(x_train, self._batch_size)), \
               itertools.cycle(np.array_split(y_train, self._batch_size))

    def _construct_network(self):
        """Constructs a CNN.
        """
        with tf.name_scope('input'):
            self.x = tf.placeholder(tf.float32, [None, 784], name='input') 
        with tf.name_scope('conv1'):
            x_image = tf.reshape(self.x, [-1, 28, 28, 1])
            W_conv1 = tf.Variable(
                tf.truncated_normal([5,5,1, self._num_filters1], stddev=0.1))
            h_conv1 = tf.nn.conv2d(
                x_image, W_conv1, strides=[1,1,1,1], padding='SAME')
            b_conv1 = tf.Variable(tf.constant(0.1, shape=[self._num_filters1]))
            h_conv1_cutoff = tf.nn.relu(h_conv1 + b_conv1)
        with tf.name_scope('pool1'):
            h_pool1 = tf.nn.max_pool(
                h_conv1_cutoff, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        with tf.name_scope('conv2'):
            W_conv2 = tf.Variable(
                tf.truncated_normal([5,5,self._num_filters1, self._num_filters2], stddev=0.1))
            h_conv2 = tf.nn.conv2d(h_pool1, W_conv2, strides=[1,1,1,1], padding='SAME')
            b_conv2 = tf.Variable(tf.constant(0.1, shape=[self._num_filters2]))
            h_conv2_cutoff = tf.nn.relu(h_conv2 + b_conv2)
        with tf.name_scope('pool2'):
            h_pool2 = tf.nn.max_pool(
                h_conv2_cutoff, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
        with tf.name_scope('fully-connected'):
            h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*self._num_filters2])
            num_units1 = 7*7*self._num_filters2
            num_units2 = 1024
            w2 = tf.Variable(tf.truncated_normal([num_units1, num_units2]))
            b2 = tf.Variable(tf.constant(0.1, shape=[num_units2]))
            hidden2 = tf.nn.relu(tf.matmul(h_pool2_flat, w2) + b2)
        with tf.name_scope('dropout'):
            self.keep_prob = tf.placeholder(tf.float32)
            hidden2_drop = tf.nn.dropout(hidden2, self.keep_prob)
        with tf.name_scope('output'):
            w0 = tf.Variable(tf.zeros([num_units2, 10]))
            b0 = tf.Variable(tf.zeros([10]))
            p = tf.nn.softmax(tf.matmul(hidden2_drop, w0) + b0)

        with tf.name_scope('optimization'):
            self.t = tf.placeholder(tf.float32, [None, 3], name='labels')
            self.loss = -tf.reduce_sum(self.t * tf.log(p), name='loss')
            self.train_step = tf.train.AdamOptimizer().minimize(loss)
        with tf.name_scope('evaluation'):
            correct_prediction = tf.equal(tf.argmax(p, 1), tf.argmax(self.t, 1))
            self.accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32), name='accuracy')

        tf.scalar_summary("loss", self.loss)
        tf.scalar_summary("accuracy", self.accuracy)

    
    def _prepare_session(self):
        """
        """
        self.sess = tf.Session()
        self.sess.run(tf.initialize_all_variables())
        self.saver = tf.train.Saver()
        self.summary = tf.merge_all_summaries()
        self.writer = tf.train.SummaryWriter(self._log_dir, self.sess.graph)