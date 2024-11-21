function trekkingMania(input) {
    const groupsCount = Number(input[0]);
    let musala = 0;
    let montBlanc = 0;
    let kilimanjaro = 0;
    let k2 = 0;
    let everest = 0;
    let totalPeople = 0;

    for (let i = 1; i <= groupsCount; i++) {
        const groupSize = Number(input[i]);
        totalPeople += groupSize;

        if (groupSize <= 5) {
            musala += groupSize;
        } else if (groupSize <= 12) {
            montBlanc += groupSize;
        } else if (groupSize <= 25) {
            kilimanjaro += groupSize;
        } else if (groupSize <= 40) {
            k2 += groupSize;
        } else {
            everest += groupSize;
        }
    }

    const musalaPercent = ((musala / totalPeople) * 100).toFixed(2);
    const montBlancPercent = ((montBlanc / totalPeople) * 100).toFixed(2);
    const kilimanjaroPercent = ((kilimanjaro / totalPeople) * 100).toFixed(2);
    const k2Percent = ((k2 / totalPeople) * 100).toFixed(2);
    const everestPercent = ((everest / totalPeople) * 100).toFixed(2);

    console.log(`${musalaPercent}%`);
    console.log(`${montBlancPercent}%`);
    console.log(`${kilimanjaroPercent}%`);
    console.log(`${k2Percent}%`);
    console.log(`${everestPercent}%`);
}