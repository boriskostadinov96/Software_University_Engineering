function calculateMovieBudget(input) {
    const budget = Number(input[0]);
    const destination = input[1];
    const season = input[2];
    const days = Number(input[3]);

    let dailyRate;

    if (destination === "Dubai") {
        dailyRate = season === "Winter" ? 45000 : 40000;
    
    } else if (destination === "Sofia") {
        dailyRate = season === "Winter" ? 17000 : 12500;
    
    } else if (destination === "London") {
        dailyRate = season === "Winter" ? 24000 : 20250;
    }


    let totalCost = dailyRate * days;
    if (destination === "Dubai") {
        totalCost *= 0.7;
    
    } else if (destination === "Sofia") {
        totalCost *= 1.25;
    }

    if (budget >= totalCost) {
        const leftover = budget - totalCost;
        console.log(`The budget for the movie is enough! We have ${leftover.toFixed(2)} leva left!`);
    
    } else {
        const needed = totalCost - budget;
        console.log(`The director needs ${needed.toFixed(2)} leva more!`);
    }
}

const input = [
    "400000",
    "Sofia",
    "Winter",
    "20"
];

calculateMovieBudget(input);
