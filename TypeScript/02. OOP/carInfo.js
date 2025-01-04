"use strict";
class Car {
    constructor(brand, model, horsePower) {
        this._brand = brand;
        this._model = model;
        this._horsePower = horsePower;
    }
    get brand() {
        return this._brand;
    }
    set brand(value) {
        if (!value.trim()) {
            throw new Error("Brand cannot be empty!");
        }
        this._brand = value;
    }
    get model() {
        return this._model;
    }
    set model(value) {
        if (!value.trim()) {
            throw new Error("Model cannot be empty");
        }
        this._model = value;
    }
    get horsePower() {
        return this._horsePower;
    }
    set horsepower(value) {
        if (value <= 0) {
            throw new Error("Horsepower must be greater than 0");
        }
        this._horsePower = value;
    }
    toString() {
        return `The car is: ${this._brand} ${this._model} - ${this._horsePower} HP.`;
    }
    static fromString(input) {
        const [brand, model, horsePower] = input.split(" ");
        return new Car(brand, model, parseInt(horsePower));
    }
}
const car1 = Car.fromString("Chevrolet Impala 390");
console.log(car1.toString());
const car2 = Car.fromString("Skoda Karoq 150");
console.log(car2.toString());
