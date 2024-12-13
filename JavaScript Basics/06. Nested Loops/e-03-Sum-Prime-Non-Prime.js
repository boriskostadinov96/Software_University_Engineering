function sumPrimesAndNonPrimes(input) {
    let sumPrimes = 0;
    let sumNonPrimes = 0;

    for (let value of input) {
        if (value === "stop") {
            break;
        }

        let number = Number(value);

        if (number < 0) {
            console.log("Number is negative.");
            continue;
        }

        if (number === 0 || number === 1) {
            sumNonPrimes += number;
            continue;
        }

        let isPrime = true;

        for (let i = 2; i <= Math.sqrt(number); i++) {
            if (number % i === 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            sumPrimes += number;
        } else {
            sumNonPrimes += number;
        }
    }

    console.log(`Sum of all prime numbers is: ${sumPrimes}`);
    console.log(`Sum of all non prime numbers is: ${sumNonPrimes}`);
}

sumPrimesAndNonPrimes(["3", "9", "0", "7", "19", "4", "stop"]);
sumPrimesAndNonPrimes(["30", "83", "33", "-1", "20", "stop"]);
sumPrimesAndNonPrimes(["0", "-9", "0", "stop"]);
