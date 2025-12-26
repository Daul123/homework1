import math

def nod(x, y):
    while y:
        x, y = y, x % y
    return x

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))

chisl = A * D
znam = B * C

d = nod(chisl, znam)
chisl //= d
znam //= d

print("Результат:", chisl/znam)

print("Точки в окружности")
a = float(input("a = "))
b = float(input("b = "))
R = float(input("R = "))

points = []
for name in ['P', 'F', 'L']:
    print("Точка:", name)
    x = float(input("  {name}1 = "))
    y = float(input("  {name}2 = "))
    points.append((x, y))

count = 0
for x, y in points:
    if (x-a)**2 + (y-b)**2 < R**2:
        count += 1

print("Точек внутри окружности:", count)
