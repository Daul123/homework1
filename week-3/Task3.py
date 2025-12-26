import math

print("1 треугольник 2 стороны:")
a1, b1 = map(int, input().split())

print("2 треугольник 2 стороны:")
a2, b2 = map(int, input().split())

h1 = math.sqrt(a1**2 + b1**2)
h2 = math.sqrt(a2**2 + b2**2)
print("Треугольник 1:", round(h1, 2), "Треугольник 2:", round(h2, 2))

if h1 > h2:
    print("Первый треугольник больше")
elif h2 > h1:
    print("Второй треугольник больше")
else:
    print("Треугольники равны")

print("Cортировка букв")
text = input("Введите текст: ")
result = ' '.join([''.join(sorted(w)) for w in text.split()])
print(f"'{text}' → '{result}'")
