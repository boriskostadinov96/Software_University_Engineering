record = float(input())
distance = float(input())
time_for_one_meter_distance = float(input())

total_time = distance * time_for_one_meter_distance
delay_time = int(distance / 15) * 12.5

result = total_time + delay_time

if result < record:
    print(f"Yes, he succeeded! The new world record is {result:.2f} seconds.")

else:
    print(f"No, he failed! He was {result - record:.2f} seconds slower.")
