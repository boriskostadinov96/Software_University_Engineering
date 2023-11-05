countries = input().split(", ")
capitals = input().split(", ")

final_result = {countries[index]: capitals[index] for index in range(len(countries))}

for countries, capitals in final_result.items():
    print(f"{countries} -> {capitals}")