command = input()
result = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")

    if company_name not in result:
        result[company_name] = [employee_id]

    else:
        if employee_id not in result[company_name]:
            result[company_name].append(employee_id)

    command = input()

for key, value in result.items():
    print(key)

    for v in value:
        print(f"-- {v}")