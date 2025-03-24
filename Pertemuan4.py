import random
import datetime

skor_pengguna = []

def main():
    print("=== Permainan Tebak Angka ===")
    
    while True:
        angka_rahasia = random.randint(1, 10) 
        percobaan = 0
        
        while True:
            try:
                tebakan = int(input("Tebak angka (1-10): "))
                if tebakan < 1 or tebakan > 10:
                    print("Masukkan angka antara 1-10 saja!")
                    continue
                percobaan += 1
                
                if tebakan < angka_rahasia:
                    print("Terlalu rendah! Coba lagi.")
                elif tebakan > angka_rahasia:
                    print("Terlalu tinggi! Coba lagi.")
                else:
                    print(f"Selamat! Anda menebak dengan benar dalam {percobaan} percobaan.")
                    waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    skor_pengguna.append({"Percobaan": percobaan, "Waktu": waktu_sekarang})
                    break
            except ValueError:
                print("Masukkan angka yang valid!")

        tampilkan_skor()
        
        lanjut = input("Ingin bermain lagi? (y/n): ").lower()
        if lanjut != "y":
            print("Terima kasih sudah bermain! Sampai jumpa.")
            break

def tampilkan_skor():
    print("\n=== Riwayat Skor ===")
    if not skor_pengguna:
        print("Belum ada riwayat permainan.\n")
        return
    
    for i, skor in enumerate(skor_pengguna, start=1):
        print(f"{i}. Percobaan: {skor['Percobaan']}, Waktu: {skor['Waktu']}")
    print()

# Menjalankan program
if __name__ == "__main__":
    main()
