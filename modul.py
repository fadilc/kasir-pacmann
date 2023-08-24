class Transaction:
    """
    class Transaction dibuat untuk melakukan transaksi yang berisi list nama, jumlah, harga barang
    """

    def __init__(self):
        self.daftar_belanja = {}
        """
        dict daftar belanja (string) berisi daftar barang yang ditransaksikan
        """

    def tambah_barang(self, info_barang):
        try:
            nama, jumlah, harga = info_barang
            if nama not in self.daftar_belanja:
                self.daftar_belanja[nama] = [jumlah, harga]
            else:
                self.daftar_belanja[nama][0] += jumlah
        except ValueError:
            print("Silahkan input kembali yang benar")

        """
        menambahkan barang ke daftar belanja
        """

    def hapus_barang(self, nama):
        try:
            del self.daftar_belanja[nama]
        except KeyError:
            print(f"{nama} tidak ada dalam daftar belanja")

        """
        menghapus barang dari daftar belanja
        """

    def update_barang(self, nama, update_jumlah):
        try:
            self.daftar_belanja[nama][0] = update_jumlah
        except KeyError:
            print(f"{nama} tidak ada dalam daftar belanja ")

        """
        mengubah barang dari daftar belanja
        """

    def update_jumlah(self, nama, update_jumlah):
        try:
            self.daftar_belanja[nama][0] = update_jumlah
        except KeyError:
            print(f"{nama} tidak ada dalam daftar belanja ")

            """
            mengubah jumlah barang dari daftar belanja
            """

    def update_harga(self, nama, update_harga):
        try:
            self.daftar_belanja[nama][1] = update_harga
        except KeyError:
            print(f"{nama} tidak ada dalam daftar belanja ")

        """
        mengubah harga barang dari daftar belanja
        """

    def cek_belanja(self):
        if not self.daftar_belanja:
            print("keranjang masih kosong")
        else:
            print("===========Toko Andi Madura===========")
            print("-----------Daftar belanja anda------------")
            print("| No | Nama Barang | Jumlah | Harga | Total |")
            total_harga = 0
            for index, (nama, info_barang) in enumerate(self.daftar_belanja.items(), start=1):
                jumlah, harga = info_barang
                total = jumlah * harga
                print(f"{index} | {nama} | {jumlah} | {harga} | {total}|")
                total_harga += total
                print("*************************************************************")
                return total_harga

            """
            menampilkan daftar belanja
            """

    def total_harga(self):
        total_harga = self.cek_belanja()
        if total_harga:
            diskon = 0
            if total_harga > 200000:
                diskon = 0.05
            elif total_harga > 300000:
                diskon = 0.08
            elif total_harga > 500000:
                diskon = 0.10

            harga_setelah_diskon = total_harga - (total_harga * diskon)
            print(f"Total belanja anda sebesar Rp {harga_setelah_diskon}")

        """
        menampilkan nominal yang harus dibayar
        """

    def kembali(self):
        self.daftar_belanja = {}
