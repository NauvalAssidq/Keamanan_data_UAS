# GUI Tools Documentation

Panduan ini mencakup penggunaan dari empat aplikasi GUI: **chipergui**, **desgui**, **enigmagui**, dan **steganogui**. Keempat tools ini dirancang untuk memudahkan pengguna melakukan operasi kriptografi dan steganografi melalui antarmuka grafis berbasis Python.

---

## 📌 Cara Menjalankan Aplikasi

Untuk menjalankan masing-masing aplikasi GUI, buka terminal di direktori proyek dan jalankan perintah berikut:

```bash
python chipergui.py
python desgui.py
python enigmagui.py
python steganogui.py
```

---

## 🛠️ Panduan Penggunaan Aplikasi

### 1. `chipergui` - Cipher GUI
Aplikasi ini digunakan untuk enkripsi dan dekripsi teks menggunakan algoritma cipher klasik.

**Langkah Penggunaan:**
- Pilih algoritma cipher yang diinginkan (misal: Caesar, Vigenère).
- Masukkan teks yang akan dienkripsi atau didekripsi.
- Masukkan kunci yang sesuai.
- Klik tombol **Encrypt** atau **Decrypt**.
- Hasil akan muncul di area output.

---

### 2. `desgui` - DES Encryption GUI
Aplikasi ini menyediakan antarmuka untuk enkripsi dan dekripsi menggunakan algoritma **DES (Data Encryption Standard)**.

**Langkah Penggunaan:**
- Masukkan teks yang akan dienkripsi atau didekripsi.
- Masukkan kunci 64-bit.
- Pilih mode operasi (ECB, CBC, dll.).
- Klik **Encrypt** atau **Decrypt**.
- Hasil akan tampil di area output.

---

### 3. `enigmagui` - Enigma Machine Simulator
Simulasi grafis mesin Enigma untuk kebutuhan enkripsi dan dekripsi pesan historis.

**Langkah Penggunaan:**
- Pilih jenis rotor dan atur posisi awal rotor.
- Pilih jenis reflector.
- Masukkan teks yang ingin diproses.
- Klik tombol **Encrypt** atau **Decrypt**.
- Hasil akan ditampilkan di output.

---

### 4. `steganogui` - Steganography GUI
Alat ini digunakan untuk menyembunyikan atau mengekstrak pesan dari gambar menggunakan teknik steganografi.

**Mode:**
- **Hide Message**: Menyisipkan pesan dalam gambar.
- **Extract Message**: Mengambil pesan tersembunyi dari gambar.

**Hide Message:**
- Pilih gambar.
- Masukkan pesan yang ingin disisipkan.
- Klik **Hide** untuk memproses.
- Simpan gambar hasil.

**Extract Message:**
- Unggah gambar steganografi.
- Klik **Extract** untuk membaca pesan tersembunyi.
- Pesan akan muncul di output.

---

## 💻 Persyaratan Sistem

- Python 3.x
- Library Python yang dibutuhkan:
  - `tkinter` (sudah terintegrasi di Python)
  - `Pillow` (manipulasi gambar)
  - `pycryptodome` (untuk DES)
  - Library tambahan sesuai kebutuhan masing-masing aplikasi

---

## 🔧 Instalasi

1. **Clone Repository:**
```bash
git clone https://github.com/username/repository.git
cd repository
```

2. **Instal Library yang Diperlukan:**
```bash
pip install -r requirements.txt
```

3. **Jalankan Aplikasi GUI:**
```bash
python chipergui.py
python desgui.py
python enigmagui.py
python steganogui.py
```

---

## 🤝 Kontribusi

Kontribusi sangat terbuka!  
Silakan ajukan *issue* atau *pull request* jika Anda memiliki ide atau perbaikan untuk tools ini.

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah **MIT License**.

---

## 📬 Kontak

Untuk pertanyaan atau masukan, hubungi: `email@example.com`

---

Pastikan Anda mengganti bagian URL repository dan alamat email sesuai dengan informasi Anda sendiri sebelum membagikan atau mengunggah ke GitHub. Jika Anda butuh format tambahan seperti badge, changelog, atau gambar antarmuka GUI, saya juga bisa bantu buatkan.
