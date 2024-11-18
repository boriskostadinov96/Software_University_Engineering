function divisibleBy9(start, end) {
    let sum = 0;
    let numbers = [];
    
    for (let i = start; i <= end; i++) {
        if (i % 9 === 0) {
            sum += i;
            numbers.push(i);
        }
    }

    console.log(`The sum: ${sum}`);
    numbers.forEach(num => console.log(num));
}


divisibleBy9(100, 200);
