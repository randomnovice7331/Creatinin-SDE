import streamlit as st
from PIL import Image

# Lista točnih naziva tvojih slika
images = [
    "Fig1_1200.webp",
    "Fig2_2000.webp",
    "Fig3_1800.webp",
    "Fig4_1800.webp"
]
captions = [
    "Creatinin: raw data",
    "Plot of data and simulation",
    "Form of the model and meaning of symbols",
    "Statistical test for residuals and estimation of error"
]

st.title("Modeling Creatinine concentration in the blood for a chronic kidney disease patient (SDE project)")
for path, cap in zip(images, captions):
    img = Image.open(path)
    st.image(img, caption=cap, use_container_width=True)
