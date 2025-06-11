import streamlit as st
from PIL import Image


st.markdown(
    """
    <style>
      /* Uzmi glavni container i centriraj sve elemente */
      .css-18e3th9 {            /* klasa se može mijenjati s promjenama Streamlit-a */
        display: flex;
        flex-direction: column;
        align-items: center;
      }
    </style>
    """,
    unsafe_allow_html=True,
)



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
st.image(img1, caption="", use_column_width=True)

# razmak
st.markdown("<br>", unsafe_allow_html=True)




# 4) Druga slika veća
st.subheader("Plot of data and simulation")
st.image(img2, caption="", use_column_width=True)


# razmak
st.markdown("<br><br>", unsafe_allow_html=True)





# 5) Treća slika veća
st.subheader("Form of the model and meaning of symbols")
st.image(img3, caption="", use_column_width=True)


# razmak
st.markdown("<br><br>", unsafe_allow_html=True)


# 6) Četvrta slika veća
st.subheader("Statistical test for residuals and estimation of error")
st.image(img4, caption="", use_column_width=True)


# razmak
st.markdown("<br><br>", unsafe_allow_html=True)





