# 1
import random
def heita_noppaa():
    return random.randint(1, 6)

# Pääohjelma heittää noppaa kunnes saadaan kuutonen
while True:
    tulos = heita_noppaa()
    print(f"Nopan silmäluku: {tulos}")
    if tulos == 6:
        break

# 2
import random
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
maksimi = int(input("Anna nopan tahkojen määrä: "))

while True:
    tulos = heita_noppaa(maksimi)
    print(f"Nopan silmäluku: {tulos}")
    if tulos == maksimi:
        break

# 3
def muunna_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))
    if gallonat < 0:
        break
    litrat = muunna_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")

# 4
def laske_summa(numerot):
    return sum(numerot)

numerot = [1, 2, 3, 4, 5]
summa = laske_summa(numerot)
print(f"Listan summa on: {summa}")

# 5
def karsi_parittomat(numerot):
    return [num for num in numerot if num % 2 == 0]

numerot = [1, 2, 3, 4, 5, 6, 7, 8]
karsitut_numerot = karsi_parittomat(numerot)

print(f"Alkuperäinen lista: {numerot}")
print(f"Karsittu lista: {karsitut_numerot}")

# 6
import math
def laske_yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade / 100) ** 2  # Muutetaan pinta-ala neliömetreiksi
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

# Pääohjelma kysyy kahden pizzan tiedot ja vertaa yksikköhintoja
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (euroa): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (euroa): "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza on edullisempi.")
else:
    print("Toinen pizza on edullisempi.")


