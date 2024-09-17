function solve(length, width, height, percentage) {
    let area = length * width * height;
    let areaPercentage = area / 1000;
    let coveredSpace = percentage /100;

    let result = areaPercentage * (1 - coveredSpace);
    console.log(result);
}

solve(85,
    75,
    47,
    17
    )