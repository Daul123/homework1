salary1, salary2, salary3 = map(int, input("Enter 3 salaries: ").split())

max_salary = max(salary1, salary2, salary3)
min_salary = min(salary1, salary2, salary3)

difference = max_salary - min_salary

print(difference)
