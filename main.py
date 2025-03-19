import os
import sys
from giris_modulu import GirisModulu
from oyun_alani import OyunAlaniModulu
from raporlama import RaporlamaModulu
from personel_muhasebe import PersonelMuhasebeModulu

def clear_screen():
    """Ekranı temizleme fonksiyonu (platform bağımsız)"""
    os.system('cls' if os.name == 'nt' else 'clear')


def ana_menu():
    """Ana menü fonksiyonu"""
    while True:
        clear_screen()
        print("\n===== OYUN PARKI YÖNETİM SİSTEMİ =====")
        print("1. Giriş İşlemleri")
        print("2. Oyun Alanı İşlemleri")
        print("3. Raporlama İşlemleri")
        print("4. Personel ve Muhasebe İşlemleri")
        print("0. Çıkış")

        secim = input("\nSeçiminiz: ")

        if secim == "1":
            giris_menu()
        elif secim == "2":
            oyun_alani_menu()
        elif secim == "3":
            raporlama_menu()
        elif secim == "4":
            personel_muhasebe_menu()
        elif secim == "0":
            print("\nProgramdan çıkılıyor...")
            sys.exit(0)
        else:
            input("Geçersiz seçim! Devam etmek için Enter'a basın...")


def giris_menu():
    """Giriş işlemleri menüsü"""
    giris_modulu = GirisModulu()

    while True:
        clear_screen()
        print("\n===== GİRİŞ İŞLEMLERİ =====")
        print("1. Yeni Ziyaretçi Kaydı")
        print("0. Ana Menüye Dön")

        secim = input("\nSeçiminiz: ")

        if secim == "1":
            ziyaretci_bilgileri = giris_modulu.yeni_ziyaretci_kaydi()

            # Ziyaretçi kaydından sonra oyun alanına yönlendirme seçeneği
            oyun_secimi = input("\nOyun alanı işlemlerine geçmek ister misiniz? (E/H): ")
            if oyun_secimi.upper() == "E":
                oyun_modulu = OyunAlaniModulu()
                oyun_modulu.binis_kaydi(ziyaretci_bilgileri)

            input("\nDevam etmek için Enter'a basın...")
        elif secim == "0":
            break
        else:
            input("Geçersiz seçim! Devam etmek için Enter'a basın...")


def oyun_alani_menu():
    """Oyun alanı işlemleri menüsü"""
    oyun_modulu = OyunAlaniModulu()

    while True:
        clear_screen()
        print("\n===== OYUN ALANI İŞLEMLERİ =====")
        print("1. Yeni Biniş Kaydı")
        print("0. Ana Menüye Dön")

        secim = input("\nSeçiminiz: ")

        if secim == "1":
            oyun_modulu.binis_kaydi()
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "0":
            break
        else:
            input("Geçersiz seçim! Devam etmek için Enter'a basın...")


def raporlama_menu():
    """Raporlama işlemleri menüsü"""
    rapor_modulu = RaporlamaModulu()

    while True:
        clear_screen()
        print("\n===== RAPORLAMA İŞLEMLERİ =====")
        print("1. Günlük Rapor")
        print("2. Haftalık Rapor")
        print("0. Ana Menüye Dön")

        secim = input("\nSeçiminiz: ")

        if secim == "1":
            rapor_modulu.gunluk_rapor()
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "2":
            rapor_modulu.haftalik_rapor()
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "0":
            break
        else:
            input("Geçersiz seçim! Devam etmek için Enter'a basın...")


def personel_muhasebe_menu():
    """Personel ve muhasebe işlemleri menüsü"""
    personel_modulu = PersonelMuhasebeModulu()

    while True:
        clear_screen()
        print("\n===== PERSONEL VE MUHASEBE İŞLEMLERİ =====")
        print("1. Personel Listesi")
        print("2. Yeni Personel Ekle")
        print("3. Nöbet Çizelgesi")
        print("4. Gelir-Gider Raporu")
        print("0. Ana Menüye Dön")

        secim = input("\nSeçiminiz: ")

        if secim == "1":
            personel_modulu.personel_listesi()
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "2":
            personel_modulu.yeni_personel_ekle()
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "3":
            personel_modulu.nobet_cizelgesi()
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "4":
            personel_modulu.gelir_gider_raporu()
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "0":
            break
        else:
            input("Geçersiz seçim! Devam etmek için Enter'a basın...")


if __name__ == "__main__":
    # Gerekli klasör yapısını oluştur
    if not os.path.exists("veri"):
        os.makedirs("veri")

    # Ana menüyü başlat
    ana_menu()