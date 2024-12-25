function petFoodStatistics(input) {
    const days = Number(input[0]);
    const totalFood = Number(input[1]);

    let totalDogFood = 0;
    let totalCatFood = 0;
    let totalBiscuits = 0;

    for (let i = 1; i <= days; i++) {
        const dogFood = Number(input[i * 2]);
        const catFood = Number(input[i * 2 + 1]);

        totalDogFood += dogFood;
        totalCatFood += catFood;

        if (i % 3 === 0) {
            totalBiscuits += Math.round((dogFood + catFood) * 0.1);
        }
    }

    const totalEatenFood = totalDogFood + totalCatFood;
    const percentEatenFood = (totalEatenFood / totalFood) * 100;
    const percentDogFood = (totalDogFood / totalEatenFood) * 100;
    const percentCatFood = (totalCatFood / totalEatenFood) * 100;

    console.log(`Total eaten biscuits: ${totalBiscuits}gr.`);
    console.log(`${percentEatenFood.toFixed(2)}% of the food has been eaten.`);
    console.log(`${percentDogFood.toFixed(2)}% eaten from the dog.`);
    console.log(`${percentCatFood.toFixed(2)}% eaten from the cat.`);
}

petFoodStatistics(input1);
petFoodStatistics(input2);
