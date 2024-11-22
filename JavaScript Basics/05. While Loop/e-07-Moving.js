function calculateFreeSpace(inputData) {
    const width = parseInt(inputData[0]);
    const length = parseInt(inputData[1]);
    const height = parseInt(inputData[2]);
    
    const totalSpace = width * length * height;
    let usedSpace = 0;
    
    for (let i = 3; i < inputData.length; i++) {
        const command = inputData[i];
        
        if (command === "Done") {
            break;
        } else {
            usedSpace += parseInt(command);
        }
        
        if (usedSpace > totalSpace) {
            console.log(`No more free space! You need ${usedSpace - totalSpace} Cubic meters more.`);
            return;
        }
    }
    
    if (usedSpace < totalSpace) {
        console.log(`${totalSpace - usedSpace} Cubic meters left.`);
    }
}
