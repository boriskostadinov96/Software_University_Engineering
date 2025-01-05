"use strict";
// interface Dealership<T> {
//   dealershipName: T;
//   soldCars: number;
// }
// interface Actions<T> {
//   sellCar(dealerID: T, model: T): void;
// }
// class CarDealership<T> implements Dealership<T>, Actions<T> {
//   dealershipName: T;
//   soldCars: number;
//   public modelsSold: Record<T, T[]>;
//   constructor(dealershipName: T) {
//     this.dealershipName = dealershipName;
//     this.soldCars = 0;
//     this.modelsSold = {};
//   }
//   sellCar(dealerID: T, model: T): void {
//     if (!this.modelsSold[dealerID]) {
//       this.modelsSold[dealerID] = [];
//     }
//     this.modelsSold[dealerID].push(model);
//     this.soldCars++;
//   }
//   showDetails(): string {
//     let details = `${this.dealershipName}:\n`;
//     for (const dealerID in this.modelsSold) {
//       const models = this.modelsSold[dealerID];
//       details += `${dealerID} sold ${models.join(", ")}\n`;
//     }
//     return details.trim();
//   }
// }
// let dealership = new CarDealership("SilverStar");
// dealership.sellCar("BG01", "C Class");
// dealership.sellCar("BG02", "S Class");
// dealership.sellCar("BG03", "ML Class");
// dealership.sellCar("BG04", "CLK Class");
// console.log(dealership.showDetails());
