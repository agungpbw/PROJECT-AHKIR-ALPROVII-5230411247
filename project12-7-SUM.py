import sqlite3

conn = sqlite3.connect('HEWAN.db')
cursor = conn.cursor()

cursor.execute("SELECT SUM(jmlh_sekarang) FROM HEWAN")
total_hewan = cursor.fetchone()[0]

print(f"Total Gaji Seluruh Pegawai: {total_hewan}")

conn.close()
