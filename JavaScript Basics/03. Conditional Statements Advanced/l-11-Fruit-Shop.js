function calculateFruitPrice(fruit, day, quantity) {
    const weekdayPrices = {
        "banana": 2.50,
        "apple": 1.20,
        "orange": 0.85,
        "grapefruit": 1.45,
        "kiwi": 2.70,
        "pineapple": 5.50,
        "grapes": 3.85
    };

    
    const weekendPrices = {
        "banana": 2.70,
        "apple": 1.25,
        "orange": 0.90,
        "grapefruit": 1.60,
        "kiwi": 3.00,
        "pineapple": 5.60,
        "grapes": 4.20
    };

  
    if (!weekdayPrices[fruit] && !weekendPrices[fruit]) {
        console.log("error");
        return;
    }

    if (day === "Saturday" || day === "Sunday") {
        
        let price = weekendPrices[fruit] * quantity;
        console.log(price.toFixed(2));
    
    } else if (["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"].includes(day)) {

        let price = weekdayPrices[fruit] * quantity;
        console.log(price.toFixed(2));
    
    } else {
 
        console.log("error");
    }
}

calculateFruitPrice("apple", "Tuesday", 2);
calculateFruitPrice("orange", "Sunday", 3);
calculateFruitPrice("kiwi", "Monday", 2.5);
calculateFruitPrice("grapes", "Saturday", 0.5);
calculateFruitPrice("tomato", "Monday", 0.5);