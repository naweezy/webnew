import streamlit as st

def page_4():
  st.title("Menghitung Luas Persegi Panjang")

panjang = st.number_input("Masukkan Nilai Panjang", 0)
lebar = st.number_input("Masukkan Nilai Lebar", 0)
hitung = st.button("Hitung Luas")

if hitung :
    luas = panjang * lebar
    st.write("Luas Persegi Panjang adalah = ", luas)
    st.success(f"Luas Persegi Panjang adalah = {luas}")