import pytest
from src.order import Order 

@pytest.mark.order
def test_order__init__():
    """
    Test that Order.__init__ initializes correctly:
    - should include an empty list of pizza objects.
    - should have a zero cost until order is input.
    - should not have yet been paid.
    """
    order = Order()
    assert isinstance(order.pizzas, list)
    assert len(order.pizzas) == 0
    assert order.cost == 0.0 
    assert order.paid == False

@pytest.mark.order
def test_order__str__():
    """
    Testing Order.__str__: Returns a string containing customer full order and cost
    """
    order = Order()
    # Add a pizza to the order so __str__ has content to display.
    order.input_pizza("thin", ["marinara"], "mozzarella", ["pepperoni"]) 

    order_str = str(order)
    assert "Customer Requested:" in order_str
    assert "Crust: thin, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['pepperoni'], Cost: 9" in order_str # Updated cost
    assert "Total Order Cost: 9.00" in order_str # Updated total cost
    assert "Payment Status: Not Paid" in order_str

@pytest.mark.order
def test_order_input_pizza():
    """
    Test that input_pizza() method updates the order's total cost.
    """
    order = Order()
    # Add a pizza to the order
    order.input_pizza("thin", ["marinara"], "mozzarella", ["pepperoni"])
    assert order.cost == 9.0 

    # Add another pizza 
    order.input_pizza("thin", ["pesto"], "mozzarella", ["mushrooms"])
    assert order.cost == 9.0 + 11.0 # Updated total cost


@pytest.mark.order
def test_order_paid():
    """
    Test that order_paid() method updates 'paid' to True.
    """
    order = Order()
    assert order.paid is False # Starts as false
    order.order_paid()
    assert order.paid is True # Assert now true