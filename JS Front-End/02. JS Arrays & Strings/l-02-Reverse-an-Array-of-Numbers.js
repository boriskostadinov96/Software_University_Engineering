function processArray(number, elements) {
    let newArray = [];

    for (let el of elements) {
        newArray.push(el);

        if (newArray.length === number) {
            break;
        }
    }

    console.log(newArray.reverse().join(' '));
}

processArray(3, [10, 20, 30, 40, 50]);
