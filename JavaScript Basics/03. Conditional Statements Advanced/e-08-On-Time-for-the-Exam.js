function checkArrivalTime(examHour, examMinute, arrivalHour, arrivalMinute) {
    let examTimeInMinutes = examHour * 60 + examMinute;
    let arrivalTimeInMinutes = arrivalHour * 60 + arrivalMinute;

    
    let difference = arrivalTimeInMinutes - examTimeInMinutes;

    if (difference > 0) {
        console.log("Late");
        
        if (difference < 60) {
            console.log(`${difference} minutes after the start`);
        } 
        
        else {
            let hours = Math.floor(difference / 60);
            let minutes = difference % 60;
            console.log(`${hours}:${minutes.toString().padStart(2, '0')} hours after the start`);
        }
    } else if (difference >= -30) {
        console.log("On time");
        
        if (difference !== 0) {
            console.log(`${Math.abs(difference)} minutes before the start`);
        }
    } else {
        console.log("Early");
        
        if (difference > -60) {
            console.log(`${Math.abs(difference)} minutes before the start`);
        } 
        else {
            let hours = Math.floor(Math.abs(difference) / 60);
            let minutes = Math.abs(difference) % 60;
            console.log(`${hours}:${minutes.toString().padStart(2, '0')} hours before the start`);
        }
    }
}

checkArrivalTime(9, 30, 9, 50);
checkArrivalTime(9, 0, 10, 30);
checkArrivalTime(10, 0, 10, 0);
checkArrivalTime(9, 0, 8, 30);