from tensorflow import keras  # TensorFlow is required for Keras to work
import cv2
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
from machine_learning import classification
import serial

arduino = serial.Serial(port="COM3", baudrate=9600, timeout=0.1)
cam = cv2.VideoCapture(0)
if not cam.isOpened:
    print("Camera not found")

# Load the model
model = keras.load_model("keras_Model.h5", compile=False)

while True:
    output = classification(model, cam)
    if output[0] == "Normal":
        arduino.write("a".encode())
    elif output[0] == "Dry":
        arduino.write("b".encode())
    elif output[0] == "Diseased":
        arduino.write("c".encode())
