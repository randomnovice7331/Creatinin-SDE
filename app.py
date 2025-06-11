import streamlit as st
from PIL import Image


# 1) Širi layout ako već nisi
st.set_page_config(layout="wide")
st.title("Modeling Creatinine in Chronic kidney disease (SDE project)")


# Lista točnih naziva tvojih slika
# 2) Učitaj slike
img1 = Image.open("Fig1_1200.webp")
img2 = Image.open("Fig2_2000.webp")
img3 = Image.open("Fig3_1800.webp")
img4 = Image.open("Fig4_1800.webp")

# 3) Prva slika manja
st.subheader("Creatinin: raw data")
st.image(img1, caption="", width=400)

# razmak
st.markdown("<br>", unsafe_allow_html=True)




# 4) Druga slika veća
st.subheader("Plot of data and simulation")
st.image(img2, caption="", width=1000)


# razmak
st.markdown("<br><br>", unsafe_allow_html=True)





# 5) Treća slika veća
st.subheader("Form of the model and meaning of symbols")
st.image(img3, caption="", width=1000)


# razmak
st.markdown("<br><br>", unsafe_allow_html=True)


# 6) Četvrta slika veća
st.subheader("Statistical test for residuals and estimation of error")
st.image(img4, caption="", width=1000)


# razmak
st.markdown("<br><br>", unsafe_allow_html=True)





