import streamlit as st
from PIL import Image

# Class untuk menangani Mood Pengguna
class MoodPengguna:
    def __init__(self, mood):  # Perbaiki dari _init menjadi __init__
        self.mood = mood

    def pesan_mood(self):
        if self.mood == "Fantastis!":
            return "Itu luar biasa! Terus sebarkan getaran baik itu! 😊"
        elif self.mood == "Bagus":
            return "Senang mendengarnya! Tetap positif dan terus bersinar. 🌞"
        elif self.mood == "Bisa lebih baik":
            return "Tetap bertahan! Hari-hari yang lebih baik akan datang. 🌟"
        else:
            return "Kami di sini untuk Anda. Lihat layanan kami untuk mendapatkan dukungan! 🙏"

# Judul dan ikon halaman
# st.set_page_config(page_title="Beranda Rumah Sakit", page_icon="🏥")

# Tampilan header dengan tema
st.title("Selamat datang di Rumah Sakit Citra Kasih! ^_~")
st.subheader("Kesehatan Anda, kebahagiaan kami! 🌟")

# Muat dan tampilkan gambar lucu bertema kesehatan
try:
    image = Image.open("dokter.png")  # Pastikan gambar ini ada di direktori yang benar
    st.image(image, caption="Tetap sehat dan bahagia!🌿")
except Exception as e:
    st.error(f"Gambar tidak dapat dimuat. Pastikan file 'dokter.png' ada. Error: {e}")

# Menampilkan kutipan kesehatan yang lucu menggunakan for loop
kutipan_kesehatan = [
    "Sebuah apel sehari membuat siapa pun menjauh, jika Anda membuangnya cukup keras! 🍎",
    "Jaga kebugaran tubuhmu, jangan biarkan penyakit merajalela! 💪",
    "Tertawa adalah obat terbaik, bahkan lebih baik dari vitamin! 😂"
]

# Iterasi dan tampilkan kutipan kesehatan menggunakan for
for kutipan in kutipan_kesehatan:
    st.write(f"Tip Kesehatan: {kutipan}")

# Tombol untuk informasi lebih lanjut
if st.button("Ketahui Lebih Lanjut Tentang Kami"):
    st.write(
        "Jelajahi beragam layanan kesehatan kami, mulai dari pemeriksaan umum hingga perawatan khusus."
    )

# Elemen interaktif untuk mood pengguna
st.header("Merasa Hebat Hari Ini?🌟")
user_mood = st.radio(
    "Beri tahu kami perasaan Anda:",
    ("Fantastis!", "Bagus", "Bisa lebih baik", "Butuh bantuan"),
)

# Menggunakan objek kelas untuk menangani mood dan menampilkan pesan
mood_objek = MoodPengguna(user_mood)
st.write(mood_objek.pesan_mood())

# Footer
st.markdown(
    "---\n*Hubungi kami kapan saja di [rumahsakitcitrakasih.com](mailto:support@rumahsakitcitrakasih.com)*"
)