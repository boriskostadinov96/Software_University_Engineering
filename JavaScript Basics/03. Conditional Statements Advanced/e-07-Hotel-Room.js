function calculateHotelCost(month, nights) {
    let studioPricePerNight;
    let apartmentPricePerNight;

    if (month === "May" || month === "October") {
        studioPricePerNight = 50;
        apartmentPricePerNight = 65;
    } else if (month === "June" || month === "September") {
        studioPricePerNight = 75.20;
        apartmentPricePerNight = 68.70;
    } else if (month === "July" || month === "August") {
        studioPricePerNight = 76;
        apartmentPricePerNight = 77;
    }

    let studioCost = studioPricePerNight * nights;
    let apartmentCost = apartmentPricePerNight * nights;

    if ((month === "May" || month === "October") && nights > 14) {
        studioCost *= 0.7;
    } else if ((month === "May" || month === "October") && nights > 7) {
        studioCost *= 0.95;
    } else if ((month === "June" || month === "September") && nights > 14) {
        studioCost *= 0.8;
    }


    if (nights > 14) {
        apartmentCost *= 0.9;
    }

    studioCost = studioCost.toFixed(2);
    apartmentCost = apartmentCost.toFixed(2);

    console.log(`Apartment: ${apartmentCost} lv.`);
    console.log(`Studio: ${studioCost} lv.`);
}


calculateHotelCost("May", 15);
calculateHotelCost("June", 14);
calculateHotelCost("August", 20);
