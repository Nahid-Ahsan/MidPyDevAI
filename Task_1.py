# import libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models, layers
import matplotlib.pyplot as plt

# load dataset
mnist=keras.datasets.mnist 
(Xtrain,ytrain),(Xtest,ytest)= mnist.load_data()

# normalize pixel values to be between 0 and 1
Xtrain, Xtest = Xtrain / 255.0, Xtest / 255.0

# create a sequential model 
model=models.Sequential()
model.add(layers.Conv2D(6,(3,3),input_shape=(28,28,1),activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Conv2D(10,(3,3),activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Flatten(input_shape=(28,28))) 
model.add(layers.Dense(128, activation='relu')) 
model.add(layers.Dense(100, activation='relu'))  
model.add(layers.Dense(80, activation='relu')) 
model.add(layers.Dense(10, activation='softmax')) 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) 
model.summary()

# reshaping the dataset
Xtrain=Xtrain.reshape(60000,28,28,1)
Xtest=Xtest.reshape(10000,28,28,1)

# train the model
model.fit(Xtrain,ytrain,epochs=20,batch_size=1000,verbose=True,validation_data=(Xtest,ytest))


# evaluate accuracy of the model
test_loss, test_acc = model.evaluate(Xtest, ytest)

# print evaluation report
print(f"Test Accuracy: {test_acc * 100:.2f}%")
print(f"Test Loss: {test_loss:.4f}")


"""
               *** Explaination of this neural network ***

The given problem is mnist dataset classification that classify the numerical number of 0 to 9. Here has a several
steps to build this system. All of these explain in step by step.

1. Bring in the required libraries: These deep learning packages, TensorFlow and Keras, are used to create and train neural networks.

2. Load the MNIST dataset: keras.datasets is used to load the MNIST dataset.60,000 training images and 10,000 test images of handwritten digits (0-9) with matching labels make up the mnist database.

3. Normalize pixel values: By dividing the image's pixel values by 255.0, the images' pixel values are normalized to fall between [0, 1]. 
   It lowers the training process's computing expense.

4. Construct a sequential model. A sequential model is a stack of layers that is linear. Max-pooling layers are inserted after convolutional layers.
   The data is flattened after the convolutional and pooling layers. With ReLU activation functions, several dense, completely connected layers are added. For multiclass classification, the final dense layer comprises 10 units with softmax activation.

5. Compile the model: The sparse categorical cross-entropy loss function and Adam optimizer are used to create the Sequential model.
   Accuracy serves as the evaluation metric.

6. Restructure the dataset: The input data (Xtrain and Xtest) are restructured to have dimensions (number of samples, height, width, and channels) that correspond to the input shape anticipated by the model (28x28 pixels with one channel).

7. Train the model: Using the training data (Xtrain, ytrain), the model is trained. It operated with a batch size of 1000 throughout 20 epochs.

8. Evaluate the model: Using test data, the model is assessed, and test loss and test accuracy are computed.

9. Print the evaluation report: To assess how well the model works with obfuscated data, the script produces the test accuracy and test loss.

"""

