import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(_, _), (x_test, y_test) = mnist.load_data()

# Normalize the images to the range [0, 1]
x_test = x_test / 255.0

# Reshape the images to have a single channel (grayscale)
x_test = x_test.reshape((-1, 28, 28, 1))

# One-hot encode the labels
y_test = to_categorical(y_test, num_classes=10)

# Load the saved model
model = load_model('path/to/model_directory/my_model.h5')
model.load_weights('path/to/model_directory/my_model_weights.ckpt')

# Obtain model predictions
y_pred = model.predict(x_test)

# Select a random index to visualize
idx = np.random.randint(0, len(x_test))

# Calculate the predicted class and confidence
predicted_class = np.argmax(y_pred[idx])
confidence = np.max(y_pred[idx]) * 100

# Display the image and the prediction
plt.imshow(x_test[idx].reshape(28, 28), cmap='gray')
plt.title(f"Predicted Class: {predicted_class}, Confidence: {confidence:.2f}%")
plt.show()