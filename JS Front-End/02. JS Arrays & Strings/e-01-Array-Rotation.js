function rotateArray(arr, rotations) {
    let deque = [...arr];
    
    for (let i = 0; i < rotations; i++) {
        let el = deque.shift();
        deque.push(el);
    }
    
    console.log(deque.join(' '));
}

rotateArray([2, 4, 15, 31], 5);

