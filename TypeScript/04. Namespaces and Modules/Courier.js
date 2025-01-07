"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class Courier {
  constructor(placesToVisit) {
    this.placesToVisit = placesToVisit;
  }
  newCustomer(customerName, visited) {
    this.placesToVisit.push({ customerName, visited });
  }
  visitCustomer(customerName) {
    const customer = this.placesToVisit.find(
      (place) => place.customerName === customerName
    );
    if (customer) {
      customer.visited = true;
      return `${customerName} has been marked as visited.`;
    }
    return `${customerName} not found in places to visit.`;
  }
  showCustomers() {
    return this.placesToVisit
      .map(
        (place) =>
          `${place.customerName} (${place.visited ? "Visited" : "Not Visited"})`
      )
      .join(", ");
  }
}
exports.default = Courier;
