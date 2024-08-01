function sumDigits(num) {
    let textNum = num.toString();
    let sum_digits = 0;

    for (let i = 0; i < textNum.length; i++) {
        sum_digits += +textNum[i];
    }

    console.log(sum_digits);
}

sumDigits(543);
