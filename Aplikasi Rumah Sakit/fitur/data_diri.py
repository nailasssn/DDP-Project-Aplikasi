import streamlit as st
import pickle
import os

# Fungsi validasi input
def validasi_input(nama, email, pesan):
    if not nama or not email or not pesan:
        return False, "Semua kolom harus diisi."
    return True, ""

# Kelas Guest untuk menyimpan data tamu
class Guest:
    def __init__(self, nama, email, pesan):
        self.nama = nama
        self.email = email
        self.pesan = pesan

    def display_info(self):
        return f"Nama: {self.nama}, Email: {self.email}, Pesan: {self.pesan}"

# Fungsi untuk menyimpan daftar tamu ke file
def save_guests_to_file(guests_list, filename='guests.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(guests_list, file)

# Fungsi untuk memuat daftar tamu dari file
def load_guests_from_file(filename='guests.pkl'):
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (pickle.UnpicklingError, AttributeError):
            os.remove(filename)
            return []
    return []

# Memuat daftar tamu dari file
guests_list = load_guests_from_file()

# Fungsi untuk menambahkan tamu baru
def add_guest(nama, email, pesan):
    new_guest = Guest(nama, email, pesan)
    guests_list.append(new_guest)
    # save_guests_to_file(guests_list)

# Fungsi untuk menampilkan daftar tamu
def display_guests():
    if guests_list:
        for guest in guests_list:
            st.write(guest.display_info())
    else:
        st.write("Belum ada tamu.")

# Streamlit UI
st.title("Buku Tamu Digital")
st.subheader("Isi Data Kamu")

# Input data tamu
nama = st.text_input("Nama")
email = st.text_input("Email")
pesan = st.text_input("Keluhan")

if st.button("Kirim"):
    is_valid, message = validasi_input(nama, email, pesan)
    if is_valid:
        add_guest(nama, email, pesan)
        st.success("Tamu berhasil ditambahkan.")
        st.subheader("Daftar Tamu")
        display_guests()      # Tampilkan daftar tamu langsung setelah penambahan
    else:
        st.error(message)
else:
    st.subheader("Daftar Tamu")
    display_guests()
