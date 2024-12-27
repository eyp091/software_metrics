import streamlit as st
import pickle
import numpy as np
from predict_cost import predict

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Kod Karmaşıklığı Tahmini",
    page_icon="💻",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        font-size: 3rem !important;
        color: #1E88E5;
        margin-bottom: 2rem;
    }
    .stHeader {
        color: #0D47A1;
        margin-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 2rem;
        background-color: #1E88E5;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Ana başlık
st.title("🔍 Kod Karmaşıklığı Tahmin Uygulaması")

# İki sütunlu layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Halstead Metrikleri")
    b = st.number_input("Halstead 'b' Değeri:", min_value=0.0, step=0.01, value=0.0, help="Program içindeki benzersiz operatör sayısı")
    v = st.number_input("Halstead 'v' Değeri:", min_value=0.0, step=0.01, value=0.0, help="Program hacmi")
    n = st.number_input("Halstead 'n' Değeri:", min_value=0, step=1, value=0, help="Toplam operatör ve operand sayısı")
    e = st.number_input("Halstead 'e' Değeri:", min_value=0.0, step=0.01, value=0.0, help="Program için gereken çaba")

with col2:
    st.subheader("🔢 Diğer Metrikler")
    total_Opnd = st.number_input("Toplam Operand Sayısı:", min_value=0, step=1, value=0)
    total_Op = st.number_input("Toplam Operatör Sayısı:", min_value=0, step=1, value=0)
    t = st.number_input("Halstead 't' Zaman Tahmini:", min_value=0.0, step=0.01, value=0.0)
    d = st.number_input("Halstead 'd' Zorluk Değeri:", min_value=0.0, step=0.01, value=0.0)

# Tahmin butonu için container
with st.container():
    if st.button("🚀 Tahmin Yap", use_container_width=True):
        try:
            # Progress bar ekleyelim
            with st.spinner('Tahmin yapılıyor...'):
                inputs = np.array([[b, v, n, total_Opnd, total_Op, e, t, d]])
                prediction = predict(inputs)
            
            # Sonuç kartı
            st.markdown("### 📝 Sonuç")
            if prediction[0] == 1:
                st.success("✅ Karmaşıklık Değerlendirmesi: Başarılı (Successful)")
                st.balloons()  # Başarılı sonuç için kutlama efekti
            else:
                st.error("⚠️ Karmaşıklık Değerlendirmesi: Düzenlenmeli (Redesign)")
                
        except Exception as e:
            st.error(f"❌ Bir hata oluştu: {e}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        💡 Bu uygulama, kod karmaşıklığını Halstead metrikleri kullanarak değerlendirir.
    </div>
""", unsafe_allow_html=True)