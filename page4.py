import streamlit as st

def page_4():
    st.markdown('<h1 style="text-align:center">Menghitung Luas Persegi Panjang</h1>', unsafe_allow_html=True)
    panjang = st.number_input("Masukkan Nilai Panjang", 0)
    lebar = st.number_input("Masukkan Nilai Lebar", 0)
    hitung = st.button("Hitung Luas")

    if hitung :
        luas = panjang * lebar
        st.write("Luas Persegi Panjang adalah = ", luas)
        st.success(f"Luas Persegi Panjang adalah = {luas}")