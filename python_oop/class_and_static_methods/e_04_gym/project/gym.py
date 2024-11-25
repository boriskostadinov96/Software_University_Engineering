from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription_obj = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer_obj = next(filter(lambda c: c.id == subscription_obj.customer_id, self.customers))
        trainer_obj = next(filter(lambda t: t.id == subscription_obj.trainer_id, self.trainers))
        plan_obj = next(filter(lambda p: p.id == subscription_obj.exercise_id, self.plans))

        equipment_obj = next(filter(lambda e: e.id == plan_obj.equipment_id, self.equipment))

        return f"{str(subscription_obj)}\n{str(customer_obj)}\n{str(trainer_obj)}\n{str(equipment_obj)}\n{str(plan_obj)}"
