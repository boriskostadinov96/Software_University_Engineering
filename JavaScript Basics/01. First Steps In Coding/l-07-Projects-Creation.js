function projects(name, count) {
    const neededHours = 3 * count;
    console.log(`The architect ${name} will need ${neededHours} hours to complete ${count} project/s.`);
}

projects("George", 4);