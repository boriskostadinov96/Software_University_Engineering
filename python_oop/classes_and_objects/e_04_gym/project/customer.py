class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.personal_id = Customer.id
        Customer.id += 1

    @staticmethod
    def get_next_id():
        return Customer.id

    def __repr__(self):
        return f"Customer <{self.personal_id}> {self.name}; Address: {self.address}; Email: {self.email}"