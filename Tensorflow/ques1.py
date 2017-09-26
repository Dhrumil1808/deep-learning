import tensorflow as tf
a = tf.random_uniform([], -1, 1,tf.float32)
b = tf.random_uniform([], -1, 1,tf.float32)
def f1():return tf.add(a,b)
def f2():return 0.0
r = tf.case([(tf.less(a, b), f1)], default=f2)

summation = a + b
tensor_addition = tf.add(a,b)
with tf.Session() as sess:
    print sess.run(summation)
    print sess.run(tensor_addition)
    print sess.run(a)
    print sess.run(b)
