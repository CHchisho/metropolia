import math
import random

# 1
print(f'Terve, {input("Nimesi: ")}!')

# 2
print(f' {math.pi*float(input("Ympyrän säte: "))**2}')

# 3
a=float(input('a: '))
b=float(input('b: '))
print(f'Suorakulmion piirin ja pinta-alan = {(a+b)*2} ja {a*b}')

# 4
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
print(a+b+c, a*b*c, (a+b+c)/3)

# 5
a = float(input("Anna leiviskät.\n"))
b = float(input("Anna naulat.\n"))
c = float(input("Anna luodit.\n"))

print("Massa nykymittojen mukaan:")
s = (((a*20+b)*32)+c)*13.3
print(f'{int((s-s%1000)/1000)} kilogrammaa ja {round(s%1000,2)} grammaa. ')

# 6
print(random.randint(0,1000))
[print(random.randint(1,6),end="") for i in range(4)]