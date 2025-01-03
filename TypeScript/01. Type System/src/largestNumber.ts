function largestNumber(
  firstNum: number,
  secondNum: number,
  thirdNum: number
): void {
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
