function solve(year_tax) {
    let shoesPrice = year_tax * 0.6;
    let jersey = 0.8 * shoesPrice;
    let ball = jersey / 4;
    let otherStuff = ball / 5;
    
    result = year_tax +shoesPrice + jersey + ball + otherStuff;
    console.log(result);
}

solve(365)