def all_eq(lst):
    maxl = 0
    for i in lst:
        if len(i) > maxl:
            maxl = len(i)
    result = []
    for i in lst:
        if len(i) < maxl:
            i = i + "_" * (maxl - len(i))
        result.append(i)
    return result

n = input(": ")
words = n.split()  

result = all_eq(words)
print(":", result)
