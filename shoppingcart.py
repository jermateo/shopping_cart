def shopping():
    print("=" * 20)
    print("Welcome to Jer-Mart!")
    print("=" * 20)
    groceries = {
        'apples': 1.49,
        'bananas': 3.79,
        'lettuce': 4.49,
        'asparagus': 3.99,
        'chicken': 10.49,
        'ribeye': 10.99,
        'eggs': 4.09,
        'milk': 2.39,
        'rigatoni': 5.59
             }
    user_action = input("Enter JerMart [e], or Quit [q] ")
    shopping_cart = {}
    while user_action != 'q':
        print("=" * 20)
        print("Please choose from the list of grocery items:")
        for item, price in groceries.items():
            print(f"{item} -- ${price}")
        print("=" * 20)
        user_action = input("What would you like to do?\nAdd items [a], Delete items [d], Show cart [s], Pay [p] ")
        if user_action.lower() == 'a':
            print("=" * 20)
            add_item = input("Enter the item you wish to get: ")
            if add_item in groceries:
                item = groceries[add_item]
                how_many = int(input("Enter the quantity of your item: "))
                item_quantity = item * how_many
                shopping_cart[add_item] = item_quantity
            else:
                print('We currently do not carry that item.')
        if user_action.lower() == 'd':
            print("=" * 20)
            del_item = input("Enter the item(s) you wish to delete: ")
            if del_item in shopping_cart:
                del shopping_cart[del_item]
                print(f"You have successfully deleted {del_item} from your cart.")
            else:
                print("That item is not in your shopping cart.")
        if user_action.lower() == 's':
            print("=" * 35)
            print("=== YOUR SHOPPING CART ===")
            for item, price in shopping_cart.items():
                print(f"{item} -- ${price:.2f}")
            print("=== YOUR SHOPPING CART ===")
            print("=" * 35)
        if user_action.lower() == 'p':
            print("=" * 35)
            print("==== JERMART ====")
            for item, price in shopping_cart.items():
                print(f"{item} -- ${price:.2f}")
            subtotal = sum(shopping_cart.values())
            tax = subtotal * 0.1025
            total = tax + subtotal
            print("-" * 20)
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Tax: ${tax:.2f}")
            print(f"Total: ${total:.2f}")
            print("-" * 20)
            print("Thank you for shopping at JerMart!\nWe would love to see you again!")
            print("=" * 35)
            break
    else:
        print("Wrong answer. You should be shopping for groceries. >:(")

shopping()

# Ask for item input -> from dictionary .keys() -- if input == keys
# Ask for quantity of item -> variable
# Multiply price by quantity of item
# Add into dictionary inside(outside?) loop --> return after all is finished
# Loop user: "What do you want to do next? "
# If input == 'add', loop user again, add item and quantity to dictionary
# If input == 'quit', quit loop
    # Display receipt as a list e.g. (2 Apples $2.98)
    # Show total untaxed price
    # Show tax percentage
    # Show total price + tax 
# If input == 'delete', delete items
    # Display receipt as a list
    # Ask for user input -- "Which item would you like to delete?"
    # Find if input equals .keys() in dictionary of cart
    # Ask for user input -- "How many items would you like to delete?"
    # Multiply quantity to delete by item price, subtract total item price from quantity deleted price
    # Reevaluate items, total prices