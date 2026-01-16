# Breast Cancer Prediction App

Flask web application that predicts breast cancer (benign/malignant) using the UCI Wisconsin dataset.

## Features Used
- Bare Nuclei
- Uniformity of Cell Size
- Bland Chromatin
- Normal Nucleoli

## Model
- Random Forest Classifier (n_estimators=200)
- Test Accuracy: ~0.959

Run the application:

`python app.py`

Open: http://127.0.0.1:5000


## Deployment

**Live URL:**  
https://breast-cancer-predict-djt-37fdafeb6e27.herokuapp.com/

**Note:** The app is hosted on a Heroku Eco dyno, so the first load after inactivity may take 10–30 seconds while it wakes up.

### Screenshots

#### 1. Input Form (empty state)
<img width="472" height="409" alt="Screenshot 2026-01-16 at 10 26 21 AM" src="https://github.com/user-attachments/assets/b747db27-069e-4a60-aad1-e286159043fc" />

The main interface where users enter values (1–10 scale) for the four selected features.

#### 2. Form with Prediction Result
<img width="483" height="443" alt="Breast Cancer Prediction web form showing input fields for Bare Nuclei, Uniformity of Cell Size, Bland Chromatin, and Normal Nucleoli, with a Predict button" src="https://github.com/user-attachments/assets/8374283d-ec5e-41c8-acdc-cda1a0ef37a0" />

Example after submitting values — the prediction appears below the form (here showing a benign result).
