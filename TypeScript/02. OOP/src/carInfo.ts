class Car {
  private _brand: string;
  private _model: string;
  private _horsePower: number;

  constructor(brand: string, model: string, horsePower: number) {
    this._brand = brand;
    this._model = model;
    this._horsePower = horsePower;
  }

  public get brand(): string {
    return this._brand;
  }

  public set brand(value: string) {
    if (!value.trim()) {
      throw new Error("Brand cannot be empty!");
    }
    this._brand = value;
  }

  public get model(): string {
    return this._model;
  }

  public set model(value: string) {
    if (!value.trim()) {
      throw new Error("Model cannot be empty");
    }
    this._model = value;
  }

  public get horsePower(): number {
    return this._horsePower;
  }

  public set horsepower(value: number) {
    if (value <= 0) {
      throw new Error("Horsepower must be greater than 0");
    }
    this._horsePower = value;
  }

  public toString(): string {
    return `The car is: ${this._brand} ${this._model} - ${this._horsePower} HP.`;
  }

  public static fromString(input: string): Car {
    const [brand, model, horsePower] = input.split(" ");
    return new Car(brand, model, parseInt(horsePower));
  }
}

const car1 = Car.fromString("Chevrolet Impala 390");
console.log(car1.toString());

const car2 = Car.fromString("Skoda Karoq 150");
console.log(car2.toString());
