function solve(budget, statics, clothingPrice) {
    let decorPrice = budget * 0.1;
    let totalClothing = statics * clothingPrice;

    if (statics > 150) {
        totalClothing *= 0.9;
    }

    let totalPrice = decorPrice + totalClothing;

    if (budget >= totalPrice) {
        let moneyLeft = budget - totalPrice;
        console.log("Action!");
        console.log(`Wingard starts filming with ${moneyLeft.toFixed(2)} leva left.`);
    
    } else {
        let moneyNeeded = totalPrice - budget;
        console.log("Not enough money!");
        console.log(`Wingard needs ${moneyNeeded.toFixed(2)} leva more.`);
    }
}

solve(20000, 120, 55.5);
solve(15437.62, 186, 57.99);
solve(9587.88, 222, 55.68);