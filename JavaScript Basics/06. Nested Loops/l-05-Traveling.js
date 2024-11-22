function travelDestinations(input) {
    let index = 0;
    
    while (input[index] !== "End") {
        let destination = input[index];
        let requiredBudget = Number(input[index + 1]);
        let currentSavedMoney = 0;
        index += 2;

        while (currentSavedMoney < requiredBudget) {
            let savedMoney = Number(input[index]);
            currentSavedMoney += savedMoney;
            index++;
        }

        console.log(`Going to ${destination}!`);
    }
}
