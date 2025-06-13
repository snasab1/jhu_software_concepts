from src.pizza import Pizza 

class Order:
    """
    Defines customer's order with one or more pizza objects
    and tracks the total cost and payment status.
    """
    def __init__(self):
        """
        Initializes a customer order and order cost.
        """
        self.pizzas = []  # List to store Pizza objects
        self.cost = 0.0   # Initialize order total cost
        self.paid = False # Initialize order paid status

    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Inputs the customer's order for a given pizza, initializes the pizza
        object, attaches to the order, then updates the total cost.

        Args:
            crust (str): The type of crust.
            sauce (list[str]): List of sauce types.
            cheese (str): The type of cheese.
            toppings (list[str]): List of topping types.
        """
        new_pizza = Pizza(crust, sauce, cheese, toppings)
        self.pizzas.append(new_pizza)
        self.cost += new_pizza.cost() # Update order cost with the new pizza's cost

    def order_paid(self):
        """
        Sets the order as paid once payment has been collected.
        """
        self.paid = True

    def __str__(self):
        """
        Print a customers complete order
        """
        # Collect all parts of the order into a list, then join.
        order_lines = ["Customer Requested:"]
        if not self.pizzas:
            order_lines.append("No pizzas in this order yet.")
        else:
            for pizza in self.pizzas:
                order_lines.append(str(pizza)) # Convert Pizza object to string

        order_lines.append(f"Total Order Cost: {self.cost:.2f}")
        order_lines.append(f"Payment Status: {'Paid' if self.paid else 'Not Paid'}")

        return "\n".join(order_lines)

