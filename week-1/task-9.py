ticket = input("Enter a ticket:")

first = sum(map(int, ticket[:3]))
last = sum(map(int, ticket[3:]))

if first == last:
    print("yes")
else:
    print("No")
