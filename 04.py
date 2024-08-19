import random

# 1
c=1
while c<=1000:
    if (c%3==0):
        print(c)
    c+=1

# 2
t = float(input("Tuuma: "))
while t>=0:
    print(" ≈", t*2.54, "cm")
    t = float(input("Tuuma: "))

# 3
new_n = input("Next number: ")
mas_n = []
while len(new_n)>0:
    mas_n.append(int(new_n))
    new_n = input("Next number: ")
print(f"Max: {max(mas_n)}, Min: {min(mas_n)}")

# 4
number = random.randint(1,10)
print(number)
user_number = int(input("Enter number: "))
while number!=user_number:
    if user_number>number:
        print("Liian suuri arvaus")
    elif user_number<number:
        print("Liian pieni arvaus")
    user_number = int(input("Enter number: "))
print("Oikein")

# 5
login = input("Login: ")
password = input("Password: ")
while login!="python" and password!="rules":
    print("Pääsy evätty")
    login = input("Login: ")
    password = input("Password: ")
print("Tervetuloa")

# 6
def arvioi_pi(pisteiden_maara):
    ympyran_sisalla = 0

    for _ in range(pisteiden_maara):
        # Arvotaan satunnaispisteet x ja y välillä [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Testataan, onko piste yksikköympyrän sisällä
        if x ** 2 + y ** 2 < 1:
            ympyran_sisalla += 1

    # Piin likiarvo kaavalla π ≈ 4 * ympyrän_sisällä / pisteiden_maara
    pi_likiarvo = 4 * ympyran_sisalla / pisteiden_maara
    return pi_likiarvo


pisteiden_maara = int(input("Anna arvottavien pisteiden määrä: "))
pi_arvio = arvioi_pi(pisteiden_maara)
print(f"Piin likiarvo {pisteiden_maara} pisteellä arvioituna on noin: {pi_arvio}")

