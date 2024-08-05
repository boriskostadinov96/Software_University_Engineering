function solve(numbers) {
    const sortedNumbers = numbers.sort((a, b) => a - b);
    const result = [];

    while (sortedNumbers.length > 0) {
        let firstNum = sortedNumbers.shift();
        let lastNum = sortedNumbers.pop();

        result.push(firstNum);

        if (lastNum !== undefined) {
            result.push(lastNum);
        }
    }

    return result;
}
