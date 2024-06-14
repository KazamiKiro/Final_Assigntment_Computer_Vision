# pages/image_detection.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from computer_vision.chili_detect import detect_chili
import os

# Fungsi untuk testing
def main():
    st.title('Chili Pepper Detection App')
    st.markdown('Upload an image and detect chili peppers!')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        temp_image_path = 'temp_image.jpg'
        with open(temp_image_path, 'wb') as f:
            f.write(uploaded_file.getvalue())

        # Perform detection
        image, num_chilies = detect_chili(temp_image_path)

        # Convert BGR image to RGB for Streamlit display
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Display the image with detection results
        st.image(image_rgb, caption=f'Detected {num_chilies} chili peppers', use_column_width=True)

if __name__ == '__main__':
    main()
