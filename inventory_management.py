from models import Product, Inventory, Order, WholesaleOrder, Discount, SalesInfo, DiscountedInventory
from datetime import datetime

def create_products():
    products = [
        Product(
            name="T-shirt",
            price=25.99,
            quantity=100,
            weight=0.3,
            description="Nike T-shirt",
            category="Clothing",
            brand="Nike",
            size="M",
            color="Blue",
            created_at=datetime.now(),
            updated_at=datetime.now()
        ),
        Product(
            name="Sneakers",
            price=65.49,
            quantity=50,
            weight=1.0,
            description="Adidas Sneakers",
            category="Footwear",
            brand="Adidas",
            size="L",
            color="Black",
            created_at=datetime.now(),
            updated_at=datetime.now()
        ),
        Product(
            name="Sport Pants",
            price=35.99,
            quantity=75,
            weight=0.5,
            description="Puma Sport Pants",
            category="Clothing",
            brand="Puma",
            size="S",
            color="Red",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
    ]
    return products

def create_inventory(products):
    inventory = [
        Inventory(product=products[0], quantity_in_stock=50, last_restocked=datetime.now()),
        Inventory(product=products[1], quantity_in_stock=30, last_restocked=datetime.now()),
        Inventory(product=products[2], quantity_in_stock=20, last_restocked=datetime.now())
    ]
    return inventory

def create_orders(products):
    orders = [
        Order(
            customer="Customer 1",
            products=[products[0], products[1]],
            order_date=datetime.now(),
            shipping_address="Street 10, City 1",
            payment_method="Credit Card"
        ),
        Order(
            customer="Customer 2",
            products=[products[2]],
            order_date=datetime.now(),
            shipping_address="Street 20, City 2",
            payment_method="Cash"
        )
    ]
    return orders

def create_wholesale_orders(products):
    wholesale_orders = [
        WholesaleOrder(
            customer="Wholesale Company 1",
            products=[products[0], products[1], products[2]],
            order_date=datetime.now(),
            shipping_address="Wholesale Base, 1, City 1",
            payment_method="Bank Transfer",
            discount=10  
        ),
        WholesaleOrder(
            customer="Wholesale Company 2",
            products=[products[1]],
            order_date=datetime.now(),
            shipping_address="Wholesale Base, 2, City 2",
            payment_method="Bank Transfer",
            discount=15  
        )
    ]
    return wholesale_orders

def create_discounts(products):
    discounts = [
        Discount(
            product=products[0],
            discount_percentage=20,
            start_date=datetime.now(),
            end_date=datetime.now()
        ),
        Discount(
            product=products[1],
            discount_percentage=30,
            start_date=datetime.now(),
            end_date=datetime.now()
        )
    ]
    return discounts

def create_sales_info():
    sales_info = [
        SalesInfo(sales_count=200, last_sale_date=datetime.now()),
        SalesInfo(sales_count=150, last_sale_date=datetime.now())
    ]
    return sales_info

def create_discounted_inventory(products):
    discounted_inventory = [
        DiscountedInventory(
            product=products[0],
            discount_percentage=20,
            start_date=datetime.now(),
            end_date=datetime.now(),
            quantity_in_stock=40,
            last_restocked=datetime.now(),
            sales_count=100,
            last_sale_date=datetime.now()
        ),
        DiscountedInventory(
            product=products[1],
            discount_percentage=15,
            start_date=datetime.now(),
            end_date=datetime.now(),
            quantity_in_stock=30,
            last_restocked=datetime.now(),
            sales_count=80,
            last_sale_date=datetime.now()
        )
    ]
    return discounted_inventory

def print_info(products, inventory, orders, wholesale_orders, discounts, sales_info, discounted_inventory):
    print("Products Information:")
    print("\n".join(map(lambda product: product.get_info(), products)))

    print("\nInventory Information:")
    print("\n".join(map(lambda inv: inv.get_stock_info(), inventory)))

    print("\nOrders Information:")
    print("\n".join(map(lambda order: order.get_info(), orders)))

    print("\nWholesale Orders Information:")
    print("\n".join(map(lambda wholesale_order: wholesale_order.get_info(), wholesale_orders)))

    print("\nDiscounts Information:")
    print("\n".join(map(lambda discount: discount.get_info(), discounts)))

    print("\nSales Information:")
    print("\n".join(map(lambda sales: sales.get_sales_info(), sales_info)))

    print("\nDiscounted Inventory Information:")
    print("\n".join(map(lambda discounted: discounted.get_full_info(), discounted_inventory)))
