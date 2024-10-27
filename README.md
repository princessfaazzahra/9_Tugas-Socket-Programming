# 9_Tugas-Socket-Programming
Tugas UDP Socket Programming by Team Labschool :

Princessfa Azzahra Alvin / 18223044

Fhatika Adhalisman Ryanjani / 18223062


# Guide untuk menjalankan program Labschool Bos Roomchat
Sebelum menjalankan program, pastikan pada laptop ataupun komputer, pengaturan firewall sudah mengizinkan koneksi UDP pada port yang akan digunakan, untuk menjalankan Labschool Bos Roomchat, port yang sudah ditambahkan pada rules firewall adalah 8080 dan 5000-5010. Terakhir, sebelum menjalankan aplikasi pastikan bahwa jaringan internet stabil untuk memastikan komunikasi UDP antara server dan client berjalan dengan lancar.

Langkah- langkah pengujian program adalah sebagai berikut : 

Menjalankan server

1.1 Pastikan server.py dan client.py berada dalam folder yang sama

1.2 Pastikan laptop client dan server terhubung pada jaringan yang sama

1.3 Membuka terminal pada folder yang berisi server.py dan client.py di laptop atau komputer yang bertindak sebagai server

1.4 Command untuk menjalankan server : 
      python server.py < IP SERVER> -p [PORT]
      
1.5 Tunggu respons dari terminal 


Menjalankan client


2.1 Pastikan server.py dan client.py berada dalam folder yang sama

2.2 Pastikan laptop client dan server terhubung pada jaringan yang sama

2.3 Membuka terminal pada folder yang berisi server.py dan client.py di laptop atau komputer

2.4 Command untuk menghubungkan client ke server : 
      python client.py <IP SERVER> <PORT SERVER> <PORT CLIENT>

2.5 Client akan diminta untuk memasukkan username dan password

2.6 Client akan disiapkan untuk dapat mengirim serta menerima pesan dari server

2.7 Lakukan langkah yang sama apabila ingin melakukan pengujian pada 2 client namun
pastikan client kedua memiliki port yang berbeda


Pengujian chatroom


3.1 Setelah client pertama berhasil terhubung, ketika client kedua baru terhubung maka 
pada aplikasi roomchat client pertama akan ada notifikasi bahwa client 2 sudah hadir
      
3.2 Client pertama dapat mengirim pesan kepada server untuk kemudian diteruskan ke 
client lain yang terhubung

3.3 Untuk melihat proses menerima dan mengirim pesan antar client maka pengguna 
 dapat membuka terminal yang sudah dijalankan untuk server
 
3.4 Apabila salah satu ataupun kedua client sudah selesai mengirim pesan, maka client
bisa memberi command ‘QUIT’ untuk keluar dari aplikasi roomchat.
