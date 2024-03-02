import streamlit as st
# import pandas as pd
#import matplotlib.pyplot as plt

# st.write("Infinity Coding Club 2024")
# df = pd.DataFrame({
#   'No': [1, 2, 3, 4],
#   'Nama' : ['Mama','Bapak','Adek','Nurul'],
#   'Usia' : [47, 48, 14, 18]
# })

# df

def page_1():
  st.title("Halaman 1")
  st.write("Halaman untuk Intro")
def page_2():
  st.title("Halaman 2")
  st.write("Halaman untuk Menampilkan Youtube")
def page_3():
  st.title("Halaman 3")
  st.write("Halaman untuk Rumus MTK")
  
PAGES = {
  "Page 1" : page_1,
  "Page 2" : page_2,
  "Page 3" : page_3
}

st.sidebar.image("foto1.png", width=100)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()