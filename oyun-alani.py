


# oyun_alani.py
import os
import datetime

class OyunAlaniModulu:
    def __init__(self):
        self.veri_klasoru = "veri"
        self.binisler_dosya = f"{self.veri_klasoru}/binisler.txt"
        
        # Dosya yoksa oluştur
        if not os.path.exists(self.veri_klasoru):
            os.makedirs(self.veri_klasoru)
        
        if not os.path.exists(self.binisler_dosya):
            with open(self.binisler_dosya, "w") as file:
                file.write("tarih,isim,soyisim,yas,oyun_adi,ucret\n")
    
    def oyunlar_listesi(self, yas):
        """Yaşa göre oyun listesi sunar"""
        tum_oyunlar = {
            "Dönme Dolap": {"min_yas": 3, "max_yas": 99, "ucret": 30},
            "Hız Treni": {"min_yas": 12, "max_yas": 99, "ucret": 50},
            "Su Kaydırağı": {"min_yas": 6, "max_yas": 99, "ucret": 40},
            "Çarpışan Arabalar": {"min_yas": 8, "max_yas": 99, "ucret": 35},
            "Mini Tren": {"min_yas": 2, "max_yas": 10, "ucret": 20},
            "Korku Evi": {"min_yas": 14, "max_yas": 99, "ucret": 45}
        }
        
        # Yaşa uygun oyunları filtrele
        uygun_oyunlar = {}
        for oyun, bilgi in tum_oyunlar.items():
            if bilgi["min_yas"] <= yas <= bilgi["max_yas"]:
                uygun_oyunlar[oyun] = bilgi
        
        return uygun_oyunlar
    
    def binis_kaydi(self, ziyaretci_bilgileri=None):
        """Oyun binişi kaydeder"""
        if ziyaretci_bilgileri is None:
            # Manuel bilgi girişi
            print("\n=== YENİ BİNİŞ KAYDI ===")
            isim = input("İsim: ")
            soyisim = input("Soyisim: ")
            
            while True:
                try:
                    yas = int(input("Yaş: "))
                    if yas <= 0 or yas > 120:
                        print("Geçerli bir yaş giriniz.")
                        continue
                    break
                except ValueError:
                    print("Lütfen sayısal bir değer giriniz.")
        else:
            # Giriş modülünden gelen bilgiler
            isim, soyisim, yas, _, _ = ziyaretci_bilgileri
        
        # Yaşa uygun oyunları listele
        uygun_oyunlar = self.oyunlar_listesi(yas)
        
        if not uygun_oyunlar:
            print(f"Üzgünüz, {yas} yaşına uygun oyun bulunmamaktadır.")
            return
        
        print(f"\n{isim} {soyisim} için uygun oyunlar:")
        for i, (oyun, bilgi) in enumerate(uygun_oyunlar.items(), 1):
            print(f"{i} - {oyun} (Ücret: {bilgi['ucret']} TL)")
        
        # Oyun seçimi
        while True:
            try:
                secim = int(input(f"Seçiminiz (1-{len(uygun_oyunlar)}): "))
                if secim < 1 or secim > len(uygun_oyunlar):
                    print(f"Geçerli bir seçenek giriniz (1-{len(uygun_oyunlar)}).")
                    continue
                break
            except ValueError:
                print("Lütfen sayısal bir değer giriniz.")
        
        # Seçilen oyun bilgileri
        secilen_oyun = list(uygun_oyunlar.keys())[secim-1]
        ucret = uygun_oyunlar[secilen_oyun]["ucret"]
        
        # Binişi kaydet
        tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.binisler_dosya, "a") as file:
            file.write(f"{tarih},{isim},{soyisim},{yas},{secilen_oyun},{ucret}\n")
        
        print(f"\nBiniş kaydı başarıyla oluşturuldu:")
        print(f"İsim: {isim} {soyisim}")
        print(f"Oyun: {secilen_oyun}")
        print(f"Ücret: {ucret} TL")