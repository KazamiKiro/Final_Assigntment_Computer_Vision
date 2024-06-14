import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import os

def detect_chili(image_path):
    model_path = "models/chili_detect.pt"
    model = YOLO(model_path)

    image = cv2.imread(image_path)
    results = model(image)
    
    obj_class = ["cabe hijau", "cabe merah", "cabe oranye"]
    colors = [(0, 255, 0), (0, 0, 255), (0, 140, 255)]  # Warna untuk tiap kelas
    
    for result in results:
        boxes = result.boxes.data  
        amount = len(boxes)
        
        for box in boxes:
            x1, y1, x2, y2, probs, label = box.tolist() 
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  
            probs = float(probs)
            
            color = colors[int(label)]
            image = cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            
            label_text = f'{obj_class[int(label)]} {probs:.2f}'
            image = cv2.putText(image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return image, amount

def detect_chili_real(image_input, output_dir='output'):
    model_path = "models/chili_detect.pt"
    model = YOLO(model_path)

    # Check if the input is a file path or a NumPy array
    if isinstance(image_input, str):
        image = cv2.imread(image_input)
    elif isinstance(image_input, np.ndarray):
        image = cv2.imdecode(image_input, cv2.IMREAD_COLOR) if image_input.ndim == 1 else image_input
    else:
        raise ValueError("Input must be a file path or a NumPy array.")
    
    results = model(image)
    
    obj_class = ["cabe hijau", "cabe merah", "cabe oranye"]
    colors = [(0, 255, 0), (0, 0, 255), (0, 140, 255)]  # Colors for each class
    
    for result in results:
        boxes = result.boxes.data
        amount = len(boxes)
        
        for box in boxes:
            x1, y1, x2, y2, probs, label = box.tolist()
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            probs = float(probs)
            
            color = colors[int(label)]
            image = cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            
            label_text = f'{obj_class[int(label)]} {probs:.2f}'
            image = cv2.putText(image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    # Extract filename and create the full output path
    if isinstance(image_input, str):
        filename = os.path.basename(image_input)
        output_path = os.path.join(output_dir, filename)
        os.makedirs(output_dir, exist_ok=True)
        cv2.imwrite(output_path, image)
    
    return image, amount