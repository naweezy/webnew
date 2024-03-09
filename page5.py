import streamlit as st

def page_5():
    st.markdown('<h1 style="text-align:center">Menghitung Luas Segitiga</h1>', unsafe_allow_html=True)
    alas = st.slider("Masukkan Nilai Alas", 0, 100)
    tinggi = st.slider("Masukkan Nilai Tinggi", 0, 100)
    hitung = st.button("Hitung Luas")

    if hitung :
        luas = 0.5 * alas * tinggi
        st.write("Luas Persegi Panjang adalah = ", luas)
        st.success(f"Luas Segitiga adalah = {luas}")