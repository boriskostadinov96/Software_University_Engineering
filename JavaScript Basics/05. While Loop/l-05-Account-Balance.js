function calculateAccount(input) {
    let index = 0;
    let total = 0;

    while (input[index] !== "NoMoreMoney") {
        let amount = parseFloat(input[index]);
        if (amount < 0) {
            console.log("Invalid operation!");
            break;
        }

        console.log(`Increase: ${amount.toFixed(2)}`);
        total += amount;
        index++;
    }

    console.log(`Total: ${total.toFixed(2)}`);
}

calculateAccount(["5.51", "69.42", "100", "NoMoreMoney"]);
calculateAccount(["120", "45.55", "-150"]);
