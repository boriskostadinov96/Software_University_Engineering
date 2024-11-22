function cakePieces(input) {
    let width = Number(input[0]);
    let length = Number(input[1]);
    let totalPieces = width * length;
    let index = 2;
    let command = input[index];
    let piecesTaken = 0;

    while (command !== "STOP") {
        let pieces = Number(command);
        totalPieces -= pieces;
        
        if (totalPieces < 0) {
            console.log(`No more cake left! You need ${Math.abs(totalPieces)} pieces more.`);
            return;
        }
        index++;
        command = input[index];
    }

    console.log(`${totalPieces} pieces are left.`);
}