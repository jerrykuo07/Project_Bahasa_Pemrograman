from datetime import datetime

class Produk:
    def __init__(self, nama, harga, stok, deskripsi):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.deskripsi = deskripsi

    def kurangi_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        return False

class ItemKeranjang:
    def __init__(self, produk, jumlah, note="Tidak ada"):
        self.produk = produk 
        self.jumlah = jumlah
        self.note = note
        self.waktu = datetime.now().strftime("%H:%M:%S")

    def total_harga(self):
        return self.produk.harga * self.jumlah


class Order:
    def __init__(self, nomor_order, daftar_item):
        self.nomor_order = nomor_order
        self.daftar_item = daftar_item 
        self.waktu = daftar_item[0].waktu if daftar_item else ""

    def total_final(self):
        return sum(item.total_harga() for item in self.daftar_item)

    def tampilkan_struk(self):
        print("\n" + "="*50)
        print(f"STRUK PEMBELIAN - Order #{self.nomor_order:0>4}")
        print("-" * 50)
        for item in self.daftar_item:
            print(f"{item.produk.nama:<15} x{item.jumlah:<3} Rp{item.total_harga():>10,}")
            item.produk.kurangi_stok(item.jumlah)
        print("-" * 50)
        print(f"Waktu: {self.waktu}")
        print(f"TOTAL BAYAR: Rp{self.total_final():,}")
        print("="*50)


class Restoran:
    def __init__(self):
        self.fitur_now = ["Kasir", "Dapur", "Gudang", "Exit"]
        self.antrean_pembeli = []
        self.nomor_order_global = 1
        self.katalog_nama = ["Makanan Ringan", "Makanan Berat", "Makanan Penutup", "Minuman", "Menu Tambahan"]
        self.katalog_menu = [
            # 1: Makanan Ringan
            [
                Produk("French Fries", 25000, 50, "Kentang goreng renyah dengan taburan garam laut."),
                Produk("Chicken Wings", 35000, 30, "Sayap ayam goreng dengan saus madu pedas."),
                Produk("Nachos Supreme", 40000, 20, "Keripik jagung dengan topping keju leleh dan salsa."),
                Produk("Fried Calamari", 45000, 15, "Cumi goreng tepung dengan saus tartar."),
                Produk("Garlic Bread", 20000, 40, "Roti panggang mentega bawang dan peterseli."),
                Produk("Spring Rolls", 22000, 35, "Lumpia isi sayuran dan ayam dengan saus asam manis."),
                Produk("Onion Rings", 25000, 45, "Bawang bombay goreng tepung renyah."),
                Produk("Tahu Cabai Garam", 18000, 50, "Tahu goreng krispi dengan bumbu cabai dan bawang."),
                Produk("Caesar Salad", 38000, 20, "Selada segar dengan saus caesar dan crouton."),
                Produk("Bruschetta", 30000, 25, "Roti panggang topping tomat segar dan basil.")
            ],
            # 2: Makanan Berat
            [
                Produk("Sirloin Steak", 120000, 15, "Daging sapi sirloin 200g dengan saus lada hitam."),
                Produk("Nasi Goreng Spesial", 45000, 60, "Nasi goreng dengan telur, ayam, dan kerupuk."),
                Produk("Grilled Salmon", 110000, 10, "Fillet salmon panggang dengan mashed potato."),
                Produk("Beef Burger", 55000, 25, "Burger sapi dengan keju cheddar dan sayuran."),
                Produk("Spaghetti Carbonara", 50000, 30, "Pasta dengan saus krim, keju, dan beef bacon."),
                Produk("Ayam Bakar Taliwang", 48000, 20, "Ayam bakar khas Lombok dengan bumbu pedas."),
                Produk("Fish and Chips", 65000, 20, "Ikan dori goreng tepung dengan kentang goreng."),
                Produk("Beef Kwetiau", 42000, 35, "Kwetiau goreng dengan irisan daging sapi empuk."),
                Produk("Chicken Parmigiana", 60000, 15, "Dada ayam goreng dengan saus tomat dan keju mozarela."),
                Produk("Lamb Chop", 135000, 8, "Iga domba bakar dengan saus rosemary.")
            ],
            # 3: Makanan Penutup (Dessert)
            [
                Produk("Chocolate Lava Cake", 35000, 12, "Kue cokelat hangat dengan cokelat leleh di dalam."),
                Produk("Tiramisu", 38000, 15, "Kue klasik Italia rasa kopi dan keju mascarpone."),
                Produk("New York Cheesecake", 40000, 10, "Kue keju lembut dengan selai stroberi."),
                Produk("Fruit Platter", 25000, 20, "Potongan buah musiman segar."),
                Produk("Vanilla Gelato", 20000, 40, "Es krim krimi rasa vanilla otentik."),
                Produk("Apple Pie", 32000, 15, "Pai apel panggang dengan taburan kayu manis."),
                Produk("Banana Split", 35000, 18, "Pisang dengan tiga varian es krim dan sirup."),
                Produk("Creme Brulee", 30000, 12, "Puding karamel dengan lapisan gula bakar."),
                Produk("Matcha Pudding", 22000, 25, "Puding lembut rasa teh hijau Jepang."),
                Produk("Brownies ala Mode", 33000, 20, "Brownies cokelat dengan satu scoop es krim vanilla.")
            ],
            # 4: Minuman
            [
                Produk("Iced Americano", 25000, 100, "Kopi hitam dingin dari biji kopi arabika."),
                Produk("Cafe Latte", 30000, 80, "Campuran espresso dan susu evaporasi."),
                Produk("Fresh Orange Juice", 28000, 40, "Perasan jeruk murni tanpa pemanis buatan."),
                Produk("Lychee Iced Tea", 22000, 60, "Teh es dengan buah leci segar."),
                Produk("Strawberry Smoothie", 35000, 25, "Campuran stroberi, yoghurt, dan madu."),
                Produk("Virgin Mojito", 32000, 30, "Minuman segar lime, mint, dan soda."),
                Produk("Hot Chocolate", 30000, 50, "Cokelat panas kental dengan marshmallow."),
                Produk("Mineral Water", 10000, 200, "Air mineral kemasan 600ml."),
                Produk("Thai Milk Tea", 25000, 45, "Teh khas Thailand dengan susu kental manis."),
                Produk("Avocado Juice", 27000, 20, "Jus alpukat kental dengan sirup cokelat.")
            ],
            # 5: Menu Tambahan
            [
                Produk("Nasi Putih", 8000, 100, "Satu porsi nasi putih hangat."),
                Produk("Telur Mata Sapi", 7000, 50, "Telur ayam goreng (ceplok)."),
                Produk("Mashed Potato", 15000, 30, "Kentang tumbuk lembut dengan mentega."),
                Produk("Sauteed Vegetables", 12000, 25, "Tumisan sayuran buncis dan wortel."),
                Produk("Extra Cheese", 10000, 60, "Tambahan keju mozarela atau cheddar."),
                Produk("Sambal Matah", 5000, 40, "Sambal iris khas Bali yang segar."),
                Produk("Garlic Rice", 12000, 30, "Nasi gurih dengan aroma bawang putih."),
                Produk("Kimchi", 15000, 20, "Sawi putih fermentasi pedas khas Korea."),
                Produk("Kerupuk Udang", 5000, 100, "Kerupuk renyah rasa udang."),
                Produk("Coleslaw", 10000, 25, "Irisan kol dan wortel dengan saus mayones.")
            ]
        ]

    def print_fitur(self):
        print("\n=== SISTEM RESTORAN ===")
        for i, fitur in enumerate(self.fitur_now, start=1):
            print(f"{i}. {fitur}")

    def gudang(self):
        while True:
            for i, m in enumerate(self.katalog_nama, start=1):
                print(f"{i}. {m}")
            try:
                pilihan = int(input("Masukkan Kategori (0 untuk kembali pilih fitur): "))
            except ValueError:
                print("Input harus berupa angka!")
                continue
            
            print("\n")
            if pilihan == 0:
                break
            if 1 <= pilihan <= len(self.katalog_nama):
                menu_kategori = self.katalog_menu[pilihan-1]
                for item in menu_kategori:
                    print(f"{item.nama:<30} | {item.stok}")
                print("\n")
            else:
                print("Kategori yang anda masukkan tidak ada!")

    def kasir(self):
        keranjang_saat_ini = []
        
        while True:
            print("\n--- Pilih Kategori (0 untuk Selesai/Bayar) ---")
            for i, m in enumerate(self.katalog_nama, start=1):
                print(f"{i}. {m}")
            while True:
                try:
                    pilih_kategori = int(input("Masukkan Kategori: "))
                    break
                except ValueError:
                    print("Input harus berupa angka!")
            if pilih_kategori == 0:
                break
                
            if 1 <= pilih_kategori <= len(self.katalog_menu):
                menu = self.katalog_menu[pilih_kategori-1]
                if not menu:
                    print("Kategori ini belum memiliki menu.")
                    continue
            else:
                print("Kategori tidak valid.")
                continue

            while True:
                print("\n--- Menu Produk (0 untuk Kembali ke Kategori) ---")
                header = f"{'No':<3} | {'Nama':<20} | {'Harga':<15} | {'Stok':<5} | {'Deskripsi':20}"
                print(header)
                print("-" * len(header))
                for i, p in enumerate(menu, start=1):
                    print(f"{i:<3} | {p.nama:<20} | {f'{p.harga}:,':<15} | {p.stok:<5} | {p.deskripsi}")
                while True:
                    try:
                        pilihan = int(input("Pilih produk (nomor): "))
                        break
                    except ValueError:
                        print("Input harus berupa angka!")
                if pilihan == 0:
                    break
                
                if 1 <= pilihan <= len(menu):
                    item = menu[pilihan-1]
                    
                    if item.stok <= 0:
                        print(f"Maaf, {item.nama} sudah habis!")
                        continue
                    
                    while True:
                        try:
                            jumlah = int(input(f"Jumlah {item.nama} (0 untuk batal): "))
                        except ValueError:
                            print("Input harus berupa angka!")
                            continue
                        if jumlah == 0:
                            print("Batal memilih produk ini.")
                            break 
                        if jumlah > item.stok:
                            print(f"Stok tidak mencukupi! Sisa stok: {item.stok}")
                            continue
                        if jumlah < 0:
                            print("Jumlah tidak valid!")
                            continue
                        
                        note = "Tidak ada" if pilih_kategori == 5 else (input("Instruksi Khusus (opsional): ") or "Tidak ada")
                        
                        # Membuat objek ItemKeranjang
                        item_baru = ItemKeranjang(item, jumlah, note)
                        keranjang_saat_ini.append(item_baru)
                        print(f"Berhasil menambahkan {item.nama}.")
                        break
                else:
                    print("Pilihan tidak tersedia.")

        if keranjang_saat_ini:
            # Membuat objek Order baru
            order_baru = Order(self.nomor_order_global, keranjang_saat_ini)
            order_baru.tampilkan_struk()
            self.antrean_pembeli.append(order_baru)
            self.nomor_order_global += 1

    def dapur(self):
        print("\n--- Antrean Pesanan ---")
        if not self.antrean_pembeli:
            print("Belum ada pesanan masuk.")
            return 
        
        for order in self.antrean_pembeli:
            print(f"\n[ORDER #{order.nomor_order:0>4}] - Jam: {order.waktu}")
            header = f"{'Menu':<25} | {'Qty':<5} | {'Note':<20}"
            print(header)
            print("-" * len(header))
            for item in order.daftar_item:
                print(f"{item.produk.nama:<25} | {item.jumlah:<5} | {item.note:<20}")
        
        while True:        
            try:
                pilihan = int(input("\nMasukkan Kode Pesanan Yang Sudah Selesai (0 Untuk Kembali): "))
                if pilihan == 0:
                    return

                tertemu = False
                for index, order in enumerate(self.antrean_pembeli):
                    if order.nomor_order == pilihan:
                        self.antrean_pembeli.pop(index) 
                        print(f"Pesanan #{pilihan:0>4} berhasil diselesaikan.")
                        tertemu = True
                        break 

                if not tertemu:
                    print(f"Pembeli dengan Kode Pesanan {pilihan} Tidak ditemukan!")
            except ValueError:
                print("Input harus berupa angka!")

    def jalankan(self):
        while True:
            self.print_fitur()
            try:
                pilihan = int(input("Pilih Fitur: "))
                match pilihan:
                    case 1:
                        self.kasir()
                    case 2:
                        self.dapur()
                    case 3:
                        self.gudang()
                    case 4:
                        print("Terima kasih!")
                        break
                    case _:
                        print("Pilihan tidak valid.")
            except ValueError:
                print("Masukkan angka 1-4!")

app = Restoran()
app.jalankan()
