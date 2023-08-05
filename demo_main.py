"""
Файл с кодом фронта
"""
import streamlit as st
from qr_generating import generate_simple_qr_by_url

st.markdown(
    """
    Демо генератора QR-кодов.
    """)


def gen_button_handler():
    if a := st.text_input('Enter some text'):
        img = generate_simple_qr_by_url(a)
        st.image(img)


gen_button_handler()
