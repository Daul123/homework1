import math

def nod(a, b):
    while b:
        a, b = b, a % b
    return a

print("НОД и НОК")
x = int(input("1 число: "))
y = int(input("2 число: "))

gcd_val = nod(x, y)
lcm_val = (x * y) // gcd_val

print(f"НОД{x}, {y}) = {gcd_val}")
print(f"НОК({x}, {y}) = {lcm_val}")

print("Площадь четырехугольника")
print("Введите 4 стороны и диагональ:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
diag = float(input("Диагональ: "))

p1 = (a + b + diag) / 2
s1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - diag))

p2 = (c + d + diag) / 2
s2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - diag))

print("Площадь:", s1 + s2)
