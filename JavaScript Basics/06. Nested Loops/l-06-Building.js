function printRoomNumbers(floors, roomsPerFloor) {
    for (let floor = floors; floor > 0; floor--) {
        let floorRooms = "";

        for (let room = 0; room < roomsPerFloor; room++) {
            if (floor === floors) {
                floorRooms += `L${floor}${room} `;
            
            } else if (floor % 2 === 0) {
                floorRooms += `O${floor}${room} `;
            
            } else {
                floorRooms += `A${floor}${room} `;
            }
        }

        console.log(floorRooms.trim());
    }
}

printRoomNumbers(6, 4);
printRoomNumbers(9, 5);
printRoomNumbers(4, 4);