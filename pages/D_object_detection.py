# pages/object_detection.py
import streamlit as st
import cv2
import numpy as np
from computer_vision.chili_detect import detect_chili_real

def main():
    st.title("Object Detection")
    st.markdown('Turn on your camera first then we can detect the chilis!')

    toggleOn = st.checkbox('run')

    # Initialize counts in session_state if not present
    if 'counts' not in st.session_state:
        st.session_state.counts = []

    # Initialize camera status
    if 'fstStart' not in st.session_state:
        st.session_state.fstStart = True
    
    if toggleOn:
        st.session_state.fstStart = False
        cap = cv2.VideoCapture(0)
        # Check if the camera opened successfully
        if not cap.isOpened():
            st.error("Tidak dapat membuka kamera.")
            return
        
        # Container to display the frame
        frame_container = st.empty()
        # Loop to display frames from the camera
        while True:
            # Read frame from the camera
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detect chili
            frame, detection_counts = detect_chili_real(frame)
            print(detection_counts)
            st.session_state.counts.append(detection_counts)
            
            # Display the frame
            frame_container.image(frame, channels="BGR")
            
    elif not toggleOn and not st.session_state.fstStart:
        st.session_state.fstStart = True
        # Calculate total detected chilies
        print(st.session_state.counts)
        # Optionally draw a chart
        # draw_line_chart(st.session_state.counts)

if __name__ == "__main__":
    main()
