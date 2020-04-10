"""
A coffee_bot for fun, in future maybe add order_latte type
function to all coffee types
"""
# Define your functions


def order_mocha():
    while True:
        res = input("""Would you like to try our limited-edition peppermint mocha?
[a] Sure! \n[b] Maybe next time! \n>""")
        if res == 'a':
            return 'peppermint mocha'
        elif res == 'b':
            return 'mocha'
            print_message()


def print_message():
    print("""I'm sorry, I did not understand your selection.
Please enter the corresponding letter for your response.""")


def order_latte():
    res = input("""And what kind of milk for your latte
[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>""")
    if res == "a":
        milk = "latte"
    elif res == "b":
        milk = "non-fat latte"
    elif res == "c":
        milk = "soy latte"
    else:
        print_message()
        return order_latte()
    return milk


def get_drink_type():
    res = input("""What type of drink would you like? \n[a] Brewed Coffee
[b] Mocha \n[c] Latte \n>""")
    if res == "a":
        drink = "Brewed Coffee"
    elif res == "b":
        drink = order_mocha()
    elif res == "c":
        drink = order_latte()
    else:
        print_message()
        return get_drink_type()
    return drink


def get_size():
    res = input("""What size drink can I get for you? \n[a] Small \n[b] Medium
[c] Large \n> """)
    if res == "a":
        size = "small"
    elif res == "b":
        size = "medium"
    elif res == "c":
        size = "large"
    else:
        print_message()
        return get_size()
    return size


def coffee_bot():
    print("Welcome to the cafe!")

    order_drink = 'y'

    drinks = []
    while order_drink == 'y':
        size = get_size()
        drink_type = get_drink_type()

        drink = f"{size} {drink_type}"
        drinks.append(drink)
        while True:
            order_drink = input("Would you like another drink? (y/n) \n>")

            if order_drink == 'n':
                break
            elif order_drink == 'y':
                break

    print('Okay so I have')
    for i in range(len(drinks)):
        print(drinks[i])
    name = input("Can I get your name please? \n> ")
    print(f"Thanks, {name}! Your drink will be ready shortly")


# Call coffee_bot()!
coffee_bot()
