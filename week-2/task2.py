a = input()
b = input()
count = 0

for i in range(len(a) - len(b) + 1):
    sub = a[i:i+len(b)]
    if sub == b or sub == b[1:] + b[0]:
        count += 1

print(count)
