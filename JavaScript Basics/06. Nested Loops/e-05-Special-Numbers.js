function findSpecialNumbers(N) {
    let specialNumbers = [];
    
    for (let num = 1111; num <= 9999; num++) {
        let isSpecial = true;
        let numStr = num.toString();

        for (let digit of numStr) {
            let digitInt = parseInt(digit);

            if (digitInt === 0 || N % digitInt !== 0) {
                isSpecial = false;
                break;
            }
        }
        if (isSpecial) {
            specialNumbers.push(num);
        }
    }
    console.log(specialNumbers.join(" "));
}