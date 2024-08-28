# 1
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

new_auto = Auto("ABC-123",142)
print(vars(new_auto))

# 2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def change_tn(self, nopeuden_muutos):
        new_tn = self.tämänhetkinen_nopeus+nopeuden_muutos
        if new_tn > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif new_tn < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = new_tn
        # print(self.tämänhetkinen_nopeus)

new_auto = Auto("ABC-123", 142)

new_auto.change_tn(30)
new_auto.change_tn(70)
new_auto.change_tn(50)
print(new_auto.tämänhetkinen_nopeus)
new_auto.change_tn(-200)
print(new_auto.tämänhetkinen_nopeus)


# 3

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def change_tn(self, nopeuden_muutos):
        new_tn = self.tämänhetkinen_nopeus+nopeuden_muutos
        if new_tn > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif new_tn < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = new_tn
    def kulje(self, tunti):
        self.kuljettu_matka += self.tämänhetkinen_nopeus*tunti

new_auto = Auto("ABC-123", 142)

new_auto.change_tn(60)
new_auto.kulje(1.5)
print(new_auto.kuljettu_matka)

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
        new_tn = self.tämänhetkinen_nopeus+nopeuden_muutos
        if new_tn > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif new_tn < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = new_tn
    def kulje(self, tunti):
        self.kuljettu_matka += self.tämänhetkinen_nopeus*tunti

autot = [Auto(f'ABC-{i}',random.randint(100,200)) for i in range(1,11)]

t=0
while max(map(lambda x: x.kuljettu_matka,autot))<10000:
    t+=1
    print(f"Tunti: {t}, Max km = {max(map(lambda x: x.kuljettu_matka,autot))}, First: {list(filter(lambda x: x!=0, list(map((lambda x: x.rekisteritunnus if x.kuljettu_matka==max(map(lambda x: x.kuljettu_matka,autot)) else 0), autot))))[0]}")

    list(map(lambda x: [x.change_tn(random.randint(-10,15)),x.kulje(1)], autot))



print(tabulate(sorted(list(map(lambda x: vars(x).values(), autot)), key=lambda x: dict(zip([1,2,3,4], x))[4],reverse=True),
               headers=['Rekisteritunnus', 'Huippunopeus', "Nopeus","Kuljettu matka"],
               ))