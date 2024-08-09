function calculateTotalPrice(product_name, quantity) {
    let price = 0;

    if (product_name === "coffee") {
        price = 1.50;
    
    } else if (product_name === "water") {
        price = 1.00;
    
    } else if (product_name === "coke") {
        price = 1.40;
    
    } else if (product_name === "snacks") {
        price = 2.00;
    }

    let total = price * quantity;
    
    console.log(total.toFixed(2));
}