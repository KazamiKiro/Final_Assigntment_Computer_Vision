import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def chart(data):
    # Membuat plot garis
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data, marker='o', linestyle='-', color='b')

    # Menambahkan judul dan label pada sumbu
    ax.set_title('Diagram Deteksi Cabai')
    ax.set_xlabel('Gambar')
    ax.set_ylabel('Jumlah cabai yang Dideteksi')

    # Menambahkan grid
    ax.grid(True)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)