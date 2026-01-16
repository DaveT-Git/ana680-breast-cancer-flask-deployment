# Breast Cancer Prediction App

Flask web application that predicts breast cancer (benign/malignant) using the UCI Wisconsin dataset.

## Important Disclaimer

**This project is for educational and demonstration purposes only.**

The breast cancer prediction model is built using the public UCI Wisconsin Breast Cancer dataset and a simple Random Forest classifier. It achieves high test accuracy (~0.96) in controlled experiments but is **not** a medical diagnostic tool, has **not** been clinically validated, and should **never** be used for real health decisions.

- Predictions are based on limited features and synthetic/test data patterns — they do **not** replace professional medical advice, screening (e.g., mammograms, biopsies), or consultation with a qualified healthcare provider.
- False positives/negatives are possible, and real-world performance could differ significantly.
- Always consult a doctor or oncologist for any health concerns related to breast cancer.

This app is an academic exercise in ML deployment (Flask + Heroku) and is **not** intended for clinical, diagnostic, or therapeutic use.

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
