countries = input().split(", ")
capitals = input().split(", ")

both = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in both.items():
    print(f"{country} -> {capital}")

# solution 2
# countries = input().split(", ")
# capitals = input().split(", ")
#
# both = {countries[index]: capitals[index] for index in range(len(countries))}
#
# for country, capital in both.items():
#     print(f"{country} -> {capital}")