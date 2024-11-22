function calculateStudentPerformance(input) {
    let name = input[0];
    let index = 1;
    let grade = 1;
    let sumGrades = 0;
    let failCount = 0;

    while (grade <= 12) {
        let annualGrade = parseFloat(input[index]);
        index++;

        if (annualGrade < 4.0) {
            failCount++;
            if (failCount > 1) {
                console.log(`${name} has been excluded at ${grade} grade`);
                return;
            }
        } else {
            sumGrades += annualGrade;
            grade++;
        }
    }

    let averageGrade = sumGrades / 12;
    console.log(`${name} graduated. Average grade: ${averageGrade.toFixed(2)}`);
}