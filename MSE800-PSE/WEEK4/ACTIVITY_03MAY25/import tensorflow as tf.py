import tensorflow as tf
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# show the first n_rows * n_cols images of train dataset
n_rows = 4
n_cols = 8
plt.figure(figsize=(n_cols * 2, n_rows * 2))
for row in range(n_rows): # loop row
    for col in range(n_cols): # loop column
        index = n_cols * row + col
        plt.subplot(n_rows, n_cols, index + 1) # to generate n_rows and n_cols images, this is the (index + 1)th image
        plt.imshow(x_train[index], cmap="binary", interpolation="nearest")
        plt.axis('off')

plt.subplots_adjust(wspace=0.2, hspace=0.5) # to adjust layout
plt.show()