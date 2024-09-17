function solve(chicken, fish, vegi) {
    let totalPrice = chicken * 10.35 + fish * 12.4 + vegi * 8.15;
    let desert = 0.2 * totalPrice

    let result = totalPrice + 2.5 + desert
    console.log(result);
}

solve(2,
    4,
    3
    )