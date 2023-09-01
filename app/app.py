## flask app to host cnn model

from flask import Flask, request, jsonify, render_template, make_response, redirect, url_for
from flask_cors import CORS
import numpy as np
import tensorflow as tf
import os
import json

# load model
model_version = '1.1'
model_path = os.path.join(os.getcwd(), 'saved_models', f'version_{model_version}')

model = tf.keras.models.load_model(model_path)

# load class names
CLASS_NAMES_PATH = os.path.join(os.getcwd(), 'CLASS_NAMES.json')
CLASS_NAMES = None

with open(CLASS_NAMES_PATH, 'r') as f:
    CLASS_NAMES = json.load(f)

# define prediction function
#image size 256x256

def predict(img):
    img = tf.image.resize(img, (256, 256))
    img = tf.expand_dims(img, axis=0)
    pred = model.predict(img)
    return pred

def result_format(pred):
    res = np.argmax(pred, axis=1)
    res = CLASS_NAMES[str(res[0])]
    confidence = round(100 * (np.max(pred)), 2)
    Sum = sum(pred[0])
    weights = [round(pred[0][0]/Sum, 4), round(pred[0][1]/Sum, 4), round(pred[0][2]/Sum, 4)]
    return jsonify({'prediction': res,
                    'status': 'success',
                    'confidence': confidence,
                    'weights': weights,
                    'code': 200,
                    'class_names': [CLASS_NAMES['0'], CLASS_NAMES['1'], CLASS_NAMES['2']]})

# define flask app

app = Flask(__name__)
CORS(app)

@app.route('/api/predict', methods=['POST'])
def predict_route():
    img = request.files['image']
    img = tf.io.decode_image(img.read(), channels=3)
    pred = predict(img)
   
    return result_format(pred)

@app.route('/predict', methods=['POST'])
def get_predict_route():
    img = request.files['image']
    img = tf.io.decode_image(img.read(), channels=3)
    pred = predict(img)
   
    result = result_format(pred).get_json()
    print(type(result))
    return render_template('index.html', prediction=result)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
            