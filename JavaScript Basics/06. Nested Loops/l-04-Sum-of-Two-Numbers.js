function findMagicCombination(start, end, magicNumber) {
    let combinationCount = 0;

    for (let i = start; i <= end; i++) {
        for (let j = start; j <= end; j++) {
            combinationCount++;
            if (i + j === magicNumber) {
                console.log(`Combination N:${combinationCount} (${i} + ${j} = ${magicNumber})`);
                return;
            }
        }
    }
    
    console.log(`${combinationCount} combinations - neither equals ${magicNumber}`);
}