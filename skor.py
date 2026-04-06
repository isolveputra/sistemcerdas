import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sistem Rekomendasi Karir IT", layout="wide")

st.title("🧠 Intelligent Career Recommendation System")
st.write("Berbasis Scoring + Rule-Based System")

# =========================
# INPUT USER
# =========================
st.sidebar.header("Input Profil Anda")

minat = st.sidebar.selectbox("Minat Utama", 
                            ["Programming", "Desain", "Data", "Jaringan"])

logika = st.sidebar.slider("Kemampuan Logika", 1, 10, 5)
kreativitas = st.sidebar.slider("Kreativitas", 1, 10, 5)
komunikasi = st.sidebar.slider("Komunikasi", 1, 10, 5)

kerja = st.sidebar.radio("Preferensi Kerja", 
                         ["Remote", "Office", "Flexible"])

# =========================
# KNOWLEDGE BASE (RULE)
# =========================
def hitung_skor():
    skor = {
        "Software Engineer": 0,
        "Data Scientist": 0,
        "UI/UX Designer": 0,
        "Network Engineer": 0
    }

    # Rule Minat
    if minat == "Programming":
        skor["Software Engineer"] += 3
    elif minat == "Data":
        skor["Data Scientist"] += 3
    elif minat == "Desain":
        skor["UI/UX Designer"] += 3
    elif minat == "Jaringan":
        skor["Network Engineer"] += 3

    # Rule Skill
    skor["Software Engineer"] += logika * 0.5
    skor["Data Scientist"] += logika * 0.7
    skor["UI/UX Designer"] += kreativitas * 0.8
    skor["Network Engineer"] += logika * 0.6

    skor["UI/UX Designer"] += komunikasi * 0.5
    skor["Data Scientist"] += komunikasi * 0.3

    # Rule Preferensi
    if kerja == "Remote":
        skor["Software Engineer"] += 2
        skor["Data Scientist"] += 2
    elif kerja == "Office":
        skor["Network Engineer"] += 2

    return skor

# =========================
# PROCESS
# =========================
if st.button("🔍 Analisis Karir"):
    skor = hitung_skor()

    df = pd.DataFrame(list(skor.items()), columns=["Karir", "Skor"])
    df = df.sort_values(by="Skor", ascending=False)

    st.subheader("📊 Hasil Analisis")
    st.dataframe(df)

    st.subheader("📈 Visualisasi Skor")
    st.bar_chart(df.set_index("Karir"))

    # Output utama
    terbaik = df.iloc[0]["Karir"]
    st.success(f"🎯 Rekomendasi Karir Anda: {terbaik}")

    # Explainable AI sederhana
    st.subheader("🧾 Penjelasan")
    st.write(f"Berdasarkan minat '{minat}', kemampuan logika {logika}, "
             f"kreativitas {kreativitas}, dan preferensi kerja '{kerja}', "
             f"sistem merekomendasikan karir **{terbaik}**.")
