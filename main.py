import streamlit as st
import pandas as pd

st.title("Hello World")

st.sidebar.title("Sidebar")

choice = st.sidebar.selectbox("Choose your site",["Seite1","Seite2","Seite3"])


if choice == "Seite1":
    st.write("Seite1")
    st.image("https://medien.umbreitkatalog.de/bildzentrale_original/978/384/019/4429.jpg")
    file = st.file_uploader("Put file here")
    st.date_input("Date please")
if choice == "Seite2":
    st.write("Seite2")
    st.map()