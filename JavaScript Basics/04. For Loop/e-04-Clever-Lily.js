function washingMachine(n, X, P) {
    let savedMoney = 0;
    let toyCount = 0;
    let brotherTake = 0;

    for (let i = 1; i <= n; i++) {
        if (i % 2 !== 0) {
            toyCount++;
        } else {
            let moneyFromBirthday = (i / 2) * 10;
            savedMoney += moneyFromBirthday;
            brotherTake += 1;
        }
    }

    savedMoney += toyCount * P;
    savedMoney -= brotherTake;


    if (savedMoney >= X) {
        console.log(`Yes! ${savedMoney.toFixed(2)}`);
    } else {
        let neededMoney = X - savedMoney;
        console.log(`No! ${neededMoney.toFixed(2)}`);
    }
}