import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the images to the range [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape the images to have a single channel (grayscale)
x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))

# One-hot encode the labels
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    return model

model = create_model()
model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=10, batch_size=32,
                    validation_data=(x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# Save the model and weights
model.save('path/to/model_directory/my_model.h5')
model.save_weights('path/to/model_directory/my_model_weights.ckpt')

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