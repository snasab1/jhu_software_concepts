class Pizza:
    """
    Class pizza with crust, sauce, and topping (cheese is free!). Calculates cost.
    """

    # Define the pricing 
    crust_prices = {
        'thin': 5,
        'thick': 6,
        'gluten_free': 8
    }
    sauce_prices = {
        'marinara': 2,
        'pesto': 3,
        'liv_sauce': 5
    }
    topping_prices = {
        'pineapple': 1,
        'pepperoni': 2,
        'mushrooms': 3
    }
    cheese_prices = {
        'mozzarella': 0  # Cheese is free
    }

    def __init__(self, crust, sauce, cheese, toppings):
        """
        Initializes pizza, set pizza variables, and calculate cost to create.
        """
        # Validation - make sure inputs are valid
        if not isinstance(crust, str) or crust.lower() not in self.crust_prices:
            raise ValueError(f"A pizza must include a valid crust: thin, thick, gluten_free.")
        if not isinstance(sauce, list) or not sauce:
            raise ValueError("A pizza must include valid sauces: marinara, pesto, liv_sauce.")
        if not isinstance(cheese, str) or cheese.lower() not in self.cheese_prices:
            raise ValueError(f"A pizza must include mozzarella cheese.")
        if not isinstance(toppings, list) or not toppings:
            raise ValueError("A pizza must include at least one topping from the available options: mushrooms, pineapple, pepperoni.")

        # Set pizza variables
        # Make the string inputs lowercase to ensure consistency
        self.crust = crust.lower() 
        self.sauce = [s.lower() for s in sauce] 
        self.cheese = cheese.lower() 
        self.toppings = [t.lower() for t in toppings]
       
       
    def cost(self):
        """
        Determine the cost of a pizza
        """
        total_cost = 0

        # Add crust cost
        total_cost += self.crust_prices[self.crust]

        # Add sauce cost(s)
        for s in self.sauce:
            total_cost += self.sauce_prices[s]

        # Add topping cost(s)
        for t in self.toppings:
            total_cost += self.topping_prices[t]

        return total_cost

    def __str__(self):
        """
        Print type of pizza and cost of that pizza
        """
        sauces_str = ', '.join(f"'{s}'" for s in self.sauce)
        toppings_str = ', '.join(f"'{t}'" for t in self.toppings)
        return (f"Crust: {self.crust}, Sauce: [{sauces_str}], Cheese: {self.cheese}, "
                f"Toppings: [{toppings_str}], Cost: {self.cost()}")