function depositCalculator(depositSum, depositPeriod, yearPercentage) {
    let percentage = yearPercentage / 100;
    let result = depositSum + depositPeriod * ((depositSum * percentage) / 12);

    console.log(result);
}

depositCalculator(200,
    3,
    5.7 
    )