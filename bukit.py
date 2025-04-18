import streamlit as st
import pandas as pd

# --- Title ---
st.title("Analisis Penutupan Perpustakaan Bukit Merah")

# --- Load Data ---
st.header("📥 Data Asal")

df1 = pd.read_csv('Bukit Merah.csv')  # pastikan fail ni ada dalam repo yang sama
df2 = pd.read_csv('Data Sebab Bukit Merah.csv')

# --- Gabung Data ---
data = pd.merge(df1, df2, on='Bil', how='inner')

# Gabung kolum Kunjungan
data['Kunjungan'] = data['Kunjungan_x']
data.drop(['Kunjungan_x', 'Kunjungan_y'], axis=1, inplace=True)

# Buang kolum Sebab3
if 'Sebab3' in data.columns:
    data.drop('Sebab3', axis=1, inplace=True)

# --- Info Asas ---
st.subheader("🔎 Ringkasan Data")
st.write("Jumlah responden:", data.shape[0])
st.dataframe(data)

# --- Nilai Hilang ---
st.subheader("📌 Nilai Kosong")
st.write(data.isnull().sum())

# --- Statistik Kolum Terpilih ---
st.subheader("📊 Statistik Kolum Utama")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Pendapat Penutupan**")
    st.write(data['Pendapat_penutupan'].value_counts())
    st.write(data['Pendapat_penutupan'].describe())

with col2:
    st.markdown("**Jarak ke Perpustakaan**")
    st.write(data['Jarak'].describe())


# --- Kolum Kategori Lain ---
st.subheader("📋 Statistik Kolum Kategori Lain")

kategori = ['Operasi', 'Strategik']
for col in kategori:
    st.markdown(f"**{col}**")
    st.write(data[col].describe())

st.markdown(""" Operasi = Adakah pengguna ingin melihat perpustakaan desa ini terus beroperasi?
Y = Ya
T = Tidak

Strategik = Adakah lokasi perpustakaan strategik dan mudah dikunjung?
Y = Ya
T = Tidak
""")

# --- Visualization (optional) ---
st.subheader("📈 Visualisasi Pilihan")

if st.checkbox("Tunjuk graf pendapat penutupan"):
    st.bar_chart(data['Pendapat_penutupan'].value_counts())

if st.checkbox("Tunjuk histogram jarak"):
    st.bar_chart(data['Jarak'].value_counts())



