class Party:
    def __init__(self):
        self.people = []


party = Party()
names = input()

while names != 'End':
    party.people.append(names)

    names = input()

print(f"Going: {', '.join(p for p in party.people)}")
print(f"Total: {len(party.people)}")
