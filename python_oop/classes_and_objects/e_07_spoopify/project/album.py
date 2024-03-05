from project import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, song: Song):
        pass
