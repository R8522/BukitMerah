import streamlit as st
import pandas as pd

# --- Title ---
st.title("Analisis Penutupan Perpustakaan Bukit Merah")

# --- Load Data ---
st.header("📥 Data Asal")

df1 = pd.read_csv('Bukit Merah.csv')  # pastikan fail ni ada dalam repo yang sama
df2 = pd.read_csv('Data Sebab Bukit Merah.csv')

df1.columns = df1.columns.str.strip().str.lower()
df2.columns = df2.columns.str.strip().str.lower()

data = pd.merge(df1, df2, on='bil', how='inner')

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


st.markdown(""" 
Pendapat_penutupan = Apakah pendapat pengguna/pengunjung berkaitan dengan penutupan perpustakaan ini?

TP = Tidak perlu ditutup

P = Perlu ditutup

""")

# --- Kolum Kategori Lain ---
st.subheader("📋 Statistik Kolum Kategori Lain")

kategori = ['Operasi', 'Strategik']
for col in kategori:
    st.markdown(f"**{col}**")
    st.write(data[col].describe())

st.markdown(""" 
Operasi = Adakah pengguna/pengunjung ingin melihat perpustakaan desa ini terus beroperasi?

Y = Ya

T = Tidak

Strategik = Adakah lokasi perpustakaan strategik dan mudah dikunjung?

Y = Ya

T = Tidak

""")

# --- Visualization (optional) ---
st.subheader("📈 Visualisasi Pilihan")

if st.checkbox("**Graf pendapat penutupan library**"):
    st.bar_chart(data['Pendapat_penutupan'].value_counts())
st.markdown(""" 
TP = Tidak perlu ditutup

P = Perlu ditutup

""")

if st.checkbox("**Graf jarak kediaman pengunjung**"):
    st.bar_chart(data['Jarak'].value_counts())
st.markdown(""" 
0-900 meter = 1

1-3 km = 2

4-5 km = 3

6-10 km = 4

10 km ke atas = 5


""")


