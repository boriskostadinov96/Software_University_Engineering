function calculateTotalCost(input) {
    const strawberryPricePerKg = Number(input[0]);
    const bananasKg = Number(input[1]);
    const orangesKg = Number(input[2]);
    const raspberriesKg = Number(input[3]);
    const strawberriesKg = Number(input[4]);

    const raspberryPricePerKg = strawberryPricePerKg / 2;
    const orangePricePerKg = raspberryPricePerKg * 0.6;
    const bananaPricePerKg = raspberryPricePerKg * 0.2;

    const raspberriesCost = raspberriesKg * raspberryPricePerKg;
    const orangesCost = orangesKg * orangePricePerKg;
    const bananasCost = bananasKg * bananaPricePerKg;
    const strawberriesCost = strawberriesKg * strawberryPricePerKg;
    const totalCost = raspberriesCost + orangesCost + bananasCost + strawberriesCost;

    console.log(totalCost.toFixed(2));
}

const input = [
    "48",
    "10",
    "3.3",
    "6.5",
    "1.7"
];

calculateTotalCost(input);
