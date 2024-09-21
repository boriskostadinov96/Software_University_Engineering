function checkPass(password) {
    correctPass = "s3cr3t!P@ssw0rd"

    if(password === correctPass) {
        console.log("Welcome");
        
    } else {
        console.log("Wrong password!");
        
    }
}

checkPass("s3cr3t!P@ssw0rd")