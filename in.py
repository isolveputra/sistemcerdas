import streamlit as st

# Judul aplikasi
st.title("💻 Sistem Rekomendasi Laptop Sederhana")
st.write("Sistem Cerdas berbasis Rule (IF-ELSE)")

# Input user
budget = st.selectbox(
    "Pilih Budget Anda:",
    ["< 5 juta", "5 - 10 juta", "> 10 juta"]
)

kebutuhan = st.selectbox(
    "Pilih Kebutuhan:",
    ["Office", "Desain Grafis", "Gaming"]
)

# Proses (Rule-based system)
def rekomendasi_laptop(budget, kebutuhan):
    if budget == "< 5 juta":
        if kebutuhan == "Office":
            return "Rekomendasi: Laptop entry-level (RAM 4GB, SSD 256GB)"
        else:
            return "Budget kurang untuk kebutuhan ini 😅"
    
    elif budget == "5 - 10 juta":
        if kebutuhan == "Office":
            return "Rekomendasi: Laptop mid-range (RAM 8GB, SSD)"
        elif kebutuhan == "Desain Grafis":
            return "Rekomendasi: Laptop dengan GPU ringan (MX series)"
        else:
            return "Kurang optimal untuk gaming berat"
    
    elif budget == "> 10 juta":
        if kebutuhan == "Gaming":
            return "Rekomendasi: Laptop gaming (RTX series 🔥)"
        elif kebutuhan == "Desain Grafis":
            return "Rekomendasi: Laptop high-end (GPU kuat, RAM 16GB)"
        else:
            return "Rekomendasi: Laptop premium untuk office"

# Tombol proses
if st.button("Dapatkan Rekomendasi"):
    hasil = rekomendasi_laptop(budget, kebutuhan)
    st.success(hasil)
