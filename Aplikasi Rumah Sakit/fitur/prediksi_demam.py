import streamlit as st

class PrediksiDemam:
    def __init__(self, sakit_kepala, lelah, batuk):
        self.sakit_kepala = sakit_kepala
        self.lelah = lelah
        self.batuk = batuk

    def prediksi(self):
        if self.sakit_kepala and self.lelah and self.batuk:
            return "Kemungkinan besar Anda demam. Segera periksa ke dokter.", "Gambar_1.png"
        elif self.sakit_kepala or self.lelah or self.batuk:
            return "Anda mungkin sedang tidak enak badan. Cobalah istirahat dan perhatikan gejalanya.", "Gambar_2.png"
        else:
            return "Anda tidak menunjukkan gejala demam. Tetap jaga kesehatan!", "Gambar_3.png"

st.title("Prediksi Demam")

num_cases = st.number_input("Berapa banyak set gejala yang ingin Anda masukkan?", min_value=1, max_value=5, value=1)

if "prediksi_dilakukan" not in st.session_state or len(st.session_state.prediksi_dilakukan) != num_cases:
    st.session_state.prediksi_dilakukan = [False] * num_cases
    st.session_state.sakit_kepala = [False] * num_cases
    st.session_state.lelah = [False] * num_cases
    st.session_state.batuk = [False] * num_cases

for i in range(num_cases):
    st.subheader(f"Set Gejala {i+1}")

    sakit_kepala = st.selectbox(f"Apakah Anda mengalami sakit kepala? (Set {i+1})", ("Pilih", "Ya", "Tidak")) == "Ya"
    lelah = st.selectbox(f"Apakah Anda merasa lelah? (Set {i+1})", ("Pilih", "Ya", "Tidak")) == "Ya"
    batuk = st.selectbox(f"Apakah Anda batuk? (Set {i+1})", ("Pilih", "Ya", "Tidak")) == "Ya"

    st.session_state.sakit_kepala[i] = sakit_kepala
    st.session_state.lelah[i] = lelah
    st.session_state.batuk[i] = batuk

    if st.button(f"Prediksi Set {i+1}"):
        st.session_state.prediksi_dilakukan[i] = True

i = 0
while i < num_cases:
    if st.session_state.prediksi_dilakukan[i]:  
        sakit_kepala = st.session_state.sakit_kepala[i]
        lelah = st.session_state.lelah[i]
        batuk = st.session_state.batuk[i]

        prediksi_objek = PrediksiDemam(sakit_kepala, lelah, batuk)
        hasil_prediksi, image_file = prediksi_objek.prediksi()

        st.success(hasil_prediksi)
        st.image(image_file, caption=f"Hasil Prediksi Set {i+1}", width=250)
        
        i += 1
    else:
        break
