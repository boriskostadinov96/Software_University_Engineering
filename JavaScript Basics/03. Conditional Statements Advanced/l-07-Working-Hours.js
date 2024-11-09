function isOfficeOpen(hour, day) {
    const workingDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    
    if (workingDays.includes(day) && hour >= 10 && hour < 18) {
        console.log("open");
    } else {
        console.log("closed");
    }
}

isOfficeOpen(11, "Monday");
isOfficeOpen(19, "Friday");
isOfficeOpen(11, "Sunday");
