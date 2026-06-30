from datetime import datetime

# penambahan try except

katalog_menu = [
    # 1: Makanan Ringan
    [
        {'nama': "French Fries", 'harga': 25000, 'stok': 50, 'deskripsi': "Kentang goreng renyah dengan taburan garam laut."},
        {'nama': "Chicken Wings", 'harga': 35000, 'stok': 30, 'deskripsi': "Sayap ayam goreng dengan saus madu pedas."},
        {'nama': "Nachos Supreme", 'harga': 40000, 'stok': 20, 'deskripsi': "Keripik jagung dengan topping keju leleh dan salsa."},
        {'nama': "Fried Calamari", 'harga': 45000, 'stok': 15, 'deskripsi': "Cumi goreng tepung dengan saus tartar."},
        {'nama': "Garlic Bread", 'harga': 20000, 'stok': 40, 'deskripsi': "Roti panggang mentega bawang dan peterseli."},
        {'nama': "Spring Rolls", 'harga': 22000, 'stok': 35, 'deskripsi': "Lumpia isi sayuran dan ayam dengan saus asam manis."},
        {'nama': "Onion Rings", 'harga': 25000, 'stok': 45, 'deskripsi': "Bawang bombay goreng tepung renyah."},
        {'nama': "Tahu Cabai Garam", 'harga': 18000, 'stok': 50, 'deskripsi': "Tahu goreng krispi dengan bumbu cabai dan bawang."},
        {'nama': "Caesar Salad", 'harga': 38000, 'stok': 20, 'deskripsi': "Selada segar dengan saus caesar dan crouton."},
        {'nama': "Bruschetta", 'harga': 30000, 'stok': 25, 'deskripsi': "Roti panggang topping tomat segar dan basil."}
    ],
    # 2: Makanan Berat
    [
        {'nama': "Sirloin Steak", 'harga': 12000, 'stok': 15, 'deskripsi': "Daging sapi sirloin 200g dengan saus lada hitam."},
        {'nama': "Nasi Goreng Spesial", 'harga': 45000, 'stok': 60, 'deskripsi': "Nasi goreng dengan telur, ayam, dan kerupuk."},
        {'nama': "Grilled Salmon", 'harga': 110000, 'stok': 10, 'deskripsi': "Fillet salmon panggang dengan mashed potato."},
        {'nama': "Beef Burger", 'harga': 55000, 'stok': 25, 'deskripsi': "Burger sapi dengan keju cheddar dan sayuran."},
        {'nama': "Spaghetti Carbonara", 'harga': 50000, 'stok': 30, 'deskripsi': "Pasta dengan saus krim, keju, dan beef bacon."},
        {'nama': "Ayam Bakar Taliwang", 'harga': 48000, 'stok': 20, 'deskripsi': "Ayam bakar khas Lombok dengan bumbu pedas."},
        {'nama': "Fish and Chips", 'harga': 65000, 'stok': 20, 'deskripsi': "Ikan dori goreng tepung dengan kentang goreng."},
        {'nama': "Beef Kwetiau", 'harga': 42000, 'stok': 35, 'deskripsi': "Kwetiau goreng dengan irisan daging sapi empuk."},
        {'nama': "Chicken Parmigiana", 'harga': 60000, 'stok': 15, 'deskripsi': "Dada ayam goreng dengan saus tomat dan keju mozarela."},
        {'nama': "Lamb Chop", 'harga': 135000, 'stok': 8, 'deskripsi': "Iga domba bakar dengan saus rosemary."}
    ],
    # 3: Makanan Penutup (Dessert)
    [
        {'nama': "Chocolate Lava Cake", 'harga': 35000, 'stok': 12, 'deskripsi': "Kue cokelat hangat dengan cokelat leleh di dalam."},
        {'nama': "Tiramisu", 'harga': 38000, 'stok': 15, 'deskripsi': "Kue klasik Italia rasa kopi dan keju mascarpone."},
        {'nama': "New York Cheesecake", 'harga': 40000, 'stok': 10, 'deskripsi': "Kue keju lembut dengan selai stroberi."},
        {'nama': "Fruit Platter", 'harga': 25000, 'stok': 20, 'deskripsi': "Potongan buah musiman segar."},
        {'nama': "Vanilla Gelato", 'harga': 20000, 'stok': 40, 'deskripsi': "Es krim krimi rasa vanilla otentik."},
        {'nama': "Apple Pie", 'harga': 32000, 'stok': 15, 'deskripsi': "Pai apel panggang dengan taburan kayu manis."},
        {'nama': "Banana Split", 'harga': 35000, 'stok': 18, 'deskripsi': "Pisang dengan tiga varian es krim dan sirup."},
        {'nama': "Creme Brulee", 'harga': 30000, 'stok': 12, 'deskripsi': "Puding karamel dengan lapisan gula bakar."},
        {'nama': "Matcha Pudding", 'harga': 22000, 'stok': 25, 'deskripsi': "Puding lembut rasa teh hijau Jepang."},
        {'nama': "Brownies ala Mode", 'harga': 33000, 'stok': 20, 'deskripsi': "Brownies cokelat dengan satu scoop es krim vanilla."}
    ],
    # 4: Minuman
    [
        {'nama': "Iced Americano", 'harga': 25000, 'stok': 100, 'deskripsi': "Kopi hitam dingin dari biji kopi arabika."},
        {'nama': "Cafe Latte", 'harga': 30000, 'stok': 80, 'deskripsi': "Campuran espresso dan susu evaporasi."},
        {'nama': "Fresh Orange Juice", 'harga': 28000, 'stok': 40, 'deskripsi': "Perasan jeruk murni tanpa pemanis buatan."},
        {'nama': "Lychee Iced Tea", 'harga': 22000, 'stok': 60, 'deskripsi': "Teh es dengan buah leci segar."},
        {'nama': "Strawberry Smoothie", 'harga': 35000, 'stok': 25, 'deskripsi': "Campuran stroberi, yoghurt, dan madu."},
        {'nama': "Virgin Mojito", 'harga': 32000, 'stok': 30, 'deskripsi': "Minuman segar lime, mint, dan soda."},
        {'nama': "Hot Chocolate", 'harga': 30000, 'stok': 50, 'deskripsi': "Cokelat panas kental dengan marshmallow."},
        {'nama': "Mineral Water", 'harga': 10000, 'stok': 200, 'deskripsi': "Air mineral kemasan 600ml."},
        {'nama': "Thai Milk Tea", 'harga': 25000, 'stok': 45, 'deskripsi': "Teh khas Thailand dengan susu kental manis."},
        {'nama': "Avocado Juice", 'harga': 27000, 'stok': 20, 'deskripsi': "Jus alpukat kental dengan sirup cokelat."}
    ],
    # 5: Menu Tambahan
    [
        {'nama': "Nasi Putih", 'harga': 8000, 'stok': 100, 'deskripsi': "Satu porsi nasi putih hangat."},
        {'nama': "Telur Mata Sapi", 'harga': 7000, 'stok': 50, 'deskripsi': "Telur ayam goreng (ceplok)."},
        {'nama': "Mashed Potato", 'harga': 15000, 'stok': 30, 'deskripsi': "Kentang tumbuk lembut dengan mentega."},
        {'nama': "Sauteed Vegetables", 'harga': 12000, 'stok': 25, 'deskripsi': "Tumisan sayuran buncis dan wortel."},
        {'nama': "Extra Cheese", 'harga': 10000, 'stok': 60, 'deskripsi': "Tambahan keju mozarela atau cheddar."},
        {'nama': "Sambal Matah", 'harga': 5000, 'stok': 40, 'deskripsi': "Sambal iris khas Bali yang segar."},
        {'nama': "Garlic Rice", 'harga': 12000, 'stok': 30, 'deskripsi': "Nasi gurih dengan aroma bawang putih."},
        {'nama': "Kimchi", 'harga': 15000, 'stok': 20, 'deskripsi': "Sawi putih fermentasi pedas khas Korea."},
        {'nama': "Kerupuk Udang", 'harga': 5000, 'stok': 100, 'deskripsi': "Kerupuk renyah rasa udang."},
        {'nama': "Coleslaw", 'harga': 10000, 'stok': 25, 'deskripsi': "Irisan kol dan wortel dengan saus mayones."}
    ]
]

katalog = ["Makanan Ringan", "Makanan Berat", "Makanan Penutup", "Minuman", "Menu Tambahan"]
fitur_now = ["Kasir", "Dapur", "Gudang", "Exit"]
pembeli = []
nomor_order_global = 1

def print_fitur():
    print("\n=== SISTEM RESTORAN ===")
    for i, fitur in enumerate(fitur_now, start=1):
        print(f"{i}. {fitur}")

def gudang():
    while True:
        for i, m in enumerate(katalog, start=1):
            print(f"{i}. {m}")
        pilihan = int(input("Masukan Kategori (0 untuk kembali pilih fitur): "))
        print("\n")
        if pilihan == 0:
            break
        if 1 <= pilihan <= len(katalog):
            katalog_1 = katalog_menu[pilihan-1]
            for item in katalog_1:
                print(f"{item['nama']:<30} | {item['stok']}")
            print("\n")
            continue
        else:
            print("Kategori yang anda masukan tidak ada!")
            continue
        

def kasir():
    global nomor_order_global
    keranjang_saat_ini = []
    
    while True:
        print("\n--- Pilih Kategori (0 untuk Selesai/Bayar) ---")
        for i, m in enumerate(katalog, start=1):
            print(f"{i}. {m}")
        while True:
            try:
                pilih_kategori = int(input("Masukkan Kategori: "))
                break
            except ValueError:
                print("Input harus berupa angka!")
        if pilih_kategori == 0:
            break
            
        if 1 <= pilih_kategori <= len(katalog_menu):
            menu = katalog_menu[pilih_kategori-1]
            if not menu:
                print("Kategori ini belum memiliki menu.")
                continue
        else:
            print("Kategori tidak valid.")
            continue

        while True:
            print("\n--- Menu Produk (0 untuk Kembali ke Kategori) ---")
            header = f"{"No":<3} | {"Nama":<20} | {"Harga":<15} | {"Stok":<5} | {"Deskripsi":20}"
            print(header)
            print("-" * len(header))
            for i, p in enumerate(menu, start=1):
                print(f"{i:<3} | {p['nama']:<20} | {f"{p['harga']:,}":<15} | {p['stok']:<5} | {p['deskripsi']}")
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
                
                if item['stok'] <= 0:
                    print(f"Maaf, {item['nama']} sudah habis!")
                    continue
                while True:
                    while True:
                        try:
                            jumlah = int(input(f"Jumlah {item['nama']} (0 untuk batal): "))
                            break
                        except ValueError:
                            print("Input harus berupa angak!")
                    if jumlah == 0:
                        print("Batal memilih produk ini.")
                        break 
                    if jumlah > item["stok"]:
                        print(f"Stok tidak mencukupi! Sisa stok: {item['stok']}")
                        continue
                    if jumlah < 0:
                        print("Jumlah tidak valid!")
                        continue
                    
                    if pilih_kategori == 5:
                        note = "Tidak ada"
                    else:
                        note = input("Instruksi Khusus (opsional): ") or "Tidak ada"
                    
                    waktu_sekarang = datetime.now().strftime("%H:%M:%S")
                                           
                    data_order = {
                        "nomor_order": nomor_order_global,
                        "menu": item["nama"],
                        "harga": item["harga"],
                        "jumlah": jumlah,
                        "total": item["harga"] * jumlah,
                        "note": note,
                        "time" : waktu_sekarang,
                        "item_ref" : item
                    }
                    keranjang_saat_ini.append(data_order)
                    print(f"Berhasil menambahkan {item['nama']}.")
                    break
                
            else:
                print("Pilihan tidak tersedia.")

    if keranjang_saat_ini:
        print("\n" + "="*50)
        print(f"STRUK PEMBELIAN - Order #{nomor_order_global:0>4}")
        print("-" * 50)
        total_final = sum(order['total'] for order in keranjang_saat_ini)
        
        for order in keranjang_saat_ini:
            print(f"{order['menu']:<15} x{order['jumlah']:<3} Rp{order['total']:>10,}")
            order["item_ref"]["stok"] -= order["jumlah"]
            del order["item_ref"]
            
        pesanan_utuh = {
            "nomor_order" : nomor_order_global,
            "waktu" : keranjang_saat_ini[0]['time'],
            "items" : keranjang_saat_ini
        }
        pembeli.append(pesanan_utuh)
        print("-" * 50)
        print(f"Waktu: {pesanan_utuh['waktu']}")
        print(f"TOTAL BAYAR: Rp{total_final:,}")
        print("="*50)
        nomor_order_global += 1

def dapur():
    print("\n--- Antrean Pesanan ---")
    if not pembeli:
        print("Belum ada pesanan masuk.")
        return 
    
    for order_grup in pembeli:
        print(f"\n[ORDER #{order_grup['nomor_order']:0>4}] - Jam: {order_grup['waktu']}")
        header = f"{'Menu':<25} | {'Qty':<5} | {'Note':<20}"
        print(header)
        print("-" * len(header))
        for item in order_grup['items']:
            print(f"{item['menu']:<25} | {item['jumlah']:<5} | {item['note']:<20}")
    while True:        
        try:
            pilihan = int(input("\nMasukan Kode Pesanan Yang Sudah Selesai (0 Untuk Kembali): "))
            if pilihan == 0:
                return

            tertemu = False
            for index, order in enumerate(pembeli):
                if order['nomor_order'] == pilihan:
                    pembeli.pop(index) 
                    print(f"Pesanan #{pilihan:0>4} berhasil diselesaikan.")
                    tertemu = True
                    break 

            if not tertemu:
                print(f"Pembeli dengan Kode Pesanan {pilihan} Tidak ditemukan!")

        except ValueError:
            print("Input harus berupa angka!")

def main():
    while True:
        print_fitur()
        try:
            pilihan = int(input("Pilih Fitur: "))
            match pilihan:
                case 1:
                    kasir()
                case 2:
                    dapur()
                case 3:
                    gudang()
                case 4:
                    print("Terima kasih!")
                    break
                case _:
                    print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan angka 1-4!")

main()