function solve(hour, minutes) {
    let totalMinutes = hour * 60 + minutes + 15;

    let totalHours = Math.floor(totalMinutes / 60);
    let newMinutes = totalMinutes % 60;

    if (totalHours >= 24) {
        totalHours = totalHours % 24;
    }

    if (newMinutes < 10) {
        console.log(`${totalHours}:0${newMinutes}`);
    } else {
        console.log(`${totalHours}:${newMinutes}`);
    }
}