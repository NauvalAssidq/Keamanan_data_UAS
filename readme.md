Berikut adalah versi lengkap untuk README.md yang mencakup chipergui, desgui, enigmagui, dan steganogui dalam satu bagian dengan format yang memungkinkan Anda langsung menyalin dan menggunakannya.

markdown
Copy code
# GUI Tools Documentation

Berikut adalah panduan penggunaan untuk **chipergui**, **desgui**, **enigmagui**, dan **steganogui**. Tools ini dirancang untuk membantu pengguna dalam melakukan operasi kriptografi dan steganografi melalui antarmuka grafis.

---

## Cara Menggunakan

### Jalankan Aplikasi GUI

Untuk menjalankan setiap aplikasi GUI, gunakan perintah berikut di terminal:  
```bash
python chipergui.py
python desgui.py
python enigmagui.py
python steganogui.py
Berikut detail penggunaan masing-masing aplikasi:

1. Chipergui
Alat GUI untuk melakukan berbagai operasi cipher, seperti enkripsi dan dekripsi menggunakan algoritma klasik.

Pilih algoritma cipher yang diinginkan (contoh: Caesar Cipher, Vigenere Cipher).
Masukkan teks yang ingin dienkripsi atau didekripsi.
Masukkan kunci (key) yang sesuai.
Klik tombol "Encrypt" atau "Decrypt".
Hasil akan ditampilkan di area output.
2. Desgui
Alat GUI untuk melakukan enkripsi dan dekripsi menggunakan algoritma DES (Data Encryption Standard).

Masukkan teks yang ingin dienkripsi atau didekripsi.
Masukkan kunci (key) 64-bit.
Pilih mode operasi (ECB, CBC, dll.).
Klik tombol "Encrypt" atau "Decrypt".
Hasil akan ditampilkan di area output.
3. Enigmagui
Simulasi GUI dari mesin Enigma untuk enkripsi dan dekripsi pesan.

Konfigurasikan rotors dan reflector sesuai kebutuhan:
Pilih jenis rotor.
Atur posisi awal rotor.
Pilih jenis reflector.
Masukkan teks yang ingin dienkripsi atau didekripsi.
Klik tombol "Encrypt" atau "Decrypt".
Hasil akan ditampilkan di area output.
4. Steganogui
Alat GUI untuk menyembunyikan atau mengekstrak pesan dari gambar menggunakan teknik steganografi.

Pilih mode:
Hide Message: Untuk menyembunyikan pesan dalam gambar.
Extract Message: Untuk mengekstrak pesan dari gambar.
Jika memilih Hide Message:
Unggah gambar yang akan digunakan.
Masukkan pesan yang ingin disembunyikan.
Klik "Hide" untuk menyisipkan pesan ke dalam gambar.
Simpan gambar hasil steganografi.
Jika memilih Extract Message:
Unggah gambar steganografi.
Klik "Extract" untuk mendapatkan pesan tersembunyi.
Pesan akan muncul di area output.
Persyaratan Sistem
Python versi 3.x.
Library tambahan:
Tkinter (terintegrasi dengan Python).
Pillow (untuk manipulasi gambar).
PyCrypto (untuk DES).
Library lain sesuai kebutuhan aplikasi.
Instalasi
Ikuti langkah-langkah berikut untuk menjalankan aplikasi:

Clone repository:

bash
Copy code
git clone https://github.com/username/repository.git
cd repository
Instal library yang diperlukan:

bash
Copy code
pip install -r requirements.txt
Jalankan aplikasi GUI yang diinginkan:

bash
Copy code
python chipergui.py
python desgui.py
python enigmagui.py
python steganogui.py
Kontribusi
Kontribusi sangat diterima! Jika Anda memiliki ide untuk meningkatkan tools ini, silakan buka issue atau buat pull request.

Lisensi
Proyek ini dilisensikan di bawah MIT License.

Kontak
Jika Anda memiliki pertanyaan atau masukan, silakan hubungi email@example.com.

perl
Copy code

Dengan format ini, semua panduan sudah berada dalam satu tempat. Anda bisa langsung menyalin ke file `README.md`. Setiap bagian (chipergui, desgui, enigmagui, steganogui) dijelaskan dalam satu rangkaian tanpa ada potongan terpisah. Pastikan mengganti URL repository dan email sesuai kebutuhan Anda!
