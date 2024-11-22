function findMaxNumber(input) {
    let index = 0;
    let maxNumber = Number.NEGATIVE_INFINITY;

    while (input[index] !== "Stop") {
        let number = parseInt(input[index]);

        if (number > maxNumber) {
            maxNumber = number;
        }

        index++;
    }

    console.log(maxNumber);
}

findMaxNumber(["100", "99", "80", "70", "Stop"]);
findMaxNumber(["-10", "20", "-30", "Stop"]);
findMaxNumber(["45", "-20", "7", "99", "Stop"]);
findMaxNumber(["999", "Stop"]);
findMaxNumber(["-1", "-2", "Stop"]);
