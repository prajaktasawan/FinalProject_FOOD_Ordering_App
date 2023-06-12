food_items = []
users = []
orders = []

def generate_food_id():
    if not food_items:
        return 1
    else:
        return food_items[-1]['food_id'] + 1

def generate_order_id():
    if not orders:
        return 1
    else:
        return orders[-1]['order_id'] + 1

def add_food_item(name, quantity, price, discount, stock):
    food_id = generate_food_id()
    food_item = {
        'food_id': food_id,
        'name': name,
        'quantity': quantity,
        'price': price,
        'discount': discount,
        'stock': stock
    }
    food_items.append(food_item)
    print("Food item added successfully!")

def edit_food_item(food_id):
    for food_item in food_items:
        if food_item['food_id'] == food_id:
            name = input("Enter the new name: ")
            quantity = input("Enter the new quantity: ")
            price = float(input("Enter the new price: "))
            discount = float(input("Enter the new discount: "))
            stock = int(input("Enter the new stock: "))

            food_item['name'] = name
            food_item['quantity'] = quantity
            food_item['price'] = price
            food_item['discount'] = discount
            food_item['stock'] = stock
            print("Food item edited successfully!")
            return

    print("Food item not found!")

def view_food_items():
    if not food_items:
        print("No food items available.")
    else:
        print("List of food items:")
        for food_item in food_items:
            print(f"FoodID: {food_item['food_id']}")
            print(f"Name: {food_item['name']}")
            print(f"Quantity: {food_item['quantity']}")
            print(f"Price: {food_item['price']}")
            print(f"Discount: {food_item['discount']}")
            print(f"Stock: {food_item['stock']}")
            print("")

def remove_food_item(food_id):
    for food_item in food_items:
        if food_item['food_id'] == food_id:
            food_items.remove(food_item)
            print("Food item removed successfully!")
            return

    print("Food item not found!")

def register_user():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    user = {
        'full_name': full_name,
        'phone_number': phone_number,
        'email': email,
        'address': address,
        'password': password
    }
    users.append(user)
    print("User registered successfully!")

def login_user(email, password):
    for user in users:
        if user['email'] == email and user['password'] == password:
            return user

    return None

def place_order(user):
    print("List of food items:")
    for food_item in food_items:
        print(f"{food_item['food_id']}. {food_item['name']} ({food_item['quantity']}) [INR {food_item['price']}]")

    order_items = []
    while True:
        selection = input("Select food item numbers to order (separated by commas): ")
        item_numbers = [int(num.strip()) for num in selection.split(',')]

        for number in item_numbers:
            if number < 1 or number > len(food_items):
                print("Invalid item number!")
                continue

            food_item = food_items[number - 1]
            order_items.append(food_item)

        more_items = input("Do you want to add more items to the order? (yes/no): ")
        if more_items.lower() != 'yes':
            break

    order_id = generate_order_id()
    order = {
        'order_id': order_id,
        'user': user,
        'order_items': order_items
    }
    orders.append(order)

    print("Order placed successfully!")
    print("Ordered Items:")
    for item in order_items:
        print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")

def view_order_history(user):
    user_orders = [order for order in orders if order['user'] == user]

    if not user_orders:
        print("No order history available.")
    else:
        print("Order History:")
        for order in user_orders:
            print(f"Order ID: {order['order_id']}")
            print("Ordered Items:")
            for item in order['order_items']:
                print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")
            print("")

def update_profile(user):
    full_name = input("Enter your new full name: ")
    phone_number = input("Enter your new phone number: ")
    address = input("Enter your new address: ")

    user['full_name'] = full_name
    user['phone_number'] = phone_number
    user['address'] = address

    print("Profile updated successfully!")


# Admin functionalities
def admin_login():
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")

    if admin_username == "admin" and admin_password == "adminpass":
        return True
    else:
        return False

def admin_menu():
    while True:
        print("\n----- Admin Menu -----")
        print("1. Add new food item")
        print("2. Edit food item")
        print("3. View list of all food items")
        print("4. Remove food item")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the food item name: ")
            quantity = input("Enter the quantity: ")
            price = float(input("Enter the price: "))
            discount = float(input("Enter the discount: "))
            stock = int(input("Enter the stock: "))

            add_food_item(name, quantity, price, discount, stock)
        elif choice == '2':
            food_id = int(input("Enter the food item ID to edit: "))
            edit_food_item(food_id)
        elif choice == '3':
            view_food_items()
        elif choice == '4':
            food_id = int(input("Enter the food item ID to remove: "))
            remove_food_item(food_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(user):
    while True:
        print("\n----- User Menu -----")
        print("1. Place New Order")
        print("2. Order History")
        print("3. Update Profile")
        print("0. Log out")

        choice = input("Enter your choice: ")

        if choice == '1':
            place_order(user)
        elif choice == '2':
            view_order_history(user)
        elif choice == '3':
            update_profile(user)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

# Main program
def main():
    while True:
        print("\n----- Food Ordering App -----")
        print("1. Admin Login")
        print("2. User Login")
        print("3. User Registration")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if admin_login():
                admin_menu()
            else:
                print("Invalid admin credentials!")
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            user = login_user(email, password)
            if user:
                user_menu(user)
            else:
                print("Invalid email or password!")
        elif choice == '3':
            register_user()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
