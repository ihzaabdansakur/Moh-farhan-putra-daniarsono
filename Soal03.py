def hitung_total_harga(jumlah_barang):
    total_harga = 100
    for i in range(jumlah_barang):
        harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
        total_harga += harga
    return total_harga

def main():
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    total_harga = hitung_total_harga(jumlah_barang)
    print(f"Total harga belanjaan adalah: {total_harga}")

if __name__ == "__main__":
    main()
