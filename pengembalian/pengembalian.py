import copy

def process_pengembalian(buku, mahasiswa):
    laporan = []
    
    def kembalikan_buku(nama, judul):
        # 1. Validasi mahasiswa
        # TODO: melakukan pengecekan apakah nama mahasiswa ada dalam dictionary buku, kemudian
        #    return (judul, "Gagal", "Mahasiswa tidak terdaftar")

        # 2. Validasi judul buku
        # TODO: melakukan pengecekan apakah judul ada dalam dictionary buku, kemudian
        #    return (judul, "Gagal", "Judul tidak ditemukan")

        # 3. TODO: cek apakah buku tercatat sedang dipinjam oleh mahasiswa
        # hint: gunakan if judul in mahasiswa[nama].get("pinjaman", [])
        # jika iya: hapus dari daftar pinjaman
        # lalu tambahkan stok buku +1
        # jika status buku sebelumnya "Kosong", ubah menjadi "Tersedia"
            # return (judul, "Berhasil", None)

        # 4. Jika tidak ada di daftar pinjaman
        return (judul, "Gagal", "Tidak tercatat sebagai pinjaman")

    for nama, data in mahasiswa.items():
        hasil_berhasil, hasil_gagal = [], []
        ingin = data.get("ingin_kembali", [])
        for judul in ingin:
            res = kembalikan_buku(nama, judul)
            if res[1] == "Berhasil":
                hasil_berhasil.append(res[0])
            else:
                hasil_gagal.append((res[0], res[2]))
        laporan.append({
            "nama": nama,
            "berhasil": hasil_berhasil,
            "gagal": hasil_gagal
        })

    return {"laporan": laporan, "buku": buku, "mahasiswa": mahasiswa}



test_cases = [
    {
        "name": "1. Sukses sederhana (kembali 1 buku)",
        "buku": {"algoritma dasar": {"stok": 0, "status": "Kosong"}},
        "mahasiswa": {"Rina": {"pinjaman": ["algoritma dasar"], "ingin_kembali": ["algoritma dasar"]}}
    },
    {
        "name": "2. Gagal - tidak pernah pinjam",
        "buku": {"basis data": {"stok": 1, "status": "Tersedia"}},
        "mahasiswa": {"Budi": {"pinjaman": [], "ingin_kembali": ["basis data"]}}
    },
    {
        "name": "3. Beberapa pengembalian campuran",
        "buku": {
            "struktur data": {"stok": 0, "status": "Kosong"},
            "logika matematika": {"stok": 1, "status": "Tersedia"}
        },
        "mahasiswa": {
            "Citra": {"pinjaman": ["struktur data"], "ingin_kembali": ["struktur data", "logika matematika"]}
        }
    },
    {
        "name": "4. Tidak ada yang dikembalikan",
        "buku": {"pemrograman python": {"stok": 2, "status": "Tersedia"}},
        "mahasiswa": {"Deni": {"pinjaman": ["pemrograman python"], "ingin_kembali": []}}
    }
]


def print_result(result):
    print("=== Laporan Pengembalian ===")
    for item in result["laporan"]:
        print(f"Mahasiswa: {item['nama']}")
        for b in item["berhasil"]:
            print(f"  Berhasil dikembalikan : {b}")
        for g in item["gagal"]:
            print(f"  Gagal diproses         : {g[0]} ({g[1]})")
        if not item["berhasil"] and not item["gagal"]:
            print("  Tidak ada buku yang dikembalikan.")


def run_terminal():
    for tc in test_cases:
        print("\n" + "="*70 + "\n")
        print("TEST:", tc["name"])
        res = process_pengembalian(copy.deepcopy(tc["buku"]), copy.deepcopy(tc["mahasiswa"]))
        print_result(res)

if __name__ == "__main__":
    run_terminal()
    print("\n[INFO] Untuk UI Streamlit, jalankan: streamlit run app.py")
