function easterEggBattle(input) {
    let playerOneEggs = Number(input[0]);
    let playerTwoEggs = Number(input[1]);
    let index = 2;
    let command = input[index];

    while (command !== "End") {
        if (command === "one") {
            playerTwoEggs--;
        } else if (command === "two") {
            playerOneEggs--;
        }

        if (playerOneEggs === 0) {
            console.log(`Player one is out of eggs. Player two has ${playerTwoEggs} eggs left.`);
            return;
        }

        if (playerTwoEggs === 0) {
            console.log(`Player two is out of eggs. Player one has ${playerOneEggs} eggs left.`);
            return;
        }

        index++;
        command = input[index];
    }

    console.log(`Player one has ${playerOneEggs} eggs left.`);
    console.log(`Player two has ${playerTwoEggs} eggs left.`);
}