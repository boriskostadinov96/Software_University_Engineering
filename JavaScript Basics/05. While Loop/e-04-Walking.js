function walking(input) {
    let goal = 10000;
    let totalSteps = 0;
    let index = 0;

    while (index < input.length) {
        let command = input[index];
        index++;

        if (command === "Going home") {

            let homeSteps = Number(input[index]);
            totalSteps += homeSteps;
            break;
        
        } else {
            let steps = Number(command);
            totalSteps += steps;
        }

        if (totalSteps >= goal) {
            console.log("Goal reached! Good job!");
            console.log(`${totalSteps - goal} steps over the goal!`);
            return;
        }
    }

    if (totalSteps < goal) {
        console.log(`${goal - totalSteps} more steps to reach goal.`);
    } else {
        console.log("Goal reached! Good job!");
        console.log(`${totalSteps - goal} steps over the goal!`);
    }
}