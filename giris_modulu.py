import os
import datetime


class GirisModulu:
    def __init__(self):
        self.veri_klasoru = "veri"
        self.ziyaretciler_dosya = f"{self.veri_klasoru}/ziyaretciler.txt"
        self.abonmanlar_dosya = f"{self.veri_klasoru}/abonmanlar.txt"

        # Veri klasörünü ve dosyalarını oluştur
        if not os.path.exists(self.veri_klasoru):
            os.makedirs(self.veri_klasoru)

        # Ziyaretçi dosyası yoksa oluştur
        if not os.path.exists(self.ziyaretciler_dosya):
            with open(self.ziyaretciler_dosya, "w") as file:
                file.write("tarih,isim,soyisim,yas,giris_tipi,ucret\n")

        # Abonman dosyası yoksa oluştur
        if not os.path.exists(self.abonmanlar_dosya):
            with open(self.abonmanlar_dosya, "w") as file:
                file.write("abonman_id,isim,soyisim,yas,baslangic_tarih,bitis_tarih,durum\n")

    def yeni_ziyaretci_kaydi(self):
        """Yeni ziyaretçi kaydı oluşturur"""
        print("\n=== YENİ ZİYARETÇİ KAYDI ===")
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")

        # Yaş girişi ve doğrulama
        while True:
            try:
                yas = int(input("Yaş: "))
                if yas <= 0 or yas > 120:
                    print("Geçerli bir yaş giriniz.")
                    continue
                break
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")

        # Giriş tipi seçimi
        print("\nGiriş Tipi Seçiniz:")
        print("1 - Abonman Kartlı")
        print("2 - Nakit")
        print("3 - QR Kart")
        print("4 - Günübirlik (Okul/Kuruluş)")

        while True:
            try:
                giris_tipi = int(input("Seçiminiz (1-4): "))
                if giris_tipi < 1 or giris_tipi > 4:
                    print("Geçerli bir seçenek giriniz (1-4).")
                    continue
                break
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")

        # Giriş tipine göre ücret hesaplama (basit örnek)
        ucret_tablosu = {1: 0, 2: 100, 3: 80, 4: 50}  # Abonman için 0 TL
        ucret = ucret_tablosu[giris_tipi]

        # Giriş tipini metin olarak kaydet
        giris_tipi_metinleri = {
            1: "Abonman Kartlı",
            2: "Nakit",
            3: "QR Kart",
            4: "Günübirlik"
        }

        tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Ziyaretçiyi kaydet
        with open(self.ziyaretciler_dosya, "a") as file:
            file.write(f"{tarih},{isim},{soyisim},{yas},{giris_tipi_metinleri[giris_tipi]},{ucret}\n")

        print(f"\nZiyaretçi kaydı başarıyla oluşturuldu.")
        print(f"İsim: {isim} {soyisim}")
        print(f"Yaş: {yas}")
        print(f"Giriş Tipi: {giris_tipi_metinleri[giris_tipi]}")
        print(f"Ücret: {ucret} TL")

        # Abonman kartı seçildiyse abonman işlemi yap
        if giris_tipi == 1:
            self.abonman_kontrol(isim, soyisim, yas)

        return isim, soyisim, yas, giris_tipi_metinleri[giris_tipi], ucret

    def abonman_kontrol(self, isim, soyisim, yas):
        """Abonman kartı kontrolü ve işlemleri"""
        abonman_id = input("Abonman Kart ID: ")

        # Abonman ID ile kayıt ara
        abonman_bulundu = False
        with open(self.abonmanlar_dosya, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Başlık satırını atla
                    continue
                veriler = line.strip().split(",")
                if veriler[0] == abonman_id:
                    abonman_bulundu = True
                    durum = veriler[6]
                    bitis_tarih = veriler[5]

                    # Abonman durumunu kontrol et
                    if durum == "Aktif":
                        bugun = datetime.datetime.now()
                        bitis = datetime.datetime.strptime(bitis_tarih, "%Y-%m-%d")

                        # Bitiş tarihi yaklaşıyorsa uyarı ver
                        kalan_gun = (bitis - bugun).days
                        if kalan_gun <= 7:
                            print(f"UYARI: Abonman süresi {kalan_gun} gün içinde dolacak!")

                        print(f"Abonman kartı geçerli. Giriş onaylandı.")
                    else:
                        print(f"Abonman kartı iptal edilmiş veya süresi dolmuş!")
                        self.abonman_yenile(abonman_id, lines, i)
                    break

        # Abonman bulunamadıysa yeni abonman oluştur
        if not abonman_bulundu:
            self.yeni_abonman_olustur(abonman_id, isim, soyisim, yas)

    def yeni_abonman_olustur(self, abonman_id, isim, soyisim, yas):
        """Yeni abonman kaydı oluşturur"""
        print("\n=== YENİ ABONMAN KAYDI ===")
        print(f"Kart ID: {abonman_id}")

        # Abonman süresi (basit örnek)
        baslangic_tarih = datetime.datetime.now().strftime("%Y-%m-%d")
        bitis_tarih = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        durum = "Aktif"

        # Abonmanı kaydet
        with open(self.abonmanlar_dosya, "a") as file:
            file.write(f"{abonman_id},{isim},{soyisim},{yas},{baslangic_tarih},{bitis_tarih},{durum}\n")

        print(f"Yeni abonman kaydı oluşturuldu.")
        print(f"Başlangıç: {baslangic_tarih}")
        print(f"Bitiş: {bitis_tarih}")

    def abonman_yenile(self, abonman_id, lines, line_index):
        """Süresi dolan abonmanı yeniler"""
        secim = input("Abonmanı yenilemek ister misiniz? (E/H): ")
        if secim.upper() == "E":
            veriler = lines[line_index].strip().split(",")
            baslangic_tarih = datetime.datetime.now().strftime("%Y-%m-%d")
            bitis_tarih = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")

            # Abonman bilgilerini güncelle
            veriler[4] = baslangic_tarih
            veriler[5] = bitis_tarih
            veriler[6] = "Aktif"
            lines[line_index] = ",".join(veriler) + "\n"

            # Dosyaya yaz
            with open(self.abonmanlar_dosya, "w") as file:
                file.writelines(lines)

            print(f"Abonman yenilendi!")
            print(f"Yeni Bitiş Tarihi: {bitis_tarih}")