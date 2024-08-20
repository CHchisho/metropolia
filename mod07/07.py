# 1
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    vuodenaika = vuodenajat[kuukausi - 1]
    print(f"Kuukauden {kuukausi} vuodenaika on {vuodenaika}.")
else:
    print("Virheellinen kuukauden numero!")

# 2
nimet = set()
while True:
    nimi = input("Anna nimi (tai jätä tyhjä lopettaaksesi): ")
    if nimi == '':
        break
    # Tarkistetaan onko nimi uusi vai aiemmin syötetty
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

# Tulostetaan kaikki nimet
print("Syötetyt nimet:")
for nimi in nimet:
    print(nimi)

# 3
# Sanakirja ICAO-koodien ja lentoasemien nimien tallentamiseen
lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto: 1 - Syötä uusi lentoasema, 2 - Hae lentoaseman tiedot, 3 - Lopeta: ")

    if toiminto == '1':
        # Syötetään uusi lentoasema
        icao = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} lisätty ICAO-koodilla {icao}.")

    elif toiminto == '2':
        # Haetaan lentoaseman tiedot ICAO-koodin perusteella
        icao = input("Anna haettava ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"Lentoasema {icao} on {lentoasemat[icao]}.")
        else:
            print("Lentoaseman tietoja ei löytynyt.")

    elif toiminto == '3':
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta. Yritä uudelleen.")
