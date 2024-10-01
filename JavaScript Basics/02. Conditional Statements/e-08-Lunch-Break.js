function solve(name, episodeDuration, restDuration) {
    lunchTime = restDuration / 8;
    relaxTime = restDuration  / 4;

    timeLeft = restDuration - lunchTime - relaxTime;
    
    if (timeLeft >= episodeDuration) {
        time = timeLeft - episodeDuration
        console.log(`You have enough time to watch ${name} and left with ${Math.ceil(time)} minutes free time.`);
        
    } else {
        neededTime = episodeDuration - timeLeft
        console.log(`You don't have enough time to watch ${name}, you need ${Math.ceil(neededTime)} more minutes.`);
        
    } 

}

solve("Game of Thrones", 60, 96)