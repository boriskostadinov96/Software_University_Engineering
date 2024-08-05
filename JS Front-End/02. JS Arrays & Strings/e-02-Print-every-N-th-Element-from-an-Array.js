function selectElements(arr, step) {
    let newList = [];
    for (let i = 0; i < arr.length; i += step) {
        newList.push(arr[i]);
    }
    return newList;
}

console.log(selectElements(['5', 
    '20', 
    '31', 
    '4', 
    '20'], 
    2
    ))