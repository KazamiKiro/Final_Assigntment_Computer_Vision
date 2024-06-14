# pages/realtime_camera.py
import streamlit as st
import cv2
import numpy as np

def app():
    st.title("Realtime Camera")
    st.markdown('Turn on your camera and have fun!')

    run = st.checkbox('Run')
    effect = st.selectbox("Select effect", ["None", "Grayscale", "Blur", "Edge Detection", "Sepia", "Negative"])

    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image")
            break

        if effect == "Grayscale":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # Convert back to BGR for display
        elif effect == "Blur":
            frame = cv2.blur(frame, (5, 5))
        elif effect == "Edge Detection":
            frame = cv2.Canny(frame, 100, 200)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # Convert back to BGR for display
        elif effect == "Sepia":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.array(frame, dtype=np.float32)
            frame = cv2.transform(frame, np.matrix([[0.393, 0.769, 0.189],
                                                      [0.349, 0.686, 0.168],
                                                      [0.272, 0.534, 0.131]]))
            frame = np.array(frame, dtype=np.uint8)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        elif effect == "Negative":
            frame = cv2.bitwise_not(frame)

        FRAME_WINDOW.image(frame)

    cap.release()

if __name__ == "__main__":  # Fix: changed "__app__" to "__main__"
    app()