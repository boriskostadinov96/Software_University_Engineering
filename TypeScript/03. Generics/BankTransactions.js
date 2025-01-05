"use strict";
class CreateAccount {}
class PersonalAccount extends CreateAccount {
  constructor(ownerName) {
    super();
    this.money = 0;
    this.recentTransactions = {};
    this.ownerName = ownerName;
  }
  deposit(amount) {
    this.money += amount;
  }
  expense(amount, expenseType) {
    if (this.money < amount) {
      throw new Error(`You can't make ${expenseType} transaction`);
    }
    this.money -= amount;
    if (this.recentTransactions[expenseType]) {
      this.recentTransactions[expenseType] += amount;
    } else {
      this.recentTransactions[expenseType] = amount;
    }
  }
  showDetails() {
    const totalMoneySpentOnExpenses = Object.values(
      this.recentTransactions
    ).reduce((total, amount) => total + amount, 0);
    return `Bank name: ${this.constructor.name}
Bank ID: <Bank ID Placeholder> 
Owner name: ${this.ownerName}
Money: ${this.money}
Money spent: ${totalMoneySpentOnExpenses}`;
  }
}
