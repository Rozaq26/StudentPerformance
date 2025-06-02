# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech


## Business Understanding
**Jaya Jaya Institut** adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah berhasil mencetak banyak lulusan dengan reputasi yang sangat baik di berbagai bidang. Namun, seperti banyak institusi pendidikan lainnya, Jaya Jaya Institut juga menghadapi tantangan yang signifikan terkait dengan tingginya tingkat siswa yang tidak menyelesaikan pendidikannya alias dropout.

**Masalah dropout** ini merupakan masalah yang serius bagi institusi pendidikan, karena dropout yang tinggi dapat mempengaruhi citra institusi, mengurangi tingkat kelulusan, dan pada akhirnya berdampak pada daya tarik institusi bagi calon siswa di masa mendatang. Tingkat dropout yang tinggi juga bisa menjadi indikasi bahwa ada masalah mendasar dalam proses penerimaan siswa, pembelajaran, atau dukungan akademik yang disediakan oleh institusi.

### Permasalahan Bisnis
Berikut adalah beberapa pertanyaan yang menggambarkan permasalahan bisnis yang akan diselesaikan oleh Jaya Jaya Institut:

1. Bagaimana cara mengidentifikasi siswa-siswa yang berpotensi mengalami dropout sejak dini?
2. Faktor-faktor apa saja yang paling berpengaruh terhadap keputusan siswa untuk dropout?
3. Apa yang dapat dilakukan untuk meningkatkan tingkat retensi siswa dan memastikan lebih banyak siswa menyelesaikan pendidikan mereka?

### Cakupan Proyek
* Analisis Data: Menggunakan data yang ada untuk mengidentifikasi faktor-faktor utama yang mempengaruhi dropout.
* Visualisasi & Pelaporan: Mengembangkan dashboard yang dapat digunakan untuk memonitor dan menganalisis faktor-faktor tersebut secara visual.
* Rekomendasi & Intervensi: Berdasarkan hasil analisis, memberikan rekomendasi untuk intervensi yang dapat dilakukan untuk mengurangi droput.

### Persiapan

Sumber data: dataset yang digunakan merupakan dataset [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance).

### Instalasi

1. **Pastikan Python terinstal**
   - Pastikan Python versi 3.x terinstal di sistem Anda. Anda dapat mengunduh dan menginstalnya dari [python.org](https://www.python.org/).

2. **Buat lingkungan virtual**
   - Buat lingkungan virtual untuk mengisolasi dependensi proyek. Jalankan perintah berikut di terminal Anda:
     ```bash
     python -m venv env
     ```

3. **Aktifkan lingkungan virtual**
   - Untuk Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - Untuk macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Pasang dependensi menggunakan `requirements.txt`**
   - Pastikan berada di direktori proyek yang sama dengan file `requirements.txt`, lalu jalankan perintah berikut:
     ```bash
     pip install -r requirements.txt
     ```

## Business Dashboard

Dashboard ini dirancang untuk menganalisis faktor-faktor penyebab mahasiswa dropout. Komponen utama dari dashboard ini meliputi ditampilkan dalam Looker Studio.

Tautan ke Dasbor Bisnis  [Disini](https://lookerstudio.google.com/reporting/771c284c-5455-46b3-bafa-f0169be891ef).

Dashboard tersebut memperlihatkan hubungan antara beberapa kolom dan tingkat atrisi.

Isi Dashboard
<img src="https://github.com/Rozaq26/StudentPerformance/blob/main/Images/Dashboard.jpg" width="500">

### Isi dashboard

1. Gender Siswa (Pie Chart)

- Definisi: Diagram lingkaran yang menunjukkan proporsi siswa berdasarkan jenis kelamin (Laki-laki/Male dan Perempuan/Female).
- Fungsi:
Menampilkan komposisi gender siswa secara keseluruhan dan Mengidentifikasi apakah ada dominasi gender tertentu dalam populasi siswa.

2. Status Kelulusan (Pie Chart)

- Definisi: Diagram lingkaran yang menampilkan persentase siswa berdasarkan status kelulusan mereka.
- Fungsi:
Memberikan gambaran umum tentang hasil akhir program studi siswa dan Mengidentifikasi proporsi siswa yang berhasil menyelesaikan studi, yang keluar, dan yang masih aktif.

3. Distribusi Kelulusan Berdasarkan Ketergusuran (Tabel dan Bar Chart)

- Definisi: Tabel dan diagram batang yang menunjukkan jumlah siswa berdasarkan status kelulusan dan status ketergusuran mereka.
- Fungsi:
Menganalisis hubungan antara ketergusuran dengan status kelulusan siswa.
Mengidentifikasi apakah siswa yang pernah mengalami ketergusuran memiliki kecenderungan tertentu terkait kelulusan atau putus sekolah.

4. Distribusi Kelulusan Berdasarkan Beasiswa (Tabel dan Bar Chart)

- Definisi: Tabel dan diagram batang yang menampilkan jumlah siswa berdasarkan status kelulusandan apakah mereka penerima beasiswa.
- Fungsi:
Menganalisis dampak program beasiswa terhadap tingkat kelulusan siswa.
Membandingkan tingkat kelulusan antara penerima beasiswa dan non-penerima beasiswa.

5. Distribusi Kelulusan Berdasarkan Hutang (Tabel dan Bar Chart)

- Definisi: Tabel dan diagram batang yang menunjukkan jumlah siswa berdasarkan status kelulusann dan status hutang mereka.
- Fungsi:
Menganalisis potensi pengaruh hutang terhadap status kelulusan siswa.
Mengidentifikasi apakah siswa dengan hutang memiliki perbedaan dalam profil kelulusan.

6. Korelasi Status Kelulusan Siswa Berdasarkan Waktu Pembelajaran (Bar Chart)

- Definisi: 
Diagram yang membandingkan status kelulusan siswa (Lulus, Putus Sekolah, Terdaftar) antara kelompok siswa dengan waktu pembelajaran yang berbeda (Pagi/Daytime, Sore/Evening).
- Fungsi:
Mengidentifikasi apakah ada perbedaan signifikan dalam status kelulusan berdasarkan waktu pembelajaran yang dipilih siswa.
Membantu mengevaluasi efektivitas atau tantangan yang mungkin terkait dengan jadwal pembelajaran yang berbeda.

7. Korelasi Status Kelulusan Siswa Berdasarkan Biaya (Bar Chart)

- Definisi: 
Diagram batang yang menunjukkan kerterkaitan status kelulusan siswa dengan suatu kategori biaya.
- Fungsi:
Menganalisis hubungan antara faktor biaya dengan status kelulusan siswa.
Mengidentifikasi apakah kemampuan atau kewajiban membayar biaya tertentu berpengaruh pada hasil studi siswa.



## Menjalankan Sistem Machine Learning
Pada proyek ini telah disediakan sebuah prototype untuk melakukan prediksi terhadap model yang sudah dibuat. Untuk menjalankan protoype secara lokal jalankan perintah berikut di terminal: 
    ```
        streamlit run Streamlit.py
    ```

Atau buka [tautan](https://studentperformance-nnbhehdnftnvcjw243nqs9.streamlit.app/) untuk membuka prototype yang sudah dijalankan pada streamlit community.

<img src="https://github.com/Rozaq26/StudentPerformance/blob/main/Images/Streamlit.jpg" width="500">

## Conclusion
Proyek ini dirancang untuk menjawab beberapa permasalahan utama yang dihadapi oleh Jaya Jaya Institut terkait dengan tingkat dropout siswa. Berikut adalah kesimpulan dari proyek ini:

1. Bagaimana cara mengidentifikasi siswa-siswa yang berpotensi mengalami dropout sejak dini?
    - Dengan membangun model prediktif menggunakan algoritma seperti Random Forest, Jaya Jaya Institut dapat mengidentifikasi siswa-siswa yang berpotensi mengalami dropout sejak dini. Model ini mampu mendeteksi siswa berisiko dengan tingkat akurasi yang memadai berdasarkan data historis dan faktor-faktor demografis, akademik, serta ekonomi.

2. Faktor-faktor apa saja yang paling berpengaruh terhadap keputusan siswa untuk dropout?
    - Analisis korelasi dan pentingnya fitur dalam model prediktif menunjukkan bahwa beberapa faktor yang paling berpengaruh terhadap keputusan siswa untuk dropout antara lain latar belakang akademik (seperti nilai dan jumlah unit yang diambil) dan kondisi ekonomi (scholarship ataupun displaced) . Misalnya, siswa yang menghadapi kesulitan akademik dalam semester pertama atau kedua cenderung memiliki risiko lebih tinggi untuk dropout.

    <img src="https://github.com/Rozaq26/StudentPerformance/blob/main/Images/korelasi.jpg" width="500">
    
3. Apa yang dapat dilakukan untuk meningkatkan tingkat retensi siswa dan memastikan lebih banyak siswa menyelesaikan pendidikan mereka?
    - Berdasarkan temuan dari model dan analisis data, Jaya Jaya Institut dapat meningkatkan tingkat retensi siswa dengan beberapa strategi, seperti menyediakan bimbingan akademik yang lebih intensif, menyesuaikan kurikulum untuk mengurangi beban siswa, dan memberikan dukungan finansial tambahan kepada siswa yang membutuhkannya. Intervensi yang lebih dini dan berbasis data dapat membantu memastikan lebih banyak siswa menyelesaikan pendidikan mereka.

### Action Items
Berikan beberapa rekomendasi action items bisa dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
1. Implementasi Sistem Pemantauan Siswa Berbasis Data
    - Menerapkan model prediktif yang telah dibangun untuk memantau siswa secara berkala. Institusi dapat menggunakan sistem ini untuk mendeteksi siswa yang berisiko tinggi untuk dropout dan memberikan intervensi dini berupa bimbingan akademik atau dukungan lainnya.
2. Pengembangan Program Dukungan Akademik dan Psikologis
    - Berdasarkan faktor-faktor risiko yang diidentifikasi, institusi harus memperkuat program dukungan akademik dan psikologis. Ini bisa mencakup peningkatan akses ke bimbingan belajar, sesi konseling, dan dukungan kesehatan mental bagi siswa yang rentan.
3. Optimalisasi Kurikulum dan Program Studi
    - Lakukan evaluasi terhadap program studi yang memiliki tingkat dropout tinggi dan lakukan penyesuaian kurikulum atau metode pengajaran. Misalnya, meningkatkan fleksibilitas dalam penjadwalan kursus atau menyediakan materi pendukung tambahan dapat membantu mengurangi tekanan akademik pada siswa.
