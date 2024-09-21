function solve(first, second, third) {
    let totalTime = first + second + third;
    let minutes = Math.floor(totalTime / 60);
    let seconds = totalTime % 60;

    if(seconds < 10) {
        console.log(`${minutes}:0${seconds}`);
        
    } else {
        console.log(`${minutes}:${seconds}`);
        
    }
}