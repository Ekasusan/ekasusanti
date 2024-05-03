class buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"{self.judul} - {self.penulis} ({self.genre}) - status: {self.status}"

class perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-- daftar buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("koleksi buku masih kosong.")

    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                return
        print(f"buku dengan judul '{judul}' tidak ditemukan.")

    def pinjam_buku(self, judul_buku, nama_anggota):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul_buku.lower():
                if buku.status == "tersedia":
                    buku.status = "dipinjam"
                    nama_anggota.buku_pinjaman.append(buku)
                    print(f"buku '{buku.judul}' berhasil dipinjam oleh {nama_anggota.nama}.")
                else:
                    print(f"buku '{buku.judul}' tidak tersedia untuk dipinjam.")
                return
        print(f"Buku dengan judul '{judul_buku}' tidak ditemukan.")

    def kembalikan_buku(self, judul_buku, nama_anggota):
        for buku in nama_anggota.buku_pinjaman:
            if buku.judul.lower() == judul_buku.lower():
                buku.status = "tersedia"
                nama_anggota.buku_pinjaman.remove(buku)
                print(f"Buku '{buku.judul}' telah dikembalikan.")
                return
        print(f"Buku dengan judul '{judul_buku}' tidak ditemukan dalam daftar pinjaman {nama_anggota.nama}.")

class anggota:
    def __init__(self, nama, ID):
        self.nama = nama
        self.ID = ID
        self.buku_pinjaman = []

    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"-- buku pinjaman {self.nama} --")
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman.")

def main():
    # buat beberapa buku
    buku1 = buku("Bumi", "Tere Liye", "fiksi", "tersedia")
    buku2 = buku("Laskar Pelangi", "Andrea Hirata", "fiksi", "tersedia")
    buku3 = buku("Filosofi Terbang", "Dewi Lestari", "fiksi", "dipinjam")

    # buat perpustakaan dan anggota
    perpus = perpustakaan()
    perpus.koleksi_buku.extend([buku1, buku2, buku3])

    anggota1 = anggota("Andi", 12345)
    anggota2 = anggota("Budi", 56789)

    # jalankan program
    print("\n-- menu perpustakaan --")
    print("1. tampilkan daftar buku")
    print("2. cari buku")
    print("3. pinjam buku")
    print("4. kembalikan buku")
    angka = int(input("pilih menu: "))

    if angka == 1:
        perpus.tampilkan_buku()
    elif angka == 2:
        judul = input("input judul buku: ")
        perpus.cari_buku(judul)
    elif angka == 3:
        judul = input("buku yang dipinjam: ")
        nama_anggota = anggota(input("input nama anggota: "), 0)  # Dummy ID karena tidak digunakan
        perpus.pinjam_buku(judul, nama_anggota)
    elif angka == 4:
        judul = input("buku yang dikembalikan: ")
        nama_anggota = anggota(input("input nama anggota: "), 0)  # Dummy ID karena tidak digunakan
        perpus.kembalikan_buku(judul, nama_anggota)
    else:
        print("anda salah pilih")

if __name__ == "__main__":
    main()
