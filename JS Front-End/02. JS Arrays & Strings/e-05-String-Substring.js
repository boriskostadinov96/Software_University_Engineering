function findWord(word, text) {
    let lowerCaseWord = word.toLowerCase();
    let textArray = text.split(' ').map(x => x.toLowerCase());
    
    if (textArray.includes(lowerCaseWord)) {
        console.log(word);
    } else {
        console.log(`${word} not found!`);
    }
}
