import streamlit as st

# CSS to Streamlit 
st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
        background-color: #E3AFBC;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #9A1750; 
        color: white;
        padding: 5px;
    }

    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: black;
        font-size: 16px;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Side bar direktory
data_diri = st.Page("./fitur/data_diri.py", title="data diri")
prediksi_demam = st.Page("./fitur/prediksi_demam.py", title="prediksi demam")
quiz_kesehatan = st.Page("./fitur/quiz_kesehatan.py", title="quiz kesehatan")
rumah_sakit = st.Page("./fitur/rumah_sakit.py", title="rumah sakit")

pg = st.navigation(
    {
        "Menu Utama":[rumah_sakit], #""(key), [](value)
        "Menu":[data_diri, prediksi_demam, quiz_kesehatan],
    }
)

pg.run()

