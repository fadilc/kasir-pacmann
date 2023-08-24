from modul import Transaction


def main():
    print("-------Toko Andi Madura-------")
    print("silahkan masukkan barang belanja anda")
    transaksi = Transaction()
    while True:
        print("1. Tambah barang")
        print("2. Hapus barang")
        print("3. Cek keranjang")
        print("4. Ganti barang")
        print("5. Ganti jumlah barang")
        print("6. Ganti harga barang")
        print("7. kembali")
        print("8. keluar")
        try:
            pilihan = int(input("Masukan kode pilihan anda"))
            if pilihan == 1:
                nama = input("Masukan nama barang:")
                jumlah = input("Masukan jumlah barang:")
                harga = input("Masukan harga barang:")
                transaksi.tambah_barang([nama, jumlah, harga])
            elif pilihan == 2:
                nama = input("Masukan nama barang yg ingin dihapus:")
                transaksi.hapus_barang(nama)
            elif pilihan == 3:
                transaksi.cek_belanja()
            elif pilihan == 4:
                barang_lama = input("Masukkan barang yang ingin diganti:")
                barang_baru = input("Masukkan barang yang baru:")
                transaksi.update_barang(barang_lama, barang_baru)
            elif pilihan == 5:
                nama = input("Masukan barang yang ingin diperbaharui:")
                jumlah_baru = int(input("Masukan jumlah yang baru:"))
                transaksi.update_jumlah(nama, jumlah_baru)
            elif pilihan == 6:
                nama = input("Masukan harga barang yang ingin diperbaharui:")
                harga_baru = int(input("Masukan harga yang baru:"))
                transaksi.update_harga(nama, harga_baru)
            elif pilihan == 7:
                transaksi.kembali()
            elif pilihan == 8:
                print("Terima Kasih sudah berbelanja")
                break
            else:
                print("Silahkan coba lagi")
        except ValueError:
            print("Silahkan coba lagi")
        except Exception as e:
            print(e)

    if __name__ == "__main__":
        main()
