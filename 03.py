

# 1
l = int(input("Kuhan pituuden senttimetreinä: "))
if l<37: print(f"Pieni kuha, sinulta puuttuu: {37-l} cm.")

# 2
type = input("Laivan hyttiluokka: ")
if type == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif type == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif type == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif type == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

# 3
s = input("käyttäjän biologisen sukupuolen (Mies/Nainen): ")
h = int(input("käyttäjän hemoglobiiniarvon (g/l): "))
if s == "Nainen":
    if h < 117:
        print("Hemoglobiiniarvo alhainen")
    elif 117 <= h <= 175:
        print("Hemoglobiiniarvo normaali")
    elif h >= 175:
        print("Hemoglobiiniarvo korkea")
elif s == "Mies":
    if h < 134:
        print("Hemoglobiiniarvo alhainen")
    elif 134 <= h <= 195:
        print("Hemoglobiiniarvo normaali")
    elif h >= 195:
        print("Hemoglobiiniarvo korkea")

# 4
y = int(input("Vuosi: "))
if (y%4==0 and y%100!=0) or (y%100==0 and y%400==0):
    print("Vuosi on korkealla")
else:
    print("Se ei ole karkausvuosi")

