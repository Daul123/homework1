print("Think of a number.")

step1 = int(input("Multiply your number by 5: "))
step2 = int(input("Add 8 to the result: "))
step3 = int(input("Multiply the result by 2: "))

number = (step3 // 2 - 8) // 5

print("The number you thought of is:", number)
