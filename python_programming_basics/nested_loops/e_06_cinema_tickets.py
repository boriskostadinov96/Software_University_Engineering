student_tickets = 0
standard_tickets = 0
kid_tickets = 0
movie_name = input()

while movie_name != "Finish":
    free_seats = int(input())
    sold_tickets = 0

    for _ in range(free_seats):
        ticket = input()

        if ticket == "End":
            break

        elif ticket == "student":
            student_tickets += 1

        elif ticket == "standard":
            standard_tickets += 1

        elif ticket == "kid":
            kid_tickets += 1

        sold_tickets += 1

    hall_percentage = sold_tickets / free_seats * 100
    print(f"{movie_name} - {hall_percentage:.2f}% full.")

    movie_name = input()

total_sold_tickets = student_tickets + standard_tickets + kid_tickets
print(f"Total tickets: {total_sold_tickets}")
print(f"{student_tickets / total_sold_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_sold_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_sold_tickets * 100:.2f}% kids tickets.")