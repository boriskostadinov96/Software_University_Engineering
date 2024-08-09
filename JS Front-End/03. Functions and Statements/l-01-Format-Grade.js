function formatGrade(grade) {
    let result = '';

    if (grade < 3.00) {
        result = 'Fail';
        return `${result} (${Math.floor(grade)})`;
    
    } else if (grade >= 3.00 && grade < 3.50) {
        result = 'Poor';
    
    } else if (grade >= 3.50 && grade < 4.50) {
        result = 'Good';
    
    } else if (grade >= 4.50 && grade < 5.50) {
        result = 'Very good';
    
    } else {
        result = 'Excellent';
    }

    return `${result} (${grade.toFixed(2)})`;
}