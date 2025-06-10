import streamlit as st
from PIL import Image

# Lista točnih naziva tvojih slika
images = [
    "1 creatinine_data_with_caption.png",
    "2 plot_of_data_and_simulation_with_caption.png",
    "3 combinedFig3.png",
    "4 fig4.png"
]
captions = [
    "Kreatinin: vremenski niz",
    "Podaci i simulacija",
    "Model i objašnjenje simbola",
    "Statistička provjera reziduala i prosječne greške"
]

st.title("Modeliranje kreatinina u krvi (SDE projekt)")
for path, cap in zip(images, captions):
    img = Image.open(path)
    st.image(img, caption=cap, use_container_width=True)
