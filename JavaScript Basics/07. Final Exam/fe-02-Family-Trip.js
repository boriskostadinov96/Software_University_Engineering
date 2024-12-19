function calculateVacationBudget(input) {
    const budget = Number(input[0]);
    const nights = Number(input[1]);
    let pricePerNight = Number(input[2]);
    const extraExpensesPercentage = Number(input[3]);

    if (nights > 7) {
        pricePerNight *= 0.95;
    }

    const totalCostForNights = nights * pricePerNight;
    const extraExpenses = (extraExpensesPercentage / 100) * budget;
    const totalCost = totalCostForNights + extraExpenses;

    if (totalCost <= budget) {
        const moneyLeft = budget - totalCost;
        console.log(`Ivanovi will be left with ${moneyLeft.toFixed(2)} leva after vacation.`);
    
    } else {
        const moneyNeeded = totalCost - budget;
        console.log(`${moneyNeeded.toFixed(2)} leva needed.`);
    }
}

const input = [
    "800.50",
    "8",
    "100",
    "2"
];

calculateVacationBudget(input);
