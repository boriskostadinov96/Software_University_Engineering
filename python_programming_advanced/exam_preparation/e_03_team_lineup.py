def team_lineup(*players_data):
    teams_data = {}

    for name, country in players_data:
        if country not in teams_data:
            teams_data[country] = [name]
        else:
            teams_data[country].append(name)

    result = ""

    sorted_data = sorted(teams_data.items(), key=lambda x: (-len(x[1]), x[0]))

    for c, players in sorted_data:
        result += f"{c}:\n"
        for p in players:
            result += f"  -{p}\n"

    return result


print(team_lineup(

   ("Harry Kane", "England"),

   ("Manuel Neuer", "Germany"),

   ("Raheem Sterling", "England"),

   ("Toni Kroos", "Germany"),

   ("Cristiano Ronaldo", "Portugal"),

   ("Thomas Muller", "Germany"),

   ("Bruno Fernandes", "Portugal"),

   ("Bernardo Silva", "Portugal"),

   ("Harry Maguire", "England")))
