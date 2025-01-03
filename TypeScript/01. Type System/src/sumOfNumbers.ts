function sumOfNumbers(firstNum: string, secondNum: string): void {
  const start = parseInt(firstNum);
  const end = parseInt(secondNum);

  let sum = 0;

  for (let i = start; i <= end; i++) {
    sum += i;
  }
  console.log(sum);
}

sumOfNumbers("1", "5");
sumOfNumbers("-8", "20");
