from inventory_management import create_products, create_inventory, create_orders, create_wholesale_orders, create_discounts, create_sales_info, create_discounted_inventory, print_info

def main():
    products = create_products()
    inventory = create_inventory(products)
    orders = create_orders(products)
    wholesale_orders = create_wholesale_orders(products)
    discounts = create_discounts(products)
    sales_info = create_sales_info()
    discounted_inventory = create_discounted_inventory(products)

    print_info(products, inventory, orders, wholesale_orders, discounts, sales_info, discounted_inventory)

if __name__ == "__main__":
    main()
