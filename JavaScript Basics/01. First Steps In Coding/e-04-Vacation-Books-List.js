function neededHours(pagesCount, oneHourPages, days) {
    let totalTime = pagesCount / oneHourPages;
    let result = totalTime / days;

    console.log(result);
}

neededHours(212,
    20,
    2 
    )