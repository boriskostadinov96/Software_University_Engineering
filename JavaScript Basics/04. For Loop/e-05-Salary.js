function calculateSalary(input) {
    const n = Number(input[0]);
    let salary = Number(input[1]);

    for (let i = 2; i < 2 + n; i++) {
        const site = input[i];

        if (site === "Facebook") {
            salary -= 150;
        } else if (site === "Instagram") {
            salary -= 100;
        } else if (site === "Reddit") {
            salary -= 50;
        }

        if (salary <= 0) {
            console.log("You have lost your salary.");
            return;
        }
    }

    console.log(Math.floor(salary));
}