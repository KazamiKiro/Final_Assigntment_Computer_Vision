# pages/object_segmentation.py
import streamlit as st
import cv2
import numpy as np
from computer_vision.chili_segment import segment_chili
    

def main():
    st.title("Object Segmentation")
    st.markdown('Turn on your camera first then we can detect the chilis!')

    run = st.checkbox('Run')

    if 'counts' not in st.session_state:
        st.session_state.counts = []

    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image")
            break
        frame, amount = segment_chili(frame)
        
        st.session_state.counts.append(amount)

        FRAME_WINDOW.image(frame, channels="BGR")
    cap.release()

if __name__ == "__main__":
    main()
