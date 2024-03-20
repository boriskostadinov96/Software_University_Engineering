from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @property
    def musician_names(self):
        return [m.name for m in self.musicians]

    @property
    def band_names(self):
        return [b.name for b in self.bands]

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ("Guitarist", "Drummer", "Singer"):
            raise ValueError("Invalid musician type!")

        musician_names = [m.name for m in self.musicians]
        if name in musician_names:
            raise Exception(f"{name} is already a musician!")

        musician = None
        if musician_type == "Guitarist":
            musician = Guitarist(name, age)

        elif musician_type == "Drummer":
            musician = Drummer(name, age)

        elif musician_type == "Singer":
            musician = Singer(name, age)

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        bands_names = [b.name for b in self.bands]
        if name in bands_names:
            raise Exception(f"{name} band is already created!")

        b = Band(name)
        self.bands.append(b)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        existing_concerts = [c for c in self.concerts if c.place == place]
        if existing_concerts:
            raise Exception(f"{place} is already registered for {genre} concert!")

        c = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(c)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in self.musician_names:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in self.band_names:
            raise Exception(f"{band_name} isn't a band!")

        existing_musician = [m for m in self.musicians if m.name == musician_name][0]
        existing_band = [b for b in self.bands if b.name == band_name][0]

        existing_band.members.append(existing_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in self.band_names:
            raise Exception(f"{band_name} isn't a band!")

        existing_band = [b for b in self.bands if b.name == band_name][0]
        musicians = [m for m in existing_band.members if m.name == musician_name]
        if not musicians:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = musicians[0]
        existing_band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        singers = [m for m in band.members if isinstance(m, Singer)]
        drummers = [d for d in band.members if isinstance(d, Drummer)]
        guitarists = [g for g in band.members if isinstance(g, Guitarist)]

        if not (singers and not drummers and not guitarists):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        are_singers_correct = True
        for singer in singers:
            if concert.genre == "Rock":
                if "sing high pitch notes" not in singer.skills:
                    are_singers_correct = False

            elif concert.genre == "Metal":
                if concert.genre == "Metal":
                    if "sing low pitch notes" not in singer.skills:
                        are_singers_correct = False

            else:
                if "sing low pitch notes" not in singer.skills or "sing high pitch notes" not in singer.skills:
                    are_singers_correct = False

        are_drummers_correct = True
        for drummer in drummers:
            if concert.genre == "Rock":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers_correct = False

            elif concert.genre == "Metal":
                if concert.genre == "Metal":
                    if "play the drums with drumsticks" not in drummer.skills:
                        are_drummers_correct = False

            else:
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers_correct = False

        are_guitarists_correct = True
        for guitarist in guitarists:
            if concert.genre == "Rock":
                if "play rock" not in guitarist.skills:
                    are_guitarists_correct = False

            elif concert.genre == "Metal":
                if concert.genre == "Metal":
                    if "play metal" not in guitarist.skills:
                        are_guitarists_correct = False

            else:
                if "play jazz" not in guitarist.skills:
                    are_guitarists_correct = False

        if not are_guitarists_correct or not are_drummers_correct or not are_singers_correct:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
