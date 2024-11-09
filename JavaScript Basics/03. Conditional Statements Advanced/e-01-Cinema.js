function calculateIncome(projectionType, rows, columns) {
    let income = 0;
    let totalSeats = rows * columns;

    if (projectionType === "Premiere") {
        income = totalSeats * 12.00;
    } else if (projectionType === "Normal") {
        income = totalSeats * 7.50;
    } else if (projectionType === "Discount") {
        income = totalSeats * 5.00;
    } else {
        console.log("Invalid projection type");
        return;
    }

    console.log(`${income.toFixed(2)} leva`);
}

calculateIncome("Premiere", 10, 12);
calculateIncome("Normal", 21, 13);
calculateIncome("Discount", 12, 30);
