function subtract() {
    let firstNumber = document.getElementById('firstNumber').value;
    let secondNumber = document.getElementById('secondNumber').value;

    firstNum = Number(firstNumber);
    secondNum = Number(secondNumber);

    let result = firstNumber - secondNumber;
    
    let elementResult = document.getElementById('result');
    elementResult.textContent = result;

}