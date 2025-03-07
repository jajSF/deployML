from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load('model.joblib')

class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

@app.get('/')
def reed_root():
    return {'message':'Iris model API'}

@app.get('/predict')
def predict(data: dict):
    """
    Predict the class of a give set of features. 

    Args:
        data (dict): A dictionary containing the features to predict.
        eg. {"features": [5.1, 3.5, 1.4, 0.2]}

    Returns:
        dict: A dictionary containing the predicted class.
    """
    features = np.array(data['features'].reshape(1, -1))
    prediction = model.predict(features)
    class_name = class_names[prediction][0] 
    return {'predicted_class': class_name}
 