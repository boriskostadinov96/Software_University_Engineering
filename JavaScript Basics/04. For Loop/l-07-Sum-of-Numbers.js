function sumOfDigits(n) {
    let sum = 0;
    for (let i = 0; i < n.length; i++) {
        sum += Number(n[i]);
    }
    console.log(`The sum of the digits is:${sum}`);
}


sumOfDigits("1234");
sumOfDigits("564891");

