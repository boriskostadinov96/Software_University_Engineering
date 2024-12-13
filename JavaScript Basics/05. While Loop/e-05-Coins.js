function getMinimumCoins(change) {
    const coins = [200, 100, 50, 20, 10, 5, 2, 1];

    let remaining = Math.round(change * 100);

    let coinCount = 0;

    for (let coin of coins) {

        while (remaining >= coin) {
            remaining -= coin;
            coinCount++;
        }

        if (remaining === 0) break;
    }

    return coinCount;
}

console.log(getMinimumCoins(1.23));
console.log(getMinimumCoins(2));
console.log(getMinimumCoins(0.56));
console.log(getMinimumCoins(2.73)); 
