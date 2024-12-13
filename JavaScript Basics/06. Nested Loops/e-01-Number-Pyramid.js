function printNumberPyramid(n) {
    let current = 1;
    let isDone = false;

    for (let row = 1; row <= n; row++) {
        let printCurrentLine = "";

        for (let col = 1; col <= row; col++) {
            if (current > n) {
                isDone = true;
                break;
            }
            printCurrentLine += current + " ";
            current++;
        }

        console.log(printCurrentLine.trim());

        if (isDone) {
            break;
        }
    }
}


printNumberPyramid(7);
printNumberPyramid(12);
printNumberPyramid(15);

