function tennisRanklist(input) {
    const tournaments = Number(input[0]);
    let startingPoints = Number(input[1]);
    let totalPoints = startingPoints;
    let winCount = 0;
    let pointsFromTournaments = 0;

    for (let i = 2; i < 2 + tournaments; i++) {
        const result = input[i];
        if (result === "W") {
            totalPoints += 2000;
            pointsFromTournaments += 2000;
            winCount++;
        } else if (result === "F") {
            totalPoints += 1200;
            pointsFromTournaments += 1200;
        } else if (result === "SF") {
            totalPoints += 720;
            pointsFromTournaments += 720;
        }
    }

    const averagePoints = Math.floor(pointsFromTournaments / tournaments);
    const winPercentage = ((winCount / tournaments) * 100).toFixed(2);

    console.log(`Final points: ${totalPoints}`);
    console.log(`Average points: ${averagePoints}`);
    console.log(`${winPercentage}%`);
}