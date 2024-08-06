from flask import Flask, request, render_template
import pickle  # Assuming you saved your model using pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.sav', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [
            float(request.form['u_q']),
            float(request.form['coolant']),
            float(request.form['stator_winding']),
            float(request.form['u_d']),
            float(request.form['stator_tooth']),
            float(request.form['i_d']),
            float(request.form['i_q']),
            float(request.form['pm']),
            float(request.form['stator_yoke']),
            float(request.form['ambient']),
            float(request.form['torque'])
        ]
        
        # Make prediction
        prediction = model.predict([features])[0]
        
        return f'Predicted Motor Speed: {prediction:.2f}'
    except KeyError as e:
        return f'Missing form field: {str(e)}', 400
    except Exception as e:
        return f'An error occurred: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
