from tensorflow import keras  # TensorFlow is required for Keras to work
import cv2
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Load the model
model = keras.load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def classification(model, cam):
    # define data array
    data = []
    frame = cam.read()
    # Replace this with the path to your image
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Convert the RGB frame to a PIL Image
    image = Image.fromarray(frame_rgb)

    # resizing the image to be at least 224x224 and then cropping from the center
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    result = class_name[2:]
    print("Class:", result, end="")
    print("Confidence Score:", confidence_score)
    return [result, confidence_score]
