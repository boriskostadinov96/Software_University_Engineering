def team_lineup(*players_data):
    countries_and_players = {}

    for name, country in players_data:
        if not country in countries_and_players:
            countries_and_players[country] = []
        countries_and_players[country].append(name)

    result = ""

    sorted_players = sorted(countries_and_players.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for country, players in sorted_players:
        result += f"{country}:\n"
        for player_name in players:
            result += f"  -{player_name}\n"
    return result[:-1]


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
