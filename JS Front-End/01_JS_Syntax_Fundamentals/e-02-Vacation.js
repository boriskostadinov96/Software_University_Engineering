function vacation(group, type, day){
    let singlePrice = 0;
    
    if (day === 'Friday') {
        switch (type) {
            case 'Students':
                singlePrice = 8.45;
                break;
            case 'Business':
                singlePrice = 10.90;
                break;
            case 'Regular':
                singlePrice = 15;
                break;
        }
    } else if (day === 'Saturday') {
        switch (type) {
            case 'Students':
                singlePrice = 9.80;
                break;
            case 'Business':
                singlePrice = 15.60;
                break;
            case 'Regular':
                singlePrice = 20;
                break;
        }
    } else if (day === 'Sunday') {
        switch (type) {
            case 'Students':
                singlePrice = 10.46;
                break;
            case 'Business':
                singlePrice = 16;
                break;
            case 'Regular':
                singlePrice = 22.50;
                break;
        }
    }
    
    let totalPrice = singlePrice * group;
    
    if (type === 'Students' && group >= 30){
        totalPrice *= 0.85;
    } else if (type === 'Business' && group >= 100){
        totalPrice -= singlePrice * 10;
    } else if (type === 'Regular' && group >= 10 && group <= 20){
        totalPrice *= 0.95;
    }
    
    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

vacation(30, "Students", "Sunday");
