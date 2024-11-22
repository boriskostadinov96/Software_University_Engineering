function vendingMachineChange(change) {
    let coins = [200, 100, 50, 20, 10, 5, 2, 1];

    let changeInCents = Math.round(change * 100);
    let coinCount = 0;

    for (let coin of coins) {
        while (changeInCents >= coin) {
            changeInCents -= coin;
            coinCount++;
        }

        if (changeInCents === 0) {
            break;
        }
    }

    console.log(coinCount);
    return coinCount;
}