print("## Program Python Menghitung Gaji Karyawan ##")
print("=============================================")
print()
nama = input("Nama Karyawan: ")
golongan = input("Golongan: ")
jam_kerja = int(input("Jumlah Jam Kerja: "))

if golongan == "A":
    upah_per_jam = 5000
elif golongan == "B":
    upah_per_jam = 7000
elif golongan == "C":
    upah_per_jam = 8000
elif golongan == "D":
    upah_per_jam = 10000
else:
    upah_per_jam = 0

if upah_per_jam == 0:
    print("Golongan Tidak Tersedia")
elif jam_kerja > 48 and upah_per_jam > 0:
    uang_lembur = (jam_kerja - 48) * 4000
    gaji = jam_kerja * upah_per_jam + uang_lembur
    print()
    print(f"{nama} menerima upah Rp. {gaji} per minggu")
else:
    uang_lembur = 0
    gaji = jam_kerja * upah_per_jam + uang_lembur
    print()
    print(f"{nama} menerima upah Rp. {gaji} per minggu")