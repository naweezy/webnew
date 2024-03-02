import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
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
  "Page 1" : page_1,
  "Page 2" : page_2,
  "Page 3" : page_3
}

st.sidebar.image("image1.png", width=100)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()