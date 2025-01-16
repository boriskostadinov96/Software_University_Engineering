class Drink {
  name: string;
  price: number;
  volume: number;

  constructor(name: string, price: number, volume: number) {
    this.name = name;
    this.price = price;
    this.volume = volume;
  }

  toString(): string {
    return `Name: ${this.name}, Price: $${this.price}, Volume: ${this.volume} ml`;
  }
}

class VendingMachine {
  buttonCapacity: number;
  drinks: Drink[];

  constructor(buttonCapacity: number) {
    this.buttonCapacity = buttonCapacity;
    this.drinks = [];
  }

  addDrink(drink: Drink) {
    if (this.drinks.length < this.buttonCapacity) {
      this.drinks.push(drink);
    }
  }

  removeDrink(name: string) {
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

  getCheapest(): string | null {
    if (this.drinks.length === 0) {
      return null;
    }
    const cheapestDrink = this.drinks.reduce((min, drink) =>
      drink.price < min.price ? drink : min
    );
    return cheapestDrink.toString();
  }

  buyDrink(name: string): string | null {
    const index = this.drinks.findIndex((drink) => drink.name === name);
    if (index !== -1) {
      const purchasedDrink = this.drinks.splice(index, 1)[0];
      return purchasedDrink.toString();
    } else {
      return null;
    }
  }

  getCount(): number {
    return this.drinks.length;
  }

  report(): string {
    if (this.drinks.length === 0) {
      return "Drinks available:\nNone";
    }

    const reportString = this.drinks
      .map((drink) => drink.toString())
      .join("\n");
    return `Drinks available:\n${reportString}`;
  }
}
