import pytest
from src.order import Order 
from src.pizza import Pizza  

@pytest.mark.order 
@pytest.mark.pizza  

def test_multiple_pizzas():
    """
    Integration test: Ensure multiple pizza objects within a given order result in an additively larger cost.
    """
    order = Order()

    # Pizza 1: thin, marinara, mozzarella, pepperoni. Cost: 9.0
    pizza1_crust = "thin"
    pizza1_sauce = ["marinara"]
    pizza1_cheese = "mozzarella"
    pizza1_toppings = ["pepperoni"]
    order.input_pizza(pizza1_crust, pizza1_sauce, pizza1_cheese, pizza1_toppings)
    assert order.cost == 9.0
    assert len(order.pizzas) == 1

    # Pizza 2: thick, pesto, mozzarella(free), mushrooms. Cost: 6 + 3 + 0 + 3 = 12.0
    pizza2_crust = "thick"
    pizza2_sauce = ["pesto"]
    pizza2_cheese = "mozzarella"
    pizza2_toppings = ["mushrooms"]
    order.input_pizza(pizza2_crust, pizza2_sauce, pizza2_cheese, pizza2_toppings)

    # Expected total cost: cost(pizza1) + cost(pizza2) = 21.0
    assert order.cost == 21.0
    assert len(order.pizzas) == 2
