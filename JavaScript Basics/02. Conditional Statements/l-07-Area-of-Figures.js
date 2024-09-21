function solve(arg1, arg2, arg3) {
    let type = arg1;
    
    if (type === "square") {
        let a = Number(arg2);
        let result = a * a;
        console.log(result.toFixed(3));

    } else if (type === "rectangle") {
        let length = Number(arg2);
        let width = Number(arg3);
        let result = length * width;
        console.log(result.toFixed(3));

    } else if (type === "circle") {
        let radius = Number(arg2);
        let result = Math.PI * radius * radius;
        console.log(result.toFixed(3));

    } else if (type === "triangle") {
        let base = Number(arg2);
        let height = Number(arg3);
        let result = (base * height) / 2;
        console.log(result.toFixed(3));
    }
}

solve()
