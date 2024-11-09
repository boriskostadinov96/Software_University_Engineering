function categorizeProduct(product) {
    const fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"];
    const vegetables = ["tomato", "cucumber", "pepper", "carrot"];

    if (fruits.includes(product)) {
        console.log("fruit");
    } else if (vegetables.includes(product)) {
        console.log("vegetable");
    } else {
        console.log("unknown");
    }
}


categorizeProduct("banana"); 