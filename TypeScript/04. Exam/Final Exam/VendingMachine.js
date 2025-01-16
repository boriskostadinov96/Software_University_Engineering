"use strict";
class Drink {
  constructor(name, price, volume) {
    this.name = name;
    this.price = price;
    this.volume = volume;
  }
  toString() {
    return `Name: ${this.name}, Price: $${this.price}, Volume: ${this.volume} ml`;
  }
}
class VendingMachine {
  constructor(buttonCapacity) {
    this.buttonCapacity = buttonCapacity;
    this.drinks = [];
  }
  addDrink(drink) {
    if (this.drinks.length < this.buttonCapacity) {
      this.drinks.push(drink);
    }
  }
  removeDrink(name) {
    const index = this.drinks.findIndex((drink) => drink.name === name);
    if (index !== -1) {
      this.drinks.splice(index, 1);
      return true;
    } else {
      return false;
    }
  }
  getLongest() {
    if (this.drinks.length === 0) {
      return null;
    }
    const longestDrink = this.drinks.reduce((max, drink) =>
      drink.volume > max.volume ? drink : max
    );
    return longestDrink.toString();
  }
  getCheapest() {
    if (this.drinks.length === 0) {
      return null;
    }
    const cheapestDrink = this.drinks.reduce((min, drink) =>
      drink.price < min.price ? drink : min
    );
    return cheapestDrink.toString();
  }
  buyDrink(name) {
    const index = this.drinks.findIndex((drink) => drink.name === name);
    if (index !== -1) {
      const purchasedDrink = this.drinks.splice(index, 1)[0];
      return purchasedDrink.toString();
    } else {
      return null;
    }
  }
  getCount() {
    return this.drinks.length;
  }
  report() {
    if (this.drinks.length === 0) {
      return "Drinks available:\nNone";
    }
    const reportString = this.drinks
      .map((drink) => drink.toString())
      .join("\n");
    return `Drinks available:\n${reportString}`;
  }
}
