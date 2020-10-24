import cv2
import time
import keyboard
import tensorflow as tf
import numpy as np

categories = ['dislike', 'ok', 'like', 'peace']
IMG_SIZE = (64,64)

signs_model = tf.keras.models.load_model('sign_reader.model')
def predict_on_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, IMG_SIZE)
    image = np.reshape(image, (IMG_SIZE[0],IMG_SIZE[1],1))
    img_to_pred = np.expand_dims(image, axis=0)
    prediction = signs_model.predict(img_to_pred)
    category_index = np.argmax(prediction)
    category = categories[category_index]
    return category

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    pred = predict_on_image(img)
    print(pred)
    cv2.putText(img, pred, (30,50), cv2.FONT_HERSHEY_SIMPLEX, 4, (0,255,255),thickness=4)
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    