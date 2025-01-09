function solve(startNum: number, endNum: number): void {
  let totalSum = 0;
  let numbers = "";

  for (let i = startNum; i <= endNum; i++) {
    numbers += i + " ";
    totalSum += i;
  }

  console.log(numbers.trim());
  console.log(`Sum: ${totalSum}`);
}

solve(5, 10);
