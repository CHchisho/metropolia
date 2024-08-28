# 1

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1


h = Hissi(1, 10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)


# 2

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 1 <= hissin_numero <= len(self.hissit):
            hissi = self.hissit[hissin_numero - 1]
            print(f"Ajetaan hissiä {hissin_numero} kohteeseen kerros {kohde_kerros}:")
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero ei ole kelvollinen.")


talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)

# 3

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 1 <= hissin_numero <= len(self.hissit):
            hissi = self.hissit[hissin_numero - 1]
            print(f"Ajetaan hissiä {hissin_numero} kohteeseen kerros {kohde_kerros}:")
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero ei ole kelvollinen.")

    def palohälytys(self):
        print("Palohälytys!")
        for index, hissi in enumerate(self.hissit):
            # print(f"Ajetaan hissiä {index + 1} kohteeseen kerros {hissi.alin_kerros}:")
            hissi.siirry_kerrokseen(hissi.alin_kerros)


talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)

talo.palohälytys()

# 4
import random
from tabulate import tabulate


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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.tunti = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.change_tn(nopeuden_muutos)
            auto.kulje(1)
        self.tunti += 1

    def tulosta_tilanne(self):
        print(f"\nTilanne kilpailussa '{self.nimi}' tunnin {self.tunti} jälkeen:")
        print(tabulate(sorted(list(map(lambda x: vars(x).values(), self.autot)), key=lambda x: dict(zip([1, 2, 3, 4], x))[4],reverse=True),
                       headers=['Rekisteritunnus', 'Huippunopeus', "Nopeus", "Kuljettu matka"],
                       ))

    def kilpailu_ohi(self):
        return any(auto.kuljettu_matka >= self.pituus for auto in self.autot)


autot = [Auto(f'ABC-{i}', random.randint(100, 200)) for i in range(1, 11)]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()

    if kilpailu.tunti % 10 == 0 or kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()

# Lopullinen tulos
print("\nKilpailu on ohi!")
kilpailu.tulosta_tilanne()


