function calculateTicketStatistics(input) {
    let index = 0;
    let totalTickets = 0;
    let studentTickets = 0;
    let standardTickets = 0;
    let kidTickets = 0;

    while (input[index] !== "Finish") {
        let movie = input[index];
        index++;
        let availableSeats = Number(input[index]);
        index++;

        let soldTicketsForMovie = 0;
        while (input[index] !== "End" && input[index] !== "Finish") {
            let ticketType = input[index];
            index++;
            
            soldTicketsForMovie++;
            totalTickets++;

            if (ticketType === "student") {
                studentTickets++;
            } else if (ticketType === "standard") {
                standardTickets++;
            } else if (ticketType === "kid") {
                kidTickets++;
            }

            if (soldTicketsForMovie >= availableSeats) {
                break;
            }
        }

        let occupancyRate = (soldTicketsForMovie / availableSeats * 100).toFixed(2);
        console.log(`${movie} - ${occupancyRate}% full.`);

        if (input[index] === "End") {
            index++;
        }
    }

    console.log(`Total tickets: ${totalTickets}`);
    console.log(`${((studentTickets / totalTickets) * 100).toFixed(2)}% student tickets.`);
    console.log(`${((standardTickets / totalTickets) * 100).toFixed(2)}% standard tickets.`);
    console.log(`${((kidTickets / totalTickets) * 100).toFixed(2)}% kids tickets.`);
}


calculateTicketStatistics(input);
