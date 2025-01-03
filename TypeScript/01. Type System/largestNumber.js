"use strict";
function largestNumber(firstNum, secondNum, thirdNum) {
    let largest = firstNum;
    if (secondNum > largest) {
        largest = secondNum;
    }
    if (thirdNum > largest) {
        largest = thirdNum;
    }
    console.log(`The largest number is ${largest}.`);
}
largestNumber(5, -3, 16);
largestNumber(-3, -5, -22.5);
