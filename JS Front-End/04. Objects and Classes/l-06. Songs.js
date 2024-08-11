class Song {
    constructor(typeList, name, time) {
        this.typeList = typeList;
        this.name = name;
        this.time = time;
    }
}

let input = process.argv.slice(2);

let numberOfSongs = parseInt(input.shift());
let typeSong = input.pop();

let songs = [];

for (let i = 0; i < numberOfSongs; i++) {
    let [typeList, name, time] = input[i].split('_');
    let song = new Song(typeList, name, time);
    songs.push(song);
}

if (typeSong === 'all') {
    songs.forEach((i) => console.log(i.name));
} else {
    let filtered = songs.filter((i) => i.typeList === typeSong);
    filtered.forEach((i) => console.log(i.name));
}
