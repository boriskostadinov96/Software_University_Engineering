function fruitPrice(fruit, grams, price){
    let weightKg = grams / 1000;
    let money = weightKg * price
    
    console.log(`I need $${money.toFixed(2)} to buy ${weightKg.toFixed(2)} kilograms ${fruit}.`);
    
}

fruitPrice('orange', 2500, 1.80)
