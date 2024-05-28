deck_of_cards = input().split()
shuffles_count = int(input())

for _ in range(shuffles_count):
    middle_part = len(deck_of_cards) // 2

    left_part = deck_of_cards[:middle_part]
    right_part = deck_of_cards[middle_part:]
    deck_after_shuffling = []

    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])

    deck_of_cards = deck_after_shuffling

print(deck_of_cards)