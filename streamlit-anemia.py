import pickle
import streamlit as st

anemia_model =  pickle.load(open('anemia_model.sav', 'rb'))

st.title('Prediksi Penyakit Anemia')

col1, col2 = st.columns(2)

with col1:
    Gender = st.text_input('Jenis Kelamin')
with col1:
    Hemoglobin = st.text_input('Masukan Jumlah protein dalam sel darah merah')
with col1:
    MCH = st.text_input('Masukan jumlah rata-rata di setiap sel darah merah')
with col2:
    MCHC = st.text_input('masukan ukuran konsentrasi rata-rata hemoglobin')
with col2:
    MCV = st.text_input('masukan rata-rata sel darah merah')
anemia_diagnosis = ''

if st.button('Test Prediksi'):
    ane_prediction = anemia_model.predict([[Gender, Hemoglobin, MCH, MCHC, MCV]])
    
    if(ane_prediction[0] == 1):
        anemia_diagnosis = 'Passien Terjangkit anemia'
    else :
        anemia_diagnosis = 'Passien Tidak Terjangkit anemia'

    st.success(anemia_diagnosis)
