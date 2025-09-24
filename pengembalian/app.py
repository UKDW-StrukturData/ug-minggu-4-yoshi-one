import copy
import streamlit as st
from pengembalian import process_pengembalian, test_cases

st.set_page_config(page_title="Sistem Pengembalian Buku", layout="centered")
st.title("Sistem Pengembalian Buku")

pilihan = st.selectbox("Pilih skenario uji:", [tc["name"] for tc in test_cases])
tc = next(tc for tc in test_cases if tc["name"] == pilihan)

pemberitahuan = st.info
sukses = st.success
gagal = st.error 

if st.button("Proses Pengembalian"):
    result = process_pengembalian(copy.deepcopy(tc["buku"]), copy.deepcopy(tc["mahasiswa"]))

    st.subheader("Laporan Pengembalian")
    for item in result["laporan"]:
        st.markdown(f"**Mahasiswa:** {item['nama']}")
        if item["berhasil"]:
            sukses("Berhasil dikembalikan: " + ", ".join(item["berhasil"]))
        if item["gagal"]:
            gagal_list = [f"{g[0]} ({g[1]})" for g in item["gagal"]]
            gagal("Gagal diproses: " + ", ".join(gagal_list))
        if not item["berhasil"] and not item["gagal"]:
            pemberitahuan("Tidak ada buku yang dikembalikan.")


    st.subheader("Data Buku Terbaru")
    for judul, info in result["buku"].items():
        st.write(f"- {judul} | stok: {info['stok']} | status: {info['status']}")

    st.subheader("Data Mahasiswa Terbaru")
    for nama, data in result["mahasiswa"].items():
        pinj = ", ".join(data.get("pinjaman", [])) if data.get("pinjaman") else "-"
        st.write(f"- {nama} | pinjaman: {pinj}")