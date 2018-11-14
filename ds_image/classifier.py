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
    def __init__(self, log_dir, num_filters1, num_filters2):
        self._log_dir = log_dir
        self._num_filters1 = num_filters1
        self._num_filters2 = num_filters2

    def prepare_model(self):
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
        x_train : list
            Each item is a numpy.ndarray that the shape is (1, 784)
        y_train : list
            Each item is 1, 2, or 3 that represents the label of the corresponding element in x_train.

        TODO
        ----
        """

        for index in range(20000):
            pass
    
    def _batch(self, x_train, y_train):
        """
        """

    def _construct_network(self):
        """Constructs a CNN.
        """
        with tf.name_scope('input'):
            x = tf.placeholder(tf.float32, [None, 784], name='input') 
        with tf.name_scope('conv1'):
            x_image = tf.reshape(x, [-1, 28, 28, 1])
            W_conv1 = tf.Variable(
                tf.truncated_normal([5,5,1, self._num_filters1], stddev=0.1))
            h_conv1 = tf.nn.conv2d(
                x_image, W_conv1, strides=[1,1,1,1], padding='SAME')
            b_conv1 = tf.Variable(tf.constant(0.1, shape=[self._num_filters1]))
            h_conv1_cutoff = tf.nn.relu(h_conv1 + b_conv1)
        with tf.name_score('pool1'):
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
            keep_prob = tf.placeholder(tf.float32)
            hidden2_drop = tf.nn.dropout(hidden2, keep_prob)
        with tf.name_scope('output'):
            w0 = tf.Variable(tf.zeros([num_units2, 10]))
            b0 = tf.Variable(tf.zeros([10]))
            p = tf.nn.softmax(tf.matmul(hidden2_drop, w0) + b0)

        with tf.name_scope('optimization'):
            t = tf.placeholder(tf.float32, [None, 3], name='labels')
            loss = -tf.reduce_sum(t * tf.log(p), name='loss')
            train_step = tf.train.AdamOptimizer().minimize(loss)
        with tf.name_scope('evaluation'):
            correct_prediction = tf.equal(tf.argmax(p, 1), tf.argmax(t, 1))
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32), name='accuracy')
            # conv2d -> 画像の枚数 ×画像サイズ（縦×横）×レイヤー数
            # padding = same 存在しない部分のピクセルについては、その値を0として計算を行います
            # strides = [1,dy,dx,1]
            # +bまでがw
            # truncated_normalは、指定サイズの多次元リストに対応するVariableを用意して、
            # それぞれの要素を平均0、標準偏差1の正規分布の乱数で初期化します 
        tf.scalar_summary("loss", loss)
        tf.scalar_summary("accuracy", accuracy)

    
    def _prepare_session(self):
        """
        """
        sess = tf.Session()
        sess.run(tf.initialize_all_variables())
        self.saver = tf.train.Saver()
        summary = tf.merge_all_summaries()
        writer = tf.train.SummaryWriter(self._log_dir, sess.graph)
        self.sess = sess
        self.summary = summary
        self.writer = writer