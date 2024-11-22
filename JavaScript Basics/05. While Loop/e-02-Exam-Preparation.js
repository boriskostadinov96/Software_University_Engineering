function solveExam(input) {
    let maxPoorGrades = Number(input[0]);
    let index = 1;

    let poorGrades = 0;
    let totalGrades = 0;
    let problemCount = 0;
    let gradeSum = 0;
    let lastProblem = "";

    while (poorGrades < maxPoorGrades) {
        let problemName = input[index];
        index++;

        if (problemName === "Enough") {
            let averageScore = gradeSum / problemCount;
            console.log(`Average score: ${averageScore.toFixed(2)}`);
            console.log(`Number of problems: ${problemCount}`);
            console.log(`Last problem: ${lastProblem}`);
            return;
        }

        let grade = Number(input[index]);
        index++;

        gradeSum += grade;
        problemCount++;
        lastProblem = problemName;

        if (grade <= 4) {
            poorGrades++;
            if (poorGrades >= maxPoorGrades) {
                console.log(`You need a break, ${poorGrades} poor grades.`);
                return;
            }
        }
    }
}