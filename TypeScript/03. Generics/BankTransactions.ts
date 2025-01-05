abstract class CreateAccount<BankName, BankID> {}

class PersonalAccount extends CreateAccount<string, number> {
  readonly ownerName: string;
  public money: number = 0;
  public recentTransactions: Record<string, number> = {};

  constructor(ownerName: string) {
    super();
    this.ownerName = ownerName;
  }

  deposit(amount: number) {
    this.money += amount;
  }

  expense(amount: number, expenseType: string) {
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

  showDetails(): string {
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
