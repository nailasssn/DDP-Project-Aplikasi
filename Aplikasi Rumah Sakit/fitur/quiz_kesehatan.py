import streamlit as st

# Judul aplikasi
st.title("Quiz Kesehatan")

# image
st.image("quiz1.png", caption="Tetap sehat dan bahagia!🌿")

# Class untuk mengelola kuis
class Quiz:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.user_answers = []

    def add_question(self, question, options, correct_answer):
        self.questions.append({"question": question, "options": options, "correct_answer": correct_answer})

    def display_questions(self):
        for i, q in enumerate(self.questions):
            st.subheader(f"{i + 1}. {q['question']}")
            answer = st.radio("Pilih jawaban:", q['options'], key=f"q{i+1}")
            self.user_answers.append(answer)

    def evaluate(self):
        score =  0
        for i, q in enumerate(self.questions):
            if self.user_answers[i] == q['correct_answer']:
                score += 1
                st.success(f"Jawaban untuk pertanyaan {i + 1} benar!")
            else:
                st.error(f"Jawaban untuk pertanyaan {i + 1} salah. Jawaban yang benar adalah '{q['correct_answer']}'.")
        return score

# Fungsi untuk menjalankan kuis
def run_quiz():
    quiz = Quiz()

    # Tambahkan pertanyaan ke dalam kuis
    quiz.add_question(
        "Berapa lama waktu tidur yang disarankan untuk orang dewasa setiap malam?",
        ["4-5 jam", "6-8 jam", "9-10 jam", "11-12 jam"],
        "6-8 jam",
    )
    quiz.add_question(
        "Berapa banyak air yang sebaiknya dikonsumsi setiap hari?",
        ["1 liter", "2 liter", "3 liter", "4 liter"],
        "2 liter",
    )
    quiz.add_question(
        "Makanan apa yang harus dikurangi untuk menjaga kesehatan jantung?",
        ["Buah-buahan", "Sayuran", "Makanan tinggi garam", "Makanan kaya serat"],
        "Makanan tinggi garam",
    )

    # Tampilkan pertanyaan
    quiz.display_questions()

    # Tombol submit untuk evaluasi
    if st.button("Submit Jawaban"):
        score = quiz.evaluate()

        # Tampilkan skor akhir
        st.write(f"Skor akhir kamu: {score}/{len(quiz.questions)}")

        if score == len(quiz.questions):
            st.balloons()
            st.success("Luar biasa! Kamu sangat paham tentang kesehatan.", icon="🎉")
        elif score >= len(quiz.questions) // 2:
            st.info("Bagus! Tapi masih ada yang perlu diperbaiki.", icon="😍")
        else:
            st.warning("Kamu perlu belajar lebih banyak tentang kesehatan.", icon="🤔")



# Deskripsi aplikasi
st.write("Jawab pertanyaan berikut untuk menguji pengetahuanmu tentang kesehatan.")

# Jalankan kuis
run_quiz()

