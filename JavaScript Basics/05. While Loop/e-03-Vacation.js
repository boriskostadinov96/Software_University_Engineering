function vacationSavings(input) {
    let goal = Number(input[0]);
    let currentMoney = Number(input[1]);
    let index = 2;

    let spendDays = 0;
    let totalDays = 0;

    while (currentMoney < goal) {
        let action = input[index];
        index++;
        let amount = Number(input[index]);
        index++;
        totalDays++;

        if (action === "spend") {
            spendDays++;
            currentMoney -= amount;
            if (currentMoney < 0) currentMoney = 0;
            if (spendDays === 5) {
                console.log("You can't save the money.");
                console.log(totalDays);
                return;
            }
        } else if (action === "save") {
            spendDays = 0;
            currentMoney += amount;
        }
    }

    console.log(`You saved the money for ${totalDays} days.`);
}