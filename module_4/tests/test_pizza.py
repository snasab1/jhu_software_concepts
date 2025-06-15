import pytest
from src.pizza import Pizza # Import Pizza class for testing

@pytest.mark.pizza
def test__init__():
    """
    Test that Pizza.__init__ successfully initializes a Pizza object.
    It should return an initialized pizza and check its attributes and non-zero cost.
    """

    # Create a pizza object with valid parameters (correct types and values)
    crust = "thin"
    sauce = ["marinara"]
    cheese = "mozzarella"
    toppings = ["pepperoni"]

    pizza = Pizza(crust, sauce, cheese, toppings)

    # Assert it returns an initialized Pizza object
    assert isinstance(pizza, Pizza)

    # Assert pizza should have crust (str), sauce (list of str), cheese (str), toppings (list of str)
    assert pizza.crust == crust
    assert isinstance(pizza.crust, str)
    assert pizza.sauce == sauce
    assert isinstance(pizza.sauce, list)
    assert pizza.cheese == cheese
    assert isinstance(pizza.cheese, str)
    assert pizza.toppings == toppings
    assert isinstance(pizza.toppings, list)

    # Assert pizza should return a non-zero cost
    assert pizza.cost() > 0


@pytest.mark.pizza
def test__str__():
    """
    Test that Pizza.__str__ returns a string containing the pizza details and its cost.
    """
    crust = "thin"
    sauce = ["marinara"]
    cheese = "mozzarella"
    toppings = ["pepperoni"]
    
    # Calculate expected cost based on pizza_ordering_code prices:
    expected_cost = 9.0

    pizza = Pizza(crust, sauce, cheese, toppings)
    expected_str = (f"Crust: {crust}, Sauce: ['{sauce[0]}'], Cheese: {cheese}, "
                    f"Toppings: ['{toppings[0]}'], Cost: {int(expected_cost)}")

    assert str(pizza) == expected_str

@pytest.mark.pizza
@pytest.mark.parametrize(
    "crust, sauce, cheese, toppings, expected_cost",
    [
        ("thin", ["marinara"], "mozzarella", ["pepperoni"], 9.0), # 5 (thin) + 2 (marinara) + 0 (mozzarella) + 2 (pepperoni) = 9
        ("thin", ["pesto"], "mozzarella", ["mushrooms"], 11.0),    # 5 (thin) + 3 (pesto) + 0 (mozzarella) + 3 (mushrooms) = 11
        ("thick", ["marinara"], "mozzarella", ["mushrooms"], 11.0), # 6 (thick) + 2 (marinara) + 0 (mozzarella) + 3 (mushrooms) = 11
        ("gluten_free", ["marinara"], "mozzarella", ["pineapple"], 11.0), # 8 (gluten_free) + 2 (marinara) + 0 (mozzarella) + 1 (pineapple) = 11
        ("thin", ["liv_sauce", "pesto"], "mozzarella", ["mushrooms", "pepperoni"], 18.0) # 5 (thin) + 5 (liv_sauce) + 3 (pesto) + 0 (mozzarella) + 3 (mushrooms) + 2 (pepperoni) = 18
    ]
)
def test_cost(crust, sauce, cheese, toppings, expected_cost):
    """
    Test that the cost() method returns the correct calculated cost for a given input pizza.
    Uses parameterized testing to cover various combinations listed above. 
    """
    pizza = Pizza(crust, sauce, cheese, toppings)
    assert pizza.cost() == expected_cost