function solve(record, distance, timePerMeter) {
    let totalTime = distance * timePerMeter;

    let slowdowns = Math.floor(distance / 15);
    let delayTime = slowdowns * 12.5; 

    totalTime += delayTime;

    if (totalTime < record) {
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`);
    
    } else {
        let timeDiff = totalTime - record;
        console.log(`No, he failed! He was ${timeDiff.toFixed(2)} seconds slower.`);
    }
}

solve(10464, 1500, 20);
solve(55555.67, 3017, 5.03);
