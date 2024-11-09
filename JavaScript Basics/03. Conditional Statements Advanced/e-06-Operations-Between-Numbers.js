function calculate(N1, N2, operator) {
    let result;

    if (operator === "+") {
        result = N1 + N2;
        let evenOrOdd = result % 2 === 0 ? "even" : "odd";
        console.log(`${N1} + ${N2} = ${result} - ${evenOrOdd}`);
    } 
    else if (operator === "-") {
        result = N1 - N2;
        let evenOrOdd = result % 2 === 0 ? "even" : "odd";
        console.log(`${N1} - ${N2} = ${result} - ${evenOrOdd}`);
    } 
    else if (operator === "*") {
        result = N1 * N2;
        let evenOrOdd = result % 2 === 0 ? "even" : "odd";
        console.log(`${N1} * ${N2} = ${result} - ${evenOrOdd}`);
    } 
    else if (operator === "/") {
        if (N2 === 0) {
            console.log(`Cannot divide ${N1} by zero`);
        } else {
            result = (N1 / N2).toFixed(2);
            console.log(`${N1} / ${N2} = ${result}`);
        }
    } 
    else if (operator === "%") {
        if (N2 === 0) {
            console.log(`Cannot divide ${N1} by zero`);
        } else {
            result = N1 % N2;
            console.log(`${N1} % ${N2} = ${result}`);
        }
    }
}

calculate(10, 12, "+");