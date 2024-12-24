import streamlit as st
import pickle
import numpy as np
from predict_cost import predict

st.title("Kod Karmaşıklığı Tahmin Uygulaması")
st.write("----------------------------------")

st.header("Giriş Verilerini Girin")
input_1 = st.number_input("Kod İçinde Bulunan Toplam Metod Sayısı:", min_value=-1000, max_value=1000, step=1, value=0)
input_2 = st.number_input("Kod İçinde Bulunan Karşılaştırma Operatörlerinin Sayısı:", min_value=-1000, max_value=1000, step=1, value=0)
input_3 = st.number_input("Kod İçinde Kullanılan Benzersiz Kelimelerin Sayısı:", min_value=-1000, max_value=1000, step=1, value=0)
input_4 = st.number_input("Kod İçinde İç İçe Geçmiş Blokların Sayısı:", min_value=-1000, max_value=1000, step=1, value=0)
input_5 = st.number_input("Kod Bloğunda Yer Alan 'return' Sayısı:", min_value=-1000, max_value=1000, step=1, value=0)

if st.button("Tahmin Yap"):
    try:
        inputs = np.array([[input_1, input_2, input_3, input_4, input_5]])
        
        prediction = predict(inputs)
        
        st.success(f"Model Tahmini: {prediction[0]}")
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
