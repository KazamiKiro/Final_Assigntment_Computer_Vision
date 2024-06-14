# main.py
import streamlit as st

def main():

    st.title('Team A: MBKM Dago Engineering')
    st.write('*Computer Vision: 5 Pages of computer vision*')

    st.write("Our teams:")
    st.write("Angga, Andika, Windra, Marino, Yudhi")  # Add some space

    st.title("Our Expertise")
    st.write("We specialize in:")
    st.markdown("""
    - Image Processing
    - Realtime Camera
    - Image Detection
    - Object Detection
    - Object Segmentation
    """)

if __name__ == "__main__":
    main()