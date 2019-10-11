#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:09:46 2019

@author: kazzastic
"""

from flask import Flask, render_template, request
import tensorflow as tf
from skimage import io
import cv2

app = Flask(__name__)


CATEGORIES = ["WHITE-HOUSE", "NIC"]

def prepare(filepath):
    IMG_SIZE = 220 # 50 in txt-based
    img_array = filepath
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))

    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)

@app.route('/index')
def index_page():
    return render_template('index.html')


@app.route('/predict_object/', methods=['GET', 'POST'])
def render_message():
    model = tf.keras.models.load_model('NIC-CNN.model')
    
    #Get image URL as input
    image_url = request.form['image_url']
    image = io.imread(image_url)
    print("#############################################################")
    print(image)
    
    prediction = model.predict([prepare(image)])
    print(prediction)  # will be a list in a list.
    print(CATEGORIES[int(prediction[0][0])])
    
    #Store model prediction results to pass to the web page
    message = "Model prediction: {}".format(CATEGORIES[int(prediction[0][0])])
    print('Python module executed successfully')
        
    #Return the model results to the web page
    return render_template('index.html',message=message, data=prediction[0][0]) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8001)
