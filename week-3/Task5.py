def nod(a, b):
    while b:
        a, b = b, a % b
    return

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

chisl = A * D - C * B
znam = B * D
d = nod(chisl, znam)
chisl //= d
znam //= d
print("Результат:" chisl/znam)



n = int(input("Введите число: "))

print("Делители:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()
