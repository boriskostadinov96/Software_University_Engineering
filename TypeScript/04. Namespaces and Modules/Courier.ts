import { FoodAndBeverages } from "./Deliveries";

class Courier implements FoodAndBeverages.Delivery {
  protected placesToVisit: { customerName: string; visited: boolean }[];

  constructor(placesToVisit: { customerName: string; visited: boolean }[]) {
    this.placesToVisit = placesToVisit;
  }

  newCustomer(customerName: string, visited: boolean): void {
    this.placesToVisit.push({ customerName, visited });
  }

  visitCustomer(customerName: string): string {
    const customer = this.placesToVisit.find(
      (place) => place.customerName === customerName
    );
    if (customer) {
      customer.visited = true;
      return `${customerName} has been marked as visited.`;
    }
    return `${customerName} not found in places to visit.`;
  }

  showCustomers(): string {
    return this.placesToVisit
      .map(
        (place) =>
          `${place.customerName} (${place.visited ? "Visited" : "Not Visited"})`
      )
      .join(", ");
  }
}

export default Courier;
