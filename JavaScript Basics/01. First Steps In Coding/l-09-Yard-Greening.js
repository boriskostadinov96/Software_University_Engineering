function yardGreening(meters) {
    const pricePerSquareMeter = 7.61;
    const discountRate = 0.18;
    
    const initialPrice = meters * pricePerSquareMeter;
    const discount = initialPrice * discountRate;
    const finalPrice = initialPrice - discount;

    console.log(`The final price is: ${finalPrice.toFixed(2)} lv.`);
    console.log(`The discount is: ${discount.toFixed(2)} lv.`);
}

yardGreening(550);
