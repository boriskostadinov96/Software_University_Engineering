"use strict";
function dayOfWeek(day) {
    const daysMap = {
        Monday: 1,
        Tuesday: 2,
        Wednesday: 3,
        Thursday: 4,
        Friday: 5,
        Saturday: 6,
        Sunday: 7,
    };
    if (day in daysMap) {
        console.log(daysMap[day]);
    }
    else {
        console.log("error");
    }
}
dayOfWeek("Monday");
dayOfWeek("Friday");
dayOfWeek("Invalid");
