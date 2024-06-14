# pages/image_processing.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image

def main():
    st.title("Image Processing")
    st.markdown('Upload your image first, then you can apply effect')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        effect = st.selectbox("Select an effect:", ["Grayscale", "Flip Horizontally", "Rotate 90 degrees", "Blur", "Edge Detection", "Thresholding", "Sepia", "Cartoon"])

        if effect == "Grayscale":
            processed_image = np.array(image.convert('L'))
            st.image(processed_image, caption='Grayscale Image.', use_column_width=True)
        elif effect == "Flip Horizontally":
            processed_image = np.array(image.transpose(Image.FLIP_LEFT_RIGHT))
            st.image(processed_image, caption='Flipped Image.', use_column_width=True)
        elif effect == "Rotate 90 degrees":
            processed_image = np.array(image.rotate(90))
            st.image(processed_image, caption='Rotated Image.', use_column_width=True)
        elif effect == "Blur":
            processed_image = cv2.blur(np.array(image), (5, 5))
            st.image(processed_image, caption='Blurred Image.', use_column_width=True)
        elif effect == "Edge Detection":
            processed_image = cv2.Canny(np.array(image), 100, 200)
            st.image(processed_image, caption='Edge Detected Image.', use_column_width=True)
        elif effect == "Thresholding":
            processed_image = cv2.threshold(np.array(image), 127, 255, cv2.THRESH_BINARY)[1]
            st.image(processed_image, caption='Thresholded Image.', use_column_width=True)
        elif effect == "Sepia":
            processed_image = np.array(image)
            processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
            processed_image = np.array(processed_image) / 255
            processed_image = cv2.transform(processed_image, np.matrix([[0.393, 0.769, 0.189],
                                                                        [0.349, 0.686, 0.168],
                                                                        [0.272, 0.534, 0.131]]))
            processed_image = np.array(processed_image * 255, dtype=np.uint8)
            st.image(processed_image, caption='Sepia Image.', use_column_width=True)
        elif effect == "Cartoon":
            processed_image = np.array(image)
            processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
            processed_image = cv2.medianBlur(processed_image, 5)
            gray = cv2.cvtColor(processed_image, cv2.COLOR_RGB2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.Laplacian(gray, cv2.CV_8U)
            processed_image = cv2.cvtColor(processed_image, cv2.COLOR_RGB2BGR)
            processed_image = cv2.bitwise_and(processed_image, processed_image, mask=edges)
            st.image(processed_image, caption='Cartoon Image.', use_column_width=True)

        st.write("Original Image:")
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("Processed Image:")
        st.image(processed_image, caption=f'{effect} Image.', use_column_width=True)

if __name__ == "__main__":
    main()