function calculateSkiTripCost(days, roomType, feedback) {
    let nights = days - 1;
    let pricePerNight = 0;
    let discount = 0;

    if (roomType === "room for one person") {
        pricePerNight = 18.00;
    } else if (roomType === "apartment") {
        pricePerNight = 25.00;
        if (nights < 10) {
            discount = 0.30;
        } else if (nights <= 15) {
            discount = 0.35;
        } else {
            discount = 0.50;
        }
    } else if (roomType === "president apartment") {
        pricePerNight = 35.00;
        if (nights < 10) {
            discount = 0.10;
        } else if (nights <= 15) {
            discount = 0.15;
        } else {
            discount = 0.20;
        }
    }

    let totalCost = nights * pricePerNight * (1 - discount);

    if (feedback === "positive") {
        totalCost *= 1.25;
    } else if (feedback === "negative") {
        totalCost *= 0.90;
    }

    console.log(totalCost.toFixed(2));
}

calculateSkiTripCost(14, "apartment", "positive");
calculateSkiTripCost(30, "president apartment", "negative");
calculateSkiTripCost(12, "room for one person", "positive");
calculateSkiTripCost(2, "apartment", "positive");
