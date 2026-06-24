class Product:
    def __init__(self, name, demand, willingness_to_pay):
        self.name = name
        self.demand = demand
        self.willingness_to_pay = willingness_to_pay

    def is_validated(self):
        return self.demand > 0 and self.willingness_to_pay > 0
