function solve(tripPrice, puzzles, dolls, teddys, minions, trucs) {
    let toysPrice = puzzles * 2.6 + dolls * 3 + teddys * 4.1 + minions * 8.2 + trucs * 2;
    let toysCount = puzzles + dolls + teddys + minions + trucs;

    if(toysCount >= 50) {
        toysPrice *= 0.75;
    }

    toysPrice *= 0.9;

    if (toysPrice >= tripPrice) {
        let moneyLeft = toysPrice - tripPrice;
        console.log(`Yes! ${moneyLeft.toFixed(2)} lv left.`);
        
    } else {
        moneyNeeded = tripPrice - toysPrice
        console.log(`Not enough money! ${moneyNeeded.toFixed(2)} lv needed.`);
        
    }
}

solve(40.8,
    20,
    25,
    30,
    50,
    10
    )