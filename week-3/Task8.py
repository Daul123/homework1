print("Числа, делящиеся на все свои цифры")
n = int(input("n: "))

print("Результат:", end=" ")
count = 0
for i in range(1, n + 1):
    s = str(i)
    ok = True
    for c in s:
        d = int(c)
        if d == 0 or i % d != 0:
            ok = False
            break
    if ok:
        print(i, end=" ")
        count += 1

print("Всего:", count)



print("Замена первого и последнего элемента")
m = int(input("Длина массива: "))
A = []
for i in range(m):
    A.append(int(input(f"Элемент {i}: ")))

print("До:", A)

if m > 1:
    A[0], A[-1] = A[-1], A[0]

print("После:", A)
