import streamlit as st

# App Title
st.set_page_config(page_title="Analisis Perpustakaan Komuniti", layout="centered")
st.title("📚 Sistem Analisis Komuniti Perpustakaan")

# Sidebar Navigation
st.sidebar.header("📂 Pilih Lokasi")
page = st.sidebar.selectbox(
    "Lokasi Komuniti:",
    ["Desa Sempeneh", "Bukit Merah", "Kuala Dipang"]
)

# Routing
if page == "Desa Sempeneh":
    import DesaSempeneh
    DesaSempeneh.run()

elif page == "Bukit Merah":
    import BukitMerah
    BukitMerah.run()

elif page == "Kuala Dipang":
    import KualaDipang
    KualaDipang.run()

# Optional footer
st.markdown("---")
st.caption("Dibangunkan oleh 🧠 Sistem Analitik Komuniti | Projek Latihan Industri")
