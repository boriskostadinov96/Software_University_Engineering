function sumUntilTarget(input) {
    let target = Number(input[0]);
    let sum = 0;
    let index = 1;

    while (sum < target) {
        sum += Number(input[index]);
        index++;
    }

    console.log(sum);
}