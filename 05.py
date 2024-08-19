# 1
import random

num_dice = int(input("Syötä noppien lukumäärä: "))
sum_dice = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    sum_dice += roll

print(f"Pisteiden summa: {sum_dice}")

# 2
numbers = []
while True:
    num = input("Kirjoita numero (tai viimeistele painamalla Enter):")
    if num == '':
        break
    numbers.append(int(num))

numbers.sort(reverse=True)
top_five = numbers[:5]
print("Viisi suurinta numeroa:", top_five)

# 3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Syötä kokonaisluku:"))
if is_prime(num):
    print(f"Luku {num} on alkuluku.")
else:
    print(f"Luku {num} ei ole alkuluku.")

# 4
cities = []
for i in range(5):
    city = input(f"Anna kaupungin nimi{i + 1}: ")
    cities.append(city)

print("Saapuneet kaupungit:")
for city in cities:
    print(city)
