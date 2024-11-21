function histogram(input) {
    const n = Number(input[0]);
    const numbers = input.slice(1).map(Number);

    let countP1 = 0;
    let countP2 = 0;
    let countP3 = 0;
    let countP4 = 0;
    let countP5 = 0;

    for (let num of numbers) {
        if (num < 200) {
            countP1++;
        } else if (num < 400) {
            countP2++;
        } else if (num < 600) {
            countP3++;
        } else if (num < 800) {
            countP4++;
        } else {
            countP5++;
        }
    }

    const p1 = (countP1 / n * 100).toFixed(2);
    const p2 = (countP2 / n * 100).toFixed(2);
    const p3 = (countP3 / n * 100).toFixed(2);
    const p4 = (countP4 / n * 100).toFixed(2);
    const p5 = (countP5 / n * 100).toFixed(2);

    console.log(`${p1}%`);
    console.log(`${p2}%`);
    console.log(`${p3}%`);
    console.log(`${p4}%`);
    console.log(`${p5}%`);
}


histogram(input);
