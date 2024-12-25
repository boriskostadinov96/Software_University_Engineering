function generateBarcodes(input) {
    const start = input[0];
    const end = input[1];

    let result = "";

    for (let i = Number(start[0]); i <= Number(end[0]); i++) {
        for (let j = Number(start[1]); j <= Number(end[1]); j++) {
            for (let k = Number(start[2]); k <= Number(end[2]); k++) {
                for (let l = Number(start[3]); l <= Number(end[3]); l++) {
                    if (i % 2 !== 0 && j % 2 !== 0 && k % 2 !== 0 && l % 2 !== 0) {
                        result += `${i}${j}${k}${l} `;
                    }
                }
            }
        }
    }

    console.log(result.trim());
}