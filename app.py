from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model only
model = pickle.load(open('breast_cancer_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', values={}, predict=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values (raw 1–10)
    features = [
        float(request.form['bare_nuclei']),
        float(request.form['uniformity_cell_size']),
        float(request.form['bland_chromatin']),
        float(request.form['normal_nucleoli'])
    ]
    
    # Predict directly
    prediction = model.predict([features])[0]
    result = "Malignant (Cancer)" if prediction == 1 else "Benign (No Cancer)"
    

# Pass back the submitted values so form repopulates
    return render_template('index.html', 
                          predict=result, 
                          values=request.form)

if __name__ == "__main__":
    app.run(debug=True)
