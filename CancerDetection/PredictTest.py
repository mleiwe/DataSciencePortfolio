"""
This notebook is designed to test the predict.py script
"""
import requests
url = 'http://localhost:9696/predict'

# Cell JSON to input
cell = {
    "radius_mean": 17.99,
    "texture_mean": 10.38,
    "perimeter_mean": 122.80, 
    "area_mean": 1001.0,
    "smoothness_mean": 0.11840,
    "compactness_mean": 0.27760,
    "concavity_mean": 0.30010, 
    "concave points_mean": 0.14710,
    "symmetry_mean": 0.2419,
    "fractal_dimension_mean": 0.07871,
    "radius_se":  1.095,
    "texture_se": 0.9053,
    "perimeter_se": 8.589,
    "area_se": 153.4,
    "smoothness_se": 0.006399,
    "compactness_se": 0.04904,
    "concavity_se": 0.05373,
    "concave points_se": 0.0158,
    "symmetry_se":  0.03003,
    "fractal_dimension_se": 0.006193,
    "radius_worst": 25.38,
    "texture_worst": 17.33,
    "perimeter_worst": 184.6,
    "area_worst": 2019.0,
    "smoothness_worst": 0.1622,
    "compactness_worst": 0.6656,
    "concavity_worst": 0.7119,
    "concave points_worst": 0.2654,
    "symmetry_worst": 0.4601,
    "fractal_dimension_worst": 0.11890
}

response = requests.post(url, json=cell).json()

if response['Cell Diagnosis'] == 'Malignant':
    print("Cancerous Cell Detected")
else:
    print("Normal cell detected")