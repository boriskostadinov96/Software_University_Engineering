function vacationPlan(budget, season) {
    let destination = "";
    let vacationType = "";
    let spentMoney = 0.0;

    if (budget <= 100) {
        destination = "Bulgaria";
        if (season === "summer") {
            vacationType = "Camp";
            spentMoney = budget * 0.30;
        } else if (season === "winter") {
            vacationType = "Hotel";
            spentMoney = budget * 0.70;
        }
    } else if (budget <= 1000) {
        destination = "Balkans";
        if (season === "summer") {
            vacationType = "Camp";
            spentMoney = budget * 0.40;
        } else if (season === "winter") {
            vacationType = "Hotel";
            spentMoney = budget * 0.80;
        }
    } else {
        destination = "Europe";
        vacationType = "Hotel";
        spentMoney = budget * 0.90;
    }

    console.log(`Somewhere in ${destination}`);
    console.log(`${vacationType} - ${spentMoney.toFixed(2)}`);
}


vacationPlan(50, "summer");
vacationPlan(75, "winter");
vacationPlan(312, "summer");
vacationPlan(678.53, "winter");
vacationPlan(1500, "summer");
