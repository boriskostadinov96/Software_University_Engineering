function findBook(input) {
    let favoriteBook = input[0];
    let index = 1;
    let booksChecked = 0;

    while (input[index] !== "No More Books") {
        if (input[index] === favoriteBook) {
            console.log(`You checked ${booksChecked} books and found it.`);
            return;
        }

        booksChecked++;
        index++;
    }

    console.log("The book you search is not here!");
    console.log(`You checked ${booksChecked} books.`);
}