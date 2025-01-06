"use strict";
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    getPersonDetails() {
        return `${this.name} is ${this.age} years old.`;
    }
}
const peterPerson = new Person("Peter", 12);
console.log(peterPerson.getPersonDetails());
const sofiaPerson = new Person("Sofia", 33);
console.log(sofiaPerson.getPersonDetails());
