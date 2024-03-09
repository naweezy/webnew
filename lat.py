import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4
from page5 import page_5
from image1 import main

# import pandas as pd
#import matplotlib.pyplot as plt

# st.write("Infinity Coding Club 2024")
# df = pd.DataFrame({
#   'No': [1, 2, 3, 4],
#   'Nama' : ['Mama','Bapak','Adek','Nurul'],
#   'Usia' : [47, 48, 14, 18]
# })

# df
  
PAGES = {
  "Profile Enhypen" : page_1,
  "Lagu Enhypen" : page_2,
  "Belajar Python" : page_3,
  "Kalkulator Luas P2" : page_4,
  "Kalkulator Luas Segitiga" : page_5,
  "Image Processing" : main
  }

st.sidebar.image("image1.png", width=100)
page = st.sidebar.radio("Nurul Azisa", list(PAGES.keys()))
PAGES[page]()

st.markdown(
  """
        <style>
        [data-testid]="stActionButtonIcon"] {
          display: none;
        }  
        [data-testid="baseButton-header"] {
          display: none;
        }
        
        </style>
        """,
  unsafe_allow_html=True,
)