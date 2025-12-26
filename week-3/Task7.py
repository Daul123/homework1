print("Площадь четырехугольника с прямым углом")
X = float(input("X: "))
Y = float(input("Y: "))
Z = float(input("Z: "))
T = float(input("T: "))
diag = (X**2 + Y**2)**0.5
area1 = 0.5 * X * Y
p = (diag + Z + T) / 2
area2 = (p * (p - diag) * (p - Z) * (p - T))**0.5

print("Площадь:", area1 + area2)



print("10-значный восьмеричный код")
num = int(input("Chislo: "))
octal = oct(num)[2:]
result = octal.rjust(10, '0')
print("Результат:", result)
