function trainTheTrainers(input) {
    let index = 0;
    const juryCount = Number(input[index]);
    index++;

    let totalSum = 0;
    let totalGrades = 0;

    while (input[index] !== "Finish") {
        let presentationName = input[index];
        index++;

        let sumGrades = 0;

        for (let i = 0; i < juryCount; i++) {
            let grade = Number(input[index]);
            index++;
            sumGrades += grade;
        }

        let averageGrade = sumGrades / juryCount;
        totalSum += sumGrades;
        totalGrades += juryCount;

        console.log(`${presentationName} - ${averageGrade.toFixed(2)}.`);
    }

    let finalAssessment = totalSum / totalGrades;
    console.log(`Student's final assessment is ${finalAssessment.toFixed(2)}.`);
}


trainTheTrainers([
    "2",
    "While-Loop",
    "6.00",
    "5.50",
    "For-Loop",
    "5.84",
    "5.66",
    "Finish"
]);

trainTheTrainers([
    "3",
    "Arrays",
    "4.53",
    "5.23",
    "5.00",
    "Lists",
    "5.83",
    "6.00",
    "5.42",
    "Finish"
]);

trainTheTrainers([
    "2",
    "Objects and Classes",
    "5.77",
    "4.23",
    "Dictionaries",
    "4.62",
    "5.02",
    "RegEx",
    "2.88",
    "3.42",
    "Finish"
]);
