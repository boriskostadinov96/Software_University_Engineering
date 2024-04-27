budget = float(input())
video_cards_count = int(input())
cpus_count = int(input())
ram_memory_count = int(input())

video_cards_sum = video_cards_count * 250
cpus_sum = cpus_count * video_cards_sum * 0.35
ram_memory_sum = ram_memory_count * video_cards_sum * 0.1

total_sum = video_cards_sum + cpus_sum + ram_memory_sum

if video_cards_count > cpus_count:
    total_sum -= total_sum * 0.15

if budget >= total_sum:
    print(f"You have {budget - total_sum:.2f} leva left!")

else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")
