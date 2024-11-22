function findMinNumber(input) {
    let index = 0;
    let minNumber = Number.POSITIVE_INFINITY;

    while (input[index] !== "Stop") {
        let number = parseInt(input[index]);

        if (number < minNumber) {
            minNumber = number;
        }

        index++;
    }

    console.log(minNumber);
}

findMinNumber(["100", "99", "80", "70", "Stop"]);
findMinNumber(["-10", "20", "-30", "Stop"]);
findMinNumber(["45", "-20", "7", "99", "Stop"]);
findMinNumber(["999", "Stop"]);
findMinNumber(["-1", "-2", "Stop"]);
