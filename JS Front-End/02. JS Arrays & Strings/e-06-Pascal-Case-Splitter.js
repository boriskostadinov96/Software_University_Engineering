function splitPascalCase(inputString) {
    let words = inputString.match(/[A-Z][a-z]*/g);

    console.log(words.join(', '));

}

splitPascalCase('HoldTheDoor')
