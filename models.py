from datetime import datetime

class Product:
    def __init__(self, name, price, quantity, weight, description, category, brand, size, color, created_at, updated_at):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__weight = weight
        self.__description = description
        self.__category = category
        self.__brand = brand
        self.__size = size
        self.__color = color
        self.__created_at = created_at
        self.__updated_at = updated_at

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError()
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError()
        self.__quantity = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError()
        self.__weight = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        self.__updated_at = value

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    @staticmethod
    def discount(price, percentage):
        return price - (price * percentage / 100)

    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Weight: {self.weight}, Description: {self.description}, Category: {self.category}, Brand: {self.brand}, Size: {self.size}, Color: {self.color}, Created at: {self.created_at}, Updated at: {self.updated_at}"

class SportsClothing(Product):
    def __init__(self, name, price, quantity, weight, description, brand, size, color, created_at, updated_at, material):
        super().__init__(name, price, quantity, weight, description, "Sports Clothing", brand, size, color, created_at, updated_at)
        self.__material = material

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        self.__material = value

    def get_info(self):
        return super().get_info() + f", Material: {self.material}"


class Inventory:
    def __init__(self, product, quantity_in_stock, last_restocked):
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_restocked = last_restocked

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        self.__product = value

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, value):
        self.__quantity_in_stock = value

    @property
    def last_restocked(self):
        return self.__last_restocked

    @last_restocked.setter
    def last_restocked(self, value):
        self.__last_restocked = value

    def update_stock(self, new_stock):
        self.quantity_in_stock = new_stock

    def get_stock_info(self):
        return f"Product: {self.product}, Stock: {self.quantity_in_stock}, Last restocked: {self.last_restocked}"


class Discount:
    def __init__(self, product, discount_percentage, start_date, end_date):
        self.__product = product
        self.__discount_percentage = discount_percentage
        self.__start_date = start_date if start_date else datetime.now()
        self.__end_date = end_date if end_date else datetime.now()

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        self.__product = value

    @property
    def discount_percentage(self):
        return self.__discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, value):
        if value < 0 or value > 100:
            raise ValueError()
        self.__discount_percentage = value


    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value

    def get_discounted_price(self):
        return self.product.price * (1 - self.discount_percentage / 100)


    def get_info(self):
        return f"Product: {self.product.get_info()}, Discount: {self.discount_percentage}%, Start date: {self.start_date}, End date: {self.end_date}"


class Order:
    def __init__(self, customer, products, order_date, shipping_address, payment_method):
        self.__customer = customer
        self.__products = products
        self.__order_date = order_date
        self.__shipping_address = shipping_address
        self.__payment_method = payment_method

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = value

    @property
    def order_date(self):
        return self.__order_date

    @order_date.setter
    def order_date(self, value):
        self.__order_date = value

    @property
    def shipping_address(self):
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value

    def get_total_amount(self):
        total = sum([product.price for product in self.products])
        return total

    def get_info(self):
        products_info = ', '.join([product.get_info() for product in self.products])
        return f"Customer: {self.customer}, Products: {products_info}, Order Date: {self.order_date}, Shipping Address: {self.shipping_address}, Payment Method: {self.payment_method}, Total Amount: {self.get_total_amount()}"

class WholesaleOrder(Order):
    def __init__(self, customer, products, order_date, shipping_address, payment_method, discount):
        super().__init__(customer, products, order_date, shipping_address, payment_method)
        self.__discount = discount

    @property
    def discount(self):
        return self.__discount

    def get_total_amount(self):
        total = super().get_total_amount()
        return total - (total * self.discount / 100)

    def get_info(self):
        return super().get_info() + f", Wholesale Discount: {self.discount}%"

class SalesInfo:
    def __init__(self, sales_count, last_sale_date):
        self.__sales_count = sales_count
        self.__last_sale_date = last_sale_date

    @property
    def sales_count(self):
        return self.__sales_count

    @sales_count.setter
    def sales_count(self, value):
        self.__sales_count = value

    @property
    def last_sale_date(self):
        return self.__last_sale_date

    @last_sale_date.setter
    def last_sale_date(self, value):
        self.__last_sale_date = value

    def get_sales_info(self):
        return f"Sales Count: {self.sales_count}, Last Sale Date: {self.last_sale_date}"

class DiscountedInventory(Discount, Inventory, SalesInfo):
    def __init__(self, product, discount_percentage, start_date, end_date, quantity_in_stock, last_restocked, sales_count, last_sale_date):
        Discount.__init__(self, product, discount_percentage, start_date, end_date)
        Inventory.__init__(self, product, quantity_in_stock, last_restocked)
        SalesInfo.__init__(self, sales_count, last_sale_date)

    def get_full_info(self):
        return f"{self.get_info()} | Stock: {self.quantity_in_stock} | Sales: {self.sales_count}"
