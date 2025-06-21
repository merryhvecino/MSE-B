import tensorflow as tf
import matplotlib.pyplot as plt

image_path = 'ACTIVITY23\image.jpg'
image = tf.keras.utils.load_img(image_path)
plt.imshow(image)
plt.axis('off')
plt.title("Image loaded with TensorFlow")
plt.show()
