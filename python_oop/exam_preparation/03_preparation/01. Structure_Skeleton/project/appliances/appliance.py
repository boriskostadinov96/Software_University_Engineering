class Appliance:
    def __init__(self, cost: float):
        self.cost = cost  # for a single day

    def get_monthly_expense(self):
        return self.cost * 30
