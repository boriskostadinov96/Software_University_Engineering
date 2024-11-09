function fishingBoat(budget, season, fishermenCount) {
    let price = 0;

    if (season === "Spring") {
        price = 3000;
    } else if (season === "Summer" || season === "Autumn") {
        price = 4200;
    } else if (season === "Winter") {
        price = 2600;
    }

    if (fishermenCount <= 6) {
        price *= 0.90;
    } else if (fishermenCount <= 11) {
        price *= 0.85;
    } else {
        price *= 0.75;
    }

    if (fishermenCount % 2 === 0 && season !== "Autumn") {
        price *= 0.95;
    }

    if (budget >= price) {
        let remainingMoney = (budget - price).toFixed(2);
        console.log(`Yes! You have ${remainingMoney} leva left.`);
    } else {
        let neededMoney = (price - budget).toFixed(2);
        console.log(`Not enough money! You need ${neededMoney} leva.`);
    }
}

fishingBoat(3000, "Summer", 11);