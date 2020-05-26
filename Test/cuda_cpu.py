#TensorFlow and tf.keras
import tensorflow as tf
#Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from time import time

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

#CPU运行
startTime1 = time()

with tf.device('/cpu:0'):
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(1000, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(1000, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=10)
    model.evaluate(x_test, y_test)

t1 = time() - startTime1

#GPU运行
startTime2 = time()

with tf.device('/gpu:0'):
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(1000, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(1000, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(x_train, y_train, epochs=10)
    model.evaluate(x_test, y_test)

t2 = time() - startTime2

#打印运行时间
print('使用cpu花的时间：', t1)
print('使用gpu花的时间：', t2)