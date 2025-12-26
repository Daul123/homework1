n = input().strip()
count = 0

for i in range(len(n) - 4):
    if n[i:i+5] == ">>-->":
        count += 1
    if n[i:i+5] == "<--<<":
        count += 1

print(count)
