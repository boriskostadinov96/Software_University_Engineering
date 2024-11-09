function calculateFlowerCost(flowerType, flowerCount, budget) {
    let flowerPrice = 0;
    let totalPrice = 0;

    if (flowerType === "Roses") {
        flowerPrice = 5;
    } else if (flowerType === "Dahlias") {
        flowerPrice = 3.80;
    } else if (flowerType === "Tulips") {
        flowerPrice = 2.80;
    } else if (flowerType === "Narcissus") {
        flowerPrice = 3;
    } else if (flowerType === "Gladiolus") {
        flowerPrice = 2.50;
    }

    totalPrice = flowerPrice * flowerCount;

    if (flowerType === "Roses" && flowerCount > 80) {
        totalPrice *= 0.90;
    } else if (flowerType === "Dahlias" && flowerCount > 90) {
        totalPrice *= 0.85;
    } else if (flowerType === "Tulips" && flowerCount > 80) {
        totalPrice *= 0.85;
    } else if (flowerType === "Narcissus" && flowerCount < 120) {
        totalPrice *= 1.15;
    } else if (flowerType === "Gladiolus" && flowerCount < 80) {
        totalPrice *= 1.20;
    }

   
    if (budget >= totalPrice) {
        let remainingMoney = (budget - totalPrice).toFixed(2);
        console.log(`Hey, you have a great garden with ${flowerCount} ${flowerType} and ${remainingMoney} leva left.`);
    } else {
        let neededMoney = (totalPrice - budget).toFixed(2);
        console.log(`Not enough money, you need ${neededMoney} leva more.`);
    }
}


calculateFlowerCost("Roses", 55, 250);
calculateFlowerCost("Tulips", 88, 260);
calculateFlowerCost("Narcissus", 119, 360);
