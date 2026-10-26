# Program Konversi Suhu Python

## Deskripsi
Program Konversi Suhu Python adalah program berbasis terminal yang dibuat menggunakan bahasa pemrograman Python. Program ini memungkinkan pengguna mengonversi suhu dari Celsius, Fahrenheit, Reamur, dan Kelvin ke satuan suhu lainnya.

Program menggunakan percabangan `if-elif-else` untuk menentukan jenis konversi, perulangan `while` agar program dapat digunakan berulang kali, serta modul `time` untuk memberikan jeda saat menampilkan menu.

## Fitur
- Konversi Celsius ke Fahrenheit, Reamur, dan Kelvin.
- Konversi Fahrenheit ke Celsius, Reamur, dan Kelvin.
- Konversi Reamur ke Celsius, Fahrenheit, dan Kelvin.
- Konversi Kelvin ke Celsius, Fahrenheit, dan Reamur.
- Menu interaktif berbasis terminal.
- Fitur pengulangan konversi tanpa menjalankan ulang program.
- Jeda tampilan menggunakan modul `time`.

## Teknologi yang Digunakan
- **Bahasa pemrograman:** Python
- **Modul:** `time`
- **Konsep pemrograman:** variabel, input-output, tipe data, operasi aritmetika, percabangan, dan perulangan.

## Persyaratan
- Python 3 sudah terinstal di komputer.
- Terminal atau code editor, seperti Visual Studio Code.

## Cara Menjalankan

1. Unduh atau clone repository ini ke komputer.
2. Buka folder proyek di Visual Studio Code atau terminal.
3. Jalankan program dengan perintah berikut:

```bash
python konversi_suhu.py
```

Jika perintah `python` tidak dikenali di Windows, coba:

```bash
py konversi_suhu.py
```

**Catatan:** Sesuaikan `konversi_suhu.py` dengan nama file Python yang digunakan dalam proyek ini.

## Cara Menggunakan
1. Jalankan program melalui terminal.
2. Pilih satuan suhu awal: `celcius`, `fahrenheit`, `reamur`, atau `kelvin`.
3. Pilih satuan suhu tujuan sesuai menu yang tersedia.
4. Masukkan nilai suhu yang ingin dikonversi.
5. Program akan menampilkan hasil konversi.
6. Jawab `ya` jika ingin mengulang konversi atau `tidak` untuk mengakhiri program.

**Penting:** Masukkan pilihan menggunakan huruf kecil sesuai instruksi program.

## Contoh Penggunaan

```text
====KONVERSI SUHU====

Silahkan masukkan suhu yang mau anda konversikan
(celcius/fahrenheit/reamur/kelvin): celcius

kamu mau konversi celcius ke suhu apa?
fahrenheit/reamur/kelvin: fahrenheit

silahkan masukkan angka: 100

suhu dalam fahrenheit: 212.0 °F
```

## Tujuan Proyek
Proyek ini dibuat sebagai latihan dasar pemrograman Python untuk memahami penggunaan variabel, input-output, operasi aritmetika, percabangan, perulangan, dan modul bawaan Python.

## Pengembangan Selanjutnya
- Menambahkan validasi input agar program tidak berhenti ketika pengguna memasukkan nilai yang tidak valid.
- Memperbaiki ketelitian rumus konversi suhu.
- Menambahkan pilihan satuan menggunakan angka.
- Merapikan hasil konversi menggunakan format desimal yang konsisten.

## Status Proyek
Proyek latihan pembelajaran yang dapat dikembangkan lebih lanjut.
