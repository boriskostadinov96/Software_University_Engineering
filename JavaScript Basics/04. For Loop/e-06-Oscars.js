function calculateActorPoints(input) {
    const actorName = input[0];
    let totalPoints = Number(input[1]);
    const numberOfJudges = Number(input[2]);

    for (let i = 0; i < numberOfJudges; i++) {
        const judgeName = input[3 + i * 2];
        const judgePoints = Number(input[4 + i * 2]);
        const pointsFromJudge = (judgeName.length * judgePoints) / 2;
        
        totalPoints += pointsFromJudge;

        if (totalPoints > 1250.5) {
            console.log(
                `Congratulations, ${actorName} got a nominee for leading role with ${totalPoints.toFixed(1)}!`
            );
            return;
        }
    }

    const neededPoints = (1250.5 - totalPoints).toFixed(1);
    console.log(
        `Sorry, ${actorName} you need ${neededPoints} more!`
    );
}
