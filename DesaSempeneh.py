import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("Analisis Responden Terhadap Perpustakaan Komuniti")
    st.markdown("Data dari komuniti Desa Sempeneh tentang pandangan terhadap perpustakaan.")

    try:
        # Load CSV
        data = pd.read_csv('Desa sempeneh.csv')

        # Tunjuk ringkasan
        st.subheader("📌 Ringkasan Data")
        st.write(data.head())

        st.subheader("📊 Info & Statistik")
        st.write("Jumlah nilai kosong:")
        st.write(data.isnull().sum())
        st.write("Statistik Deskriptif:")
        st.write(data.describe())

        # Buang data kosong
        data.dropna(inplace=True)

        # Fungsi plot
        def plot_bar(column, title, colors):
            count_data = data[column].value_counts(dropna=False)
            fig, ax = plt.subplots(figsize=(6, 4))
            count_data.plot(kind='bar', color=colors, ax=ax)
            ax.set_title(title)
            ax.set_xlabel("Jawapan")
            ax.set_ylabel("Bilangan Responden")
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(fig)
            return count_data

        st.subheader("1. Penutupan Perpustakaan")
        penutupan = plot_bar('Penutupan_perpustakaan', 'Respon Terhadap Penutupan Perpustakaan di Komuniti', ['blue', 'mediumseagreen'])
        st.write(penutupan)

        st.subheader("2. Keperluan Perpustakaan")
        perlu_ada = plot_bar('Perlu_ada', 'Respon Terhadap Keperluan Perpustakaan di Komuniti', ['blue', 'mediumseagreen'])
        st.write(perlu_ada)

        st.subheader("3. Lokasi Strategik atau Tidak")
        lokasi = plot_bar('Lokasi_strategik', 'Lokasi Responden Strategik atau Tidak', ['green', 'mediumseagreen'])
        st.write(lokasi)

        st.subheader("4. Jarak Lokasi Responden")
        jarak = plot_bar('Jarak_lokasi', 'Jarak Lokasi Responden', ['green', 'mediumseagreen', 'darkcyan', 'aquamarine'])
        st.write(jarak)

        st.subheader("5. Penerusan Operasi Perpustakaan")
        operasi = plot_bar('Operasi', 'Respon terhadap penerusan operasi perpustakaan', ['coral', 'brown'])
        st.write(operasi)

        # Kesimpulan
        st.subheader("📌 Kesimpulan")
        if penutupan.get("Tidak", 0) > penutupan.get("Ya", 0) and perlu_ada.get("Ya", 0) > perlu_ada.get("Tidak", 0):
            st.success("Berdasarkan data, komuniti lebih cenderung untuk TIDAK menutup perpustakaan dan merasakan ia PERLU ada.")
            st.markdown("**➡️ Kesimpulan: Perpustakaan tidak perlu ditutup dan sebaliknya, perlu diperkasakan.**")
        else:
            st.warning("Sebahagian besar responden mungkin tidak melihat keperluan perpustakaan.")
            st.markdown("**➡️ Kesimpulan: Kajian lanjut diperlukan, tetapi tanda-tanda menunjukkan perpustakaan mungkin tidak lagi diperlukan.**")

    except FileNotFoundError:
        st.error("❌ Fail CSV 'Desa sempeneh.csv' tidak dijumpai. Sila pastikan ia berada dalam direktori yang betul.")
