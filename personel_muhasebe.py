import os
import datetime
import random

class PersonelMuhasebeModulu:
    def __init__(self):
        self.veri_klasoru = "veri"
        self.personel_dosya = f"{self.veri_klasoru}/personel.txt"
        self.nobet_dosya = f"{self.veri_klasoru}/nobet_cizelgesi.txt"
        self.muhasebe_dosya = f"{self.veri_klasoru}/mu"
