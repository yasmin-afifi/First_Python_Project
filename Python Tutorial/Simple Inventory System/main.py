class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Display the product's information."""
        print(f"Product Name: {self.name}\nPrice: ${
              self.price:.2f}\nQuantity: {self.quantity}\n")

    def update_quantity(self, amount):
        """Update the quantity of the product."""
        self.quantity += amount
        if self.quantity < 0:
            print("Warning: Quantity cannot be negative. Resetting to 0.")
            self.quantity = 0

    def calculate_total_value(self):
        """Calculate and return the total value of the product."""
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        """Add a new product to the inventory."""
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Product '{name}' added to the inventory.\n")

    def display_all_products(self):
        """Display information for all products in the inventory."""
        if not self.products:
            print("No products in the inventory.\n")
            return
        for product in self.products:
            product.display_info()

    def calculate_inventory_value(self):
        """Calculate and display the total value of the inventory."""
        total_value = sum(product.calculate_total_value()
                          for product in self.products)
        print(f"Total Inventory Value: ${total_value:.2f}\n")

# Simulating user interactions


def main():
    print("Welcome to the Inventory Management System!\n")
    inventory = Inventory()

    while True:
        print("Options:\n1. Add a new product\n2. Display all products\n3. Update product quantity\n4. Display total inventory value\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            inventory.add_product(name, price, quantity)
        elif choice == "2":
            inventory.display_all_products()
        elif choice == "3":
            name = input("Enter the name of the product to update: ")
            for product in inventory.products:
                if product.name.lower() == name.lower():
                    amount = int(
                        input("Enter the quantity change (positive for restock, negative for sold): "))
                    product.update_quantity(amount)
                    print(f"Quantity for '{product.name}' updated.\n")
                    break
            else:
                print(f"Product '{name}' not found in the inventory.\n")
        elif choice == "4":
            inventory.calculate_inventory_value()
        elif choice == "5":
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()