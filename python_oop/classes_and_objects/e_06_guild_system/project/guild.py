from project import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return f"Player {player_name} has been kicked from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        player_info_list = [player.player_info() for player in self.players]
        players_info = "\n".join(player_info_list)
        return f"Guild: {self.name}\n{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
