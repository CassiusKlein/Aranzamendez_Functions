def display_menu():
    menu = {
        "1": {"name": "Cheeseburger", "price": 5.99},
        "2": {"name": "Shawarma Rice", "price": 8.99},
        "3": {"name": "Footlong", "price": 4.49},
        "4": {"name": "Water", "price": 1.99}
    }
    print("\nMenu:")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ${item['price']:.2f}")
    return menu

def get_user_choice(menu):
    while True:
        choice = input("\nEnter the number of the item of your order: ")
        if choice in menu:
            return menu[choice]
        else:
            print("Invalid choice. Please try again.")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input(f"The total cost is ${total_cost:.2f}. Please enter the cash amount: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment accepted. Your change is ${change:.2f}. Thank you!")
                break
            else:
                print("Insufficient amount. Please provide enough cash.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    menu = display_menu()
    selected_item = get_user_choice(menu)
    print(f"\nYou selected: {selected_item['name']} - ${selected_item['price']:.2f}")
    process_payment(selected_item['price'])

if __name__ == "__main__":
    main()
