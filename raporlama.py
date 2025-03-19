# raporlama.py
import os
import datetime
from collections import defaultdict

class RaporlamaModulu:
    def __init__(self):
        self.veri_klasoru = "veri"
        self.ziyaretciler_dosya = f"{self.veri_klasoru}/ziyaretciler.txt"
        self.abonmanlar_dosya = f"{self.veri_klasoru}/abonmanlar.txt"
        self.binisler_dosya = f"{self.veri_klasoru}/binisler.txt"
    
    def gunluk_rapor(self):
        """Günlük ziyaretçi ve gelir raporu oluşturur"""
        bugun = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Günlük ziyaretçiler
        ziyaretci_sayisi = 0
        toplam_gelir = 0
        
        try:
            with open(self.ziyaretciler_dosya, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i == 0:  # Başlık satırını atla
                        continue
                    
                    veriler = line.strip().split(",")
                    tarih = veriler[0].split()[0]  # Tarih kısmını al
                    
                    if tarih == bugun:
                        ziyaretci_sayisi += 1
                        toplam_gelir += float(veriler[5])  # Ücret
        except FileNotFoundError:
            print("Ziyaretçiler dosyası bulunamadı.")
        
        # Günlük binişler
        binis_sayisi = 0
        binis_geliri = 0
        
        try:
            with open(self.binisler_dosya, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i == 0:  # Başlık satırını atla
                        continue
                    
                    veriler = line.strip().split(",")
                    tarih = veriler[0].split()[0]  # Tarih kısmını al
                    
                    if tarih == bugun:
                        binis_sayisi += 1
                        binis_geliri += float(veriler[5])  # Ücret
        except FileNotFoundError:
            print("Binişler dosyası bulunamadı.")
        
        # Raporu ekrana yazdır
        print("\n=== GÜNLÜK RAPOR ===")
        print(f"Tarih: {bugun}")
        print(f"Toplam Ziyaretçi: {ziyaretci_sayisi}")
        print(f"Ziyaretçi Geliri: {toplam_gelir} TL")
        print(f"Toplam Biniş: {binis_sayisi}")
        print(f"Biniş Geliri: {binis_geliri} TL")
        print(f"Toplam Gelir: {toplam_gelir + binis_geliri} TL")
        
        # Raporu dosyaya kaydet
        rapor_dosya = f"{self.veri_klasoru}/rapor_{bugun}.txt"
        with open(rapor_dosya, "w") as file:
            file.write(f"=== GÜNLÜK RAPOR ===\n")
            file.write(f"Tarih: {bugun}\n")
            file.write(f"Toplam Ziyaretçi: {ziyaretci_sayisi}\n")
            file.write(f"Ziyaretçi Geliri: {toplam_gelir} TL\n")
            file.write(f"Toplam Biniş: {binis_sayisi}\n")
            file.write(f"Biniş Geliri: {binis_geliri} TL\n")
            file.write(f"Toplam Gelir: {toplam_gelir + binis_geliri} TL\n")
        
        print(f"\nRapor '{rapor_dosya}' dosyasına kaydedildi.")
    
    def haftalik_rapor(self):
        """Haftalık ziyaretçi ve gelir raporu oluşturur"""
        bugun = datetime.datetime.now()
        bir_hafta_once = bugun - datetime.timedelta(days=7)
        
        # Günlere göre verileri topla
        gunluk_veriler = defaultdict(lambda: {"ziyaretci": 0, "ziyaretci_gelir": 0, "binis": 0, "binis_gelir": 0})
        
        # Ziyaretçi verilerini topla
        try:
            with open(self.ziyaretciler_dosya, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i == 0:  # Başlık satırını atla
                        continue
                    
                    veriler = line.strip().split(",")
                    tarih_str = veriler[0].split()[0]  # Tarih kısmını al
                    tarih = datetime.datetime.strptime(tarih_str, "%Y-%m-%d")
                    
                    if bir_hafta_once <= tarih <= bugun:
                        gunluk_veriler[tarih_str]["ziyaretci"] += 1
                        gunluk_veriler[tarih_str]["ziyaretci_gelir"] += float(veriler[5])  # Ücret
        except FileNotFoundError:
            print("Ziyaretçiler dosyası bulunamadı.")
        
        # Biniş verilerini topla
        try:
            with open(self.binisler_dosya, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i == 0:  # Başlık satırını atla
                        continue
                    
                    veriler = line.strip().split(",")
                    tarih_str = veriler[0].split()[0]  # Tarih kısmını al
                    tarih = datetime.datetime.strptime(tarih_str, "%Y-%m-%d")
                    
                    if bir_hafta_once <= tarih <= bugun:
                        gunluk_veriler[tarih_str]["binis"] += 1
                        gunluk_veriler[tarih_str]["binis_gelir"] += float(veriler[5])  # Ücret
        except FileNotFoundError:
            print("Binişler dosyası bulunamadı.")
        
        # Raporu ekrana yazdır
        print("\n=== HAFTALIK RAPOR ===")
        print(f"Tarih Aralığı: {bir_hafta_once.strftime('%Y-%m-%d')} - {bugun.strftime('%Y-%m-%d')}")
        
        toplam_ziyaretci = 0
        toplam_ziyaretci_gelir = 0
        toplam_binis = 0
        toplam_binis_gelir = 0
        
        for tarih in sorted(gunluk_veriler.keys()):
            veri = gunluk_veriler[tarih]
            print(f"\nTarih: {tarih}")
            print(f"  Ziyaretçi: {veri['ziyaretci']}")
            print(f"  Ziyaretçi Geliri: {veri['ziyaretci_gelir']} TL")
            print(f"  Biniş: {veri['binis']}")
            print(f"  Biniş Geliri: {veri['binis_gelir']} TL")
            print(f"  Günlük Toplam: {veri['ziyaretci_gelir'] + veri['binis_gelir']} TL")
            
            toplam_ziyaretci += veri['ziyaretci']
            toplam_ziyaretci_gelir += veri['ziyaretci_gelir']
            toplam_binis += veri['binis']
            toplam_binis_gelir += veri['binis_gelir']
        
        print("\n=== HAFTALIK ÖZET ===")
        print(f"Toplam Ziyaretçi: {toplam_ziyaretci}")
        print(f"Toplam Ziyaretçi Geliri: {toplam_ziyaretci_gelir} TL")
        print(f"Toplam Biniş: {toplam_binis}")
        print(f"Toplam Biniş Geliri: {toplam_binis_gelir} TL")
        print(f"Haftalık Toplam Gelir: {toplam_ziyaretci_gelir + toplam_binis_gelir} TL")
        
        # Raporu dosyaya kaydet
        rapor_dosya = f"{self.veri_klasoru}/haftalik_rapor_{bugun.strftime('%Y-%m-%d')}.txt"
        with open(rapor_dosya, "w") as file:
            file.write(f"=== HAFTALIK RAPOR ===\n")
            file.write(f"Tarih Aralığı: {bir_hafta_once.strftime('%Y-%m-%d')} - {bugun.strftime('%Y-%m-%d')}\n\n")
            
            for tarih in sorted(gunluk_veriler.keys()):
                veri = gunluk_veriler[tarih]
                file.write(f"Tarih: {tarih}\n")
                file.write(f"  Ziyaretçi: {veri['ziyaretci']}\n")
                file.write(f"  Ziyaretçi Geliri: {veri['ziyaretci_gelir']} TL\n")
                file.write(f"  Biniş: {veri['binis']}\n")
                file.write(f"  Biniş Geliri: {veri['binis_gelir']} TL\n")
                file.write(f"  Günlük Toplam: {veri['ziyaretci_gelir'] + veri['binis_gelir']} TL\n\n")
            
            file.write("=== HAFTALIK ÖZET ===\n")
            file.write(f"Toplam Ziyaretçi: {toplam_ziyaretci}\n")
            file.write(f"Toplam Ziyaretçi Geliri: {toplam_ziyaretci_gelir} TL\n")
            file.write(f"Toplam Biniş: {toplam_binis}\n")
            file.write(f"Toplam Biniş Geliri: {toplam_binis_gelir} TL\n")
            file.write(f"Haftalık Toplam Gelir: {toplam_ziyaretci_gelir + toplam_binis_gelir} TL\n")
        
        print(f"\nRapor '{rapor_dosya}' dosyasına kydedildi.")





