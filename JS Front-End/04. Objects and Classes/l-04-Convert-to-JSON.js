function objToJson(name, lastName, hairColor) {
    let obj = {
        name,
        lastName,
        hairColor
    };

    let result = JSON.stringify(obj);

    console.log(result);
    

}

objToJson('George', 'Jones', 'Brown')