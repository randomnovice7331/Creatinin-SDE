import streamlit as st
from PIL import Image

# ── 1. PAGE CONFIG: jedini prvi Streamlit poziv ────────────────────────────────  
st.set_page_config(
    page_title="Modeling Creatinine in CKD (SDE project)",
    layout="wide",
)

# ── 2. CSS za centriranje (može odmah nakon set_page_config) ───────────────────  
st.markdown(
    """
    <style>
      /* Centriramo glavni container */
      .css-18e3th9 {
        display: flex !important;
        flex-direction: column;
        align-items: center;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── 3. Naslov ───────────────────────────────────────────────────────────────────  
st.title("Modeling Creatinine in Chronic Kidney Disease (SDE project)")

# ── 4. Učitavanje slika ────────────────────────────────────────────────────────  
img1 = Image.open("Fig1_1200.webp")
img2 = Image.open("Fig2_2000.webp")
img3 = Image.open("Fig3_1800.webp")
img4 = Image.open("Fig4_1800.webp")

# ── 5. Prikaz slika s različitim veličinama i razmacima ─────────────────────────  
st.subheader("Fig 1: Creatinin: raw data")
st.image(img1, caption="", width=400)    # manja prva slika
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Fig 2: Plot of data and simulation")
st.image(img2, caption="", width=1000)   # veća druga slika
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("Fig 3: Form of the model and meaning of symbols")
st.image(img3, caption="", use_column_width=True)
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("Fig 4: Statistical test for residuals and estimation of error")
st.image(img4, caption="", use_column_width=True)
st.markdown("<br><br>", unsafe_allow_html=True)
