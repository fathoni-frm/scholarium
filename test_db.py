import mysql.connector
try:
    con = mysql.connector.connect(host="localhost", user="root", password="password", db="tubespbo")
    print("Koneksi Berhasil!")
except Exception as e:
    print(f"Koneksi Gagal: {e}")