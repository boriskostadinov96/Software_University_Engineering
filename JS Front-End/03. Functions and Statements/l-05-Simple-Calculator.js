function calculator(first_num, second_num, operator){
    let result = 0;

    switch (operator) {
        case 'multiply':
            result = first_num * second_num
            return result;
        
        case 'divide':
            result = first_num / second_num
            return result;
        
        case 'add':
            result = first_num + second_num
            return result;
        
        case 'subtract':
            result = first_num - second_num
            return result;
    }
    
    }
    
console.log(calculator(40,
    8,
    'divide'
    ));
