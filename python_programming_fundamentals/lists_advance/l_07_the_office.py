employees_happiness = [int(x) for x in input().split()]
factor_happy = int(input())

employees_happiness = [num * factor_happy for num in employees_happiness]
average_happy = sum(employees_happiness) / len(employees_happiness)
happy_employees_count = len([el for el in employees_happiness if el >= average_happy])
half_employees_count = len(employees_happiness) / 2

if happy_employees_count >= half_employees_count:
    print(f"Score: {happy_employees_count}/{len(employees_happiness)}. Employees are happy!")

else:
    print(f"Score: {happy_employees_count}/{len(employees_happiness)}. Employees are not happy!")


