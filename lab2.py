class Product:
    def __init__(self, name, price, quantity):
        self.__name = name  
        self.__price = price  
        self.__quantity = quantity  

    def get_info(self):
        return f"Product: {self.__name}, Price: {self.__price}, Quantity: {self.__quantity}"

    def update_quantity(self, new_quantity):
        self.__quantity = new_quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @staticmethod
    def discount(price, percentage):
        return price - (price * percentage / 100)


class SportsEquipment(Product):
    def __init__(self, name, price, quantity, sport_type):
        super().__init__(name, price, quantity)
        self.sport_type = sport_type  

    def get_info(self):
        return f"Equipment: {self.name}, Sport: {self.sport_type}, Price: {self.price}, Quantity: {self.quantity}"


class Warranty:
    def __init__(self, warranty_period):
        self.warranty_period = warranty_period

    def get_warranty_info(self):
        return f"Warranty: {self.warranty_period} years"


class ElectronicEquipment(Product, Warranty):
    def __init__(self, name, price, quantity, warranty_period):
        Product.__init__(self, name, price, quantity)
        Warranty.__init__(self, warranty_period)

    def get_info(self):
        return f"Electronic: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Warranty: {self.warranty_period} years"


def display():
    ball = SportsEquipment("Football", 30, 10, "Football")
    treadmill = ElectronicEquipment("Treadmill", 600, 5, 2)

    print(ball.get_info())  
    print(treadmill.get_info())

    ball.update_quantity(8)
    print(f"Updated quantity of {ball.name}: {ball.quantity}")

    discounted_price = Product.discount(treadmill.price, 10)
    print(f"Discounted price of {treadmill.name}: {discounted_price}")


display()
