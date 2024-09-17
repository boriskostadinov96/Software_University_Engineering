function moneyNeeded(pensCount, markersCount, liquid, discount) {
    let pensPrice = pensCount * 5.8;
    let markersPrice = markersCount * 7.2;
    let liquidPrice = liquid * 1.2;

    let totalPrice = pensPrice + markersPrice + liquidPrice;
    let discountPrice = totalPrice - (totalPrice * discount);

    console.log(discountPrice);
    

}

moneyNeeded(2,
    3,
    4,
    25 
    )