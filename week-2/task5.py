letters = set("ABCEHKMOPTXY")

n = int(input())
for _ in range(n):
    s = input().strip()
    
    if (len(s) == 6 and
        s[0] in letters and
        s[1:4].isdigit() and  
        s[4] in letters and
        s[5] in letters):
        print("Yes")
    else:
        print("No")
