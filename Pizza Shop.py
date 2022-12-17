from math import pi, sqrt, ceil

PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True


def get_pizza_area(diameter):
    """ (float) -> float
    Uses the diameter of a pizza to return its area as a positive float.

    >>> round(get_pizza_area(1.5), 2)
    1.77
    >>> round(get_pizza_area(2.0), 5)
    3.14159
    >>> round(get_pizza_area(3.3), 3)
    8.553
"""
    area = pi * (diameter / 2) ** 2
    return area


def get_fair_quantity(diameter1, diameter2):
    """ (float, float) -> int
    Uses the diameter of two pizzas to return the minimum number of small pizzas to match the area of one large pizza as an integer.

    >>> get_fair_quantity(14.0, 8.0)
    4
    >>> get_fair_quantity(3.0, 14.0)
    22
    >>> get_fair_quantity(10.2, 6.3)
    3
"""
    area_1 = get_pizza_area(diameter1)
    area_2 = get_pizza_area(diameter2)
    if area_1 > area_2:
        multiple = ceil(area_1/area_2) 
    elif area_1 < area_2:
        multiple = ceil(area_2/area_1) 
    if FAIR == False:
        multiple * 1.5
    return multiple


def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    """ (float, float, float, float, int) -> float
    Uses the four values to return the the missing imput value that is the integer -1 as a positive float.

    >>> pizza_formula(12.0, 6.0, 10.0, -1, 2)
    5.0
    >>> pizza_formula(14.0, 8.0, 9.55, -1, 4)
    12.47
    >>> pizza_formula(12.0, 9.0, 6.45, 2, -1)
    0.55
"""
    n_large = 1
    area_large = get_pizza_area(d_large)
    area_small = get_pizza_area(d_small)
    small_pizza_per_dollar = (area_small * n_small) / c_small
    large_pizza_per_dollar = (area_large * n_large) / c_large
    if d_large == -1:
        find_d_large = (c_large * small_pizza_per_dollar) / n_large
        find = 2 * (sqrt(find_d_large / pi))
    elif d_small == -1:
        find_d_small = (c_small * large_pizza_per_dollar) / n_small
        find = 2 * (sqrt(find_d_small / pi))
    elif c_large == -1:
        find = (area_large * n_large) / small_pizza_per_dollar
    elif c_small == -1:
        find = (area_small * n_small) / large_pizza_per_dollar
    elif n_small == -1:
        find = (c_small * large_pizza_per_dollar) / area_small
    return float(round(find, 2))


def get_pizza_cake_cost(base_diameter, height_per_level):
    """ (int, float) -> float
    Uses the base diameter of a pizza and its height per level to return the cost of the pizza cake as a positive float.

    >>> get_pizza_cake_cost(2, 1.0)
    15.71
    >>> get_pizza_cake_cost(10, 2.0)
    2419.03
    >>> get_pizza_cake_cost(10, 2.2)
    2660.93
"""
    sum_of_areas = 0
    while base_diameter > 0:
        area_1 = pi * (base_diameter / 2) ** 2
        base_diameter = base_diameter - 1
        sum_of_areas += area_1
    pizza_cost = float(round(sum_of_areas * PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED * height_per_level, 2))
    if FAIR == False:
        pizza_count *= 1.5
    return pizza_cost


def get_pizza_poutine_cost(diameter, height):
    """ (int, float) -> float
    Uses the diameter of the poutine and its height to return its cost as a positive float.

    >>> get_pizza_poutine_cost(2, 1.0)
    9.42
    >>> get_pizza_poutine_cost(10, 2.0)
    471.24
    >>> get_pizza_poutine_cost(4, 3.2)
    120.64
"""
    poutine_volume = pi * (diameter / 2) ** 2 * height
    poutine_cost = float(round(PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED * poutine_volume, 2))
    if FAIR == False:
        pizza_count *= 1.5
    return poutine_cost


def display_welcome_menu():
    """ () -> None
    Displays a welcome message and menu with three options.

    >>> display_welcome_menu()
    Welcome To The Ocky Way Pizzeria. Don't Forget the Bev: Neva Neva Neva!
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
"""
    print(
        "Welcome To The Ocky Way Pizzeria. Don't Forget the Bev: Neva Neva Neva!\nPlease choose an option:\nA. Special Orders\nB. Formula Mode")
    print("C. Quantity Mode")


def special_orders():
    """ () -> None
    User chooses either a poutine or a cake and is asked to enter the diameter, height and if they went the special ingredient.
    It then prints the total cost.

    >>> special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? yes
    The cost is $35.7

    >>> special_orders()
    Would you like the cake or poutine? poutine
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? no
    The cost is $9.42

    >>> special_orders()
    Would you like the cake or poutine? poutine
    Enter diameter: 4
    Enter height: 1.5
    Do you want the guacamole? yes
    The cost is $161.36
"""
    cake_poutine = input("Would you like the cake or poutine?: ")
    diameter1 = int(input("Enter diameter: "))
    height1 = float(input("Enter height: "))
    Guac = input("Do you want the " + SPECIAL_INGREDIENT + "? ")
    cake_cost = get_pizza_cake_cost(diameter1, height1)
    cake_with_Guac = cake_cost + SPECIAL_INGREDIENT_COST
    poutine_cost = get_pizza_poutine_cost(diameter1, height1)
    poutine_with_Guac = poutine_cost + SPECIAL_INGREDIENT_COST

    if cake_poutine == "cake" and 'y' in Guac:
        cost = str(cake_with_Guac)
    elif cake_poutine == "cake":
        cost = str(cake_cost)
    elif (cake_poutine == "poutine") and 'y' in Guac:
        cost = str(poutine_with_Guac)
    elif cake_poutine == "poutine":
        cost = str(poutine_cost)
    print("The cost is $" + cost)

def quantity_mode():
    """ () -> None
    Uses enters the diameters of two pizzas.
    The program prints out the minimum number of small pizzas to get the same amount of one large pizza by area.

    >>> quantity_mode()
    Enter diameter 1: 14.0
    Enter diameter 2: 8.0
    You should buy 4 pizzas.

    >>> Enter diameter_1: 1.0
    Enter diameter_2: 2.0
    You should buy 6 pizzas.

    >>> Enter diameter_1: 3.0
    Enter diameter_2: 10.0
    You should buy 16 pizzas.
"""
    diameter_1 = float(input("Enter diameter 1: "))
    diameter_2 = float(input("Enter diameter 2: "))
    print("You should buy", get_fair_quantity(diameter_1, diameter_2), "pizzas.")


def formula_mode():
    """ () -> None
    The user enters the diameter of a large and small pizza into the program, the costs of it, and number of small pizzas.
    It prints the actual value of the unkown value given as -1.

    >>> formula_mode()
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price: 10.0
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0

    >>> formula_mode()
    Enter large diameter: -1.0
    Enter small diameter: 8.0
    Enter large price: 3.0
    Enter small price: 4
    Enter small number: 3
    The missing value is: 12.0

    >>> formula_mode()
    Enter large diameter: 13.0
    Enter small diameter: 10.0
    Enter large price: -1
    Enter small price: 12.0
    Enter small number: 5
    The missing value is: 4.06

"""
    large_diameter = float(input("Enter large diameter: "))
    small_diameter = float(input("Enter small diameter: "))
    large_price = float(input("Enter large price: "))
    small_price = float(input("Enter small price: "))
    small_number = float(input("Enter small number: "))
    missing_value_formula = pizza_formula(large_diameter, small_diameter, large_price, small_price, small_number)
    print("The missing value is:", missing_value_formula)


def run_pizza_calculator():
    """ () -> None
    Shows a welcome message and a list of options which the user has to choose from, and depending on the choice then calls the right
    function.

    >>> run_pizza_calculator()
    Welcome To The Ocky Way Pizzeria. Don't Forget the Bev: Neva Neva Neva!
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: A
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? yes
    The cost is $35.7

    >>> run_pizza_calculator()
    Welcome To The Ocky Way Pizzeria. Don't Forget the Bev: Neva Neva Neva!
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: F
    Invalid mode.

    >>> run_pizza_calculator()
    Welcome To The Ocky Way Pizzeria. Don't Forget the Bev: Neva Neva Neva!
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: C
    Enter diameter 1: 2
    Enter diameter 2: 3
    You should buy 3 pizzas.
"""
    display_welcome_menu()
    choice = input("Your Choice: ")
    if choice == "A":
        special_orders()
    elif choice == "B":
        formula_mode()
    elif choice == "C":
        quantity_mode()
    else:
        print("Invalid mode.")