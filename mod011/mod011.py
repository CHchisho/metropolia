# 1

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}")



kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulosta_tiedot()
print()
lehti.tulosta_tiedot()

# 2
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def change_tn(self, nopeuden_muutos):
        new_tn = self.tämänhetkinen_nopeus + nopeuden_muutos
        if new_tn > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif new_tn < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = new_tn

    def kulje(self, tunti):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunti


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki_koko = bensatankki_koko


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.change_tn(150)
polttomoottoriauto.change_tn(120)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauto {sahkoauto.rekisteritunnus} on kulkenut {sahkoauto.kuljettu_matka} km.")
print(f"Polttomoottoriauto {polttomoottoriauto.rekisteritunnus} on kulkenut {polttomoottoriauto.kuljettu_matka} km.")
