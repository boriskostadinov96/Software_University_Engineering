function validateNumber(number) {
    if (number < 100 || number > 200 && number !== 0) {
        console.log("invalid");
    }
}


validateNumber(75);