function sumVowels(text) {
    let sum = 0;
    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        if (char === 'a') {
            sum += 1;
        } else if (char === 'e') {
            sum += 2;
        } else if (char === 'i') {
            sum += 3;
        } else if (char === 'o') {
            sum += 4;
        } else if (char === 'u') {
            sum += 5;
        }
    }
    console.log(sum);
}

sumVowels("hello");
sumVowels("ice cream");