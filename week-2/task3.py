s = input().strip()
n1 = s[0]
op = s[1]
n2 = s[2]
res = s[4]

if n1 == 'x':
    if op == '+':
        x = int(res) - int(n2)
    else:
        x = int(res) + int(n2)

elif n2 == 'x':
    if op == '+':
        x = int(res) - int(n1)
    else:
        x = int(n1) - int(res)

elif res == 'x':
    if op == '+':
        x = int(n1) + int(n2)
    else:
        x = int(n1) - int(n2)

print(x)

