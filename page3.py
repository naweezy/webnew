import streamlit as st

def page_3():
  st.markdown('<h1 style="text-align:center">Belajar Python</h1>', unsafe_allow_html=True)
  st.write("Menampilkan Halaman dari File MD (MarkDown)")
  
  with open('nama.md', 'r') as file:
      isi_teks = file.read()
      st.markdown(isi_teks)