function solve(budget, numGPUs, numCPUs, numRAMs) {
    let gpuPrice = 250;
    let totalGPUPrice = numGPUs * gpuPrice;
    
    let cpuPrice = totalGPUPrice * 0.35;
    let ramPrice = totalGPUPrice * 0.10;

    let totalCPUPrice = numCPUs * cpuPrice;
    let totalRAMPrice = numRAMs * ramPrice;

    let totalPrice = totalGPUPrice + totalCPUPrice + totalRAMPrice;

    if (numGPUs > numCPUs) {
        totalPrice *= 0.85;
    }

    if (budget >= totalPrice) {
        let moneyLeft = budget - totalPrice;
        console.log(`You have ${moneyLeft.toFixed(2)} leva left!`);
    
    } else {
        let moneyNeeded = totalPrice - budget;
        console.log(`Not enough money! You need ${moneyNeeded.toFixed(2)} leva more!`);
    }
}

solve(900, 2, 1, 3);
solve(920.45, 3, 1, 1);
