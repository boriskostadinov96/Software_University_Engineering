function generateRooms(floors, roomsPerFloor) {
    for (let floor = floors - 1; floor >= 0; floor--) {
        let rooms = [];
        
        if (floor % 2 === 0) {
            if (floor === floors - 1) {
                for (let room = 0; room < roomsPerFloor; room++) {
                    rooms.push(`L${floor}${room}`);
                }
            } else {
                for (let room = 0; room < roomsPerFloor; room++) {
                    rooms.push(`A${floor}${room}`);
                }
            }
        } else {
            for (let room = 0; room < roomsPerFloor; room++) {
                rooms.push(`O${floor}${room}`);
            }
        }
        console.log(rooms.join(' '));
    }
}
