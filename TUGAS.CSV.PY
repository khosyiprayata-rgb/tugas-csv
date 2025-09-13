import csv
from collections import defaultdict

# Ganti path ini dengan lokasi file CSV kamu
file_path = r"C:\python\tugas csv\csv\keuangan.cvs"

# Untuk menyimpan semua data transaksi
data_keuangan = []

# 1️⃣ Tampilkan Semua Data
print("📋 Semua Data Transaksi:")
with open(file_path, mode="r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # Lewati header

    for row in reader:
        data_keuangan.append(row)
        tanggal, keterangan, kategori, jumlah = row
        print(f"{tanggal} | {keterangan} | {kategori} | Rp{jumlah}")

# 2️⃣ Hitung Total Pengeluaran
total_pengeluaran = sum(int(row[3]) for row in data_keuangan)
print("\n💸 Total Pengeluaran: Rp{}".format(total_pengeluaran))

# 3️⃣ Hitung Total per Kategori
pengeluaran_per_kategori = defaultdict(int)
for row in data_keuangan:
    kategori = row[2]
    jumlah = int(row[3])
    pengeluaran_per_kategori[kategori] += jumlah

print("\n📊 Pengeluaran per Kategori:")
for kategori, total in pengeluaran_per_kategori.items():
    print(f"- {kategori}: Rp{total}")

# 4️⃣ Cari Kategori dengan Pengeluaran Terbesar
kategori_terbesar = max(pengeluaran_per_kategori.items(), key=lambda x: x[1])
print("\n🏆 Kategori Terbesar: {} (Rp{})".format(kategori_terbesar[0], kategori_terbesar[1]))

# 🎲 Tantangan Tambahan (Opsional)

# 🗓️ Cari tanggal dengan pengeluaran terbanyak
pengeluaran_per_tanggal = defaultdict(int)
for row in data_keuangan:
    tanggal = row[0]
    jumlah = int(row[3])
    pengeluaran_per_tanggal[tanggal] += jumlah

tanggal_terbesar = max(pengeluaran_per_tanggal.items(), key=lambda x: x[1])
print("\n📅 Tanggal dengan Pengeluaran Terbesar: {} (Rp{})".format(tanggal_terbesar[0], tanggal_terbesar[1]))

# 📈 Rata-rata pengeluaran per hari
total_hari = len(pengeluaran_per_tanggal)
rata_rata = total_pengeluaran / total_hari
print("📈 Rata-rata Pengeluaran per Hari: Rp{:.0f}".format(rata_rata))
