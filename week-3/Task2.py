import math

a = float(input("Сторона шестиугольника: "))
triangle = (math.sqrt(3) / 4) * a ** 2
hexagon = 6 * triangle
print("Площадь:", hexagon)

for i in range(1, 4):
    print("Прямоугольник:", i)
    x = float(input("  Сторона 1: "))
    y = float(input("  Сторона 2: "))
    print("Площадь:", x*y)
