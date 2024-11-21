function login(input) {
    let username = input[0];
    let password = input[1];

    let data = input[2];
    let counter = 3;

    while (data !== password) {
        data = input[counter];
        counter++;
    }

    console.log(`Welcome ${username}!`);
}