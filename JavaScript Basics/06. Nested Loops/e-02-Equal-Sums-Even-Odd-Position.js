function printEqualSumsNumbers(start, end) {
    let result = "";

    for (let num = start; num <= end; num++) {
        let numAsString = num.toString();

        let sumOdd = 0;
        let sumEven = 0;

        for (let i = 0; i < numAsString.length; i++) {
            let digit = Number(numAsString[i]);

            if ((i + 1) % 2 === 0) {
                sumEven += digit;
            
            } else {
                sumOdd += digit;
            }
        }

        if (sumOdd === sumEven) {
            result += num + " ";
        }
    }

    console.log(result.trim());
}

printEqualSumsNumbers(100000, 100050);
printEqualSumsNumbers(123456, 124000);
printEqualSumsNumbers(299900, 300000);
printEqualSumsNumbers(100115, 100120);
