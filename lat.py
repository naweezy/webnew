import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.write("Coding Club 2024")
df = pd.DataFrame({
  'No': [1, 2, 3, 4],
  'Nama' : ['Mama','Bapak','Adek','Nurul'],
  'Usia' : [47, 48, 14, 18]
})

df