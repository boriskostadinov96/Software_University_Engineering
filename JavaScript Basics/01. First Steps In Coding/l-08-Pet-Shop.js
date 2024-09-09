function zooShop(dogFood, catFood) {
    const dogFoodPrice = 2.5;
    const catFoodPrice = 4;
    
    const totalCost = (dogFood * dogFoodPrice) + (catFood * catFoodPrice);
    console.log(`${totalCost} lv.`);
}

zooShop(5, 4);