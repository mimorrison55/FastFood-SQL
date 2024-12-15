from operations import operations

db = operations()

def main():
    # ----------------------------
    
    print()
    print("Welcome to the fast food order service.")
    print("Answers to the questions will be provided in parenthesis after each promt.")
    print("Make sure to input your answer exactly as one of the options shown.  ")
    unknown = input("Are you a new user?(y/n): ") # new users are always customers

    if unknown == 'y':
        mode = 'c'
        # make new user 
        while True:
            username = input("Enter your desired username (must be unique): ")
            #> check unique
            if db.username_check(username) == False:
                break
            input("That username is already in use, please ENTER to try again. ")
        firstName = input("What is your first name?: ")
        lastName = input("What is yout last name?: ")
        password = input("Create a password: ")
        # make user
        db.add_customer(username, password, firstName, lastName)
        
    else:
    # 1st: ask user to log in
        # > choose user or manager or root
        mode = input("Are you returning as a customer, manager, or root user? (c, m, r): ")
        # > enter password

    if mode == 'm':
        while True:
            eyedee = int(input("Enter you managerID number: "))
            # check ID valid
            if db.managerID_check(eyedee) == True:
                break
            input("The manager ID provided does not exist in the databse, press ENTER to try again.")
        while True:
            password = input("Enter your password: ")
            #password check
            if db.manager_password_check(eyedee, password) == True:
                break
            input("The password provided is incorrect, press ENTER to try again.")

        # log in manager
        print("Logging in as manager", eyedee, "...")

        # 3rd: manager option menu
        # > check item frequency
        # > check combo frequency
        # > check customer frequency
        # > check total earnings (by week/year/month?)
        # > show $ lost by combos
        while True:
            print()
            choice = input('''MANAGER MENU:
            1. Item frequency
            2. Combo frequency
            3. Total earnings
            4. Customer list
            5. Add new item
            6. Add new combo
            7. Quit
            ENTER NUMERICAL SELECTION: ''')
            print()

            if choice == '1':
                db.item_frequency(db.get_restraunt_from_manager(eyedee))
            elif choice == '2':
                db.combo_frequency(db.get_restraunt_from_manager(eyedee))
            elif choice == '3':
                db.total_earnings(db.get_restraunt_from_manager(eyedee))
            elif choice == '4':
                db.customer_list(db.get_restraunt_from_manager(eyedee))
            elif choice == '5':
                name = input("What is the new item called?: ")
                cost = input("How much will it cost?: ")
                calories = input("How many calories will it have ?: ")
                db.add_item(name, float(cost), float(calories), db.get_restraunt_from_manager(eyedee))
            elif choice == '6':
                print("Here is the items available at your restraunt:")
                db.print_filtered_items(db.get_restraunt_from_manager(eyedee))
                print("Enter the itemID of each item one by one that you would like to include into the combo,") 
                print("enter q to quit: ")
                items = []
                while True:
                    i = input()
                    if i == 'q':
                        break
                    items.append(int(i))
                name = input("What is the new combo called?: ")
                cost = input("How much will it cost?: ")
                db.add_combo(name, float(cost), db.get_restraunt_from_manager(eyedee))
                db.add_combo_items(items)
                db.combo_update_calories_all()
            elif choice == '7':
                break

    elif mode == 'c':
        if unknown == 'n':
            while True:
                username = input("Enter your username: ")
                if db.username_check(username) == True:
                    break
                input("The username provided does not exist in the databse, press ENTER to try again.")
            # check username valid
            while True:
                password = input("Enter your password: ")
                if db.customer_password_check(username, password) == True:
                    break
                input("The password provided is incorrect, press ENTER to try again.")
            
            # log is customer
            db.customer_welcome_back(username)

        # 2nd: user option menu
        # > check rewards points
        # > check past orders
        # > find options for a given item across all restraunts
        while True:
            print()
            choice = input('''CUSTOMER MENU:
            1. Start new order
            2. View Past orders
            3. Check rewards points
            4. Find specific item 
            5. Combo details
            6. QUIT
            ENTER NUMERICAL SELECTION: ''')
            print()

            if choice == '1':
                # enter restraunt id (show items and combos)
                db.print_restraunt_options()
                print()
                res = input("choose a restrauntID from above to order from: ")
                print()
                print("ITEM AND COMBOS AVAILIABLE FROM RESTAURANT", res)
                db.print_one_menu_items(int(res))
                db.print_one_menu_combos(int(res))
                order_items = []
                order_combos = []
                while True:
                    opt = input("Would you like to order a combo or individual item? (c/i): ")
                    if opt == 'c':
                        chk = input("Would you like to view any of the combo details? (y/n): ")
                        while chk == 'y':
                            combo = input("choose a comboID from above to get details: ")
                            db.combo_details(int(combo))
                            fin = input("Want another combo's details? (y/n): ")
                            if fin == 'n':
                                break
                        temp_c = input("What combo number would you want to include in the order?: ")
                        order_combos.append(int(temp_c))
                    elif opt == 'i':
                        temp_i = input("What item number would you like to include in the order?: ")
                        order_items.append(int(temp_i))
                    dun = input("Are you finished ordering? (y/n):")
                    if dun == 'y':
                        break
                db.order(int(res), db.id_from_username(username), order_items, order_combos)
                pass
            elif choice == '2':
                db.print_past_orders(db.id_from_username(username))
            elif choice == '3':
                db.print_points(username)
            elif choice == '4':
                item = input("What item would you like to search for?: ")
                db.find_items(item)
                db.find_combos(item)
            elif choice == '5':
                db.print_combos_clean()
                print()
                combo = input("choose a comboID from above to get details: ")
                db.combo_details(int(combo))
            elif choice == '6':
                break

    else:
        print("Logging in as root user. ")
        # 4th: root user menu
        # > show all tables (or one by one)
        # > get sum orders by restraunt
        # > get specific item orders across all restraunts
        # > get earning of each restraunt
        # > create new manager
        while True:
            print()
            choice = input('''ROOT USER MENU:
            1. Show individual tables
            2. Show all tables
            3. Total orders by restaurant
            4. Total earnings by restaurant
            5. Get item frequency across all restaurants 
            6. Create new restaurant
            7. Create new manager
            8. QUIT
            ENTER NUMERICAL SELECTION: ''')
            print()

            if choice == '1':
                tbles = input('''TABLES:
                1. Restaurants
                2. Managers
                3. Items
                4. Combos
                5. Item_combo
                6. Customers
                7. Orders
                8. Order_menu
                CHOOSE A TABLE FROM ABOVE TO PRINT (1-8): 
                ''')
                print_one(tbles)
            elif choice == '2':
                print_all()
            elif choice == '3':
                db.print_total_orders_all()
            elif choice == '4':
                db.print_total_earnings_all()
            elif choice == '5':
                print("ITEMS ORDERED ACROSS ALL RESTAURANTS: ")
                db.item_frequency_all()
            elif choice == '6':
                rname = input("What is the new restaurant called?: ")
                rate = float(input("What is this restaurants rating?: "))
                loc = input("What is the location?: ")
                db.create_new_restraunt(rname, rate, loc)
            elif choice == '7':
                db.print_restraunt_options()
                hire = int(input("Enter a restaurantID from above to add a manager to that restaurant: "))
                psw = input("What is the new manager's password?: ")
                db.create_new_manager(hire, psw)
            elif choice == '8':
                break



def create_database():
    db.create_restraunts()
    db.create_customers()
    db.create_managers()
    db.create_items()
    db.create_combos()
    db.create_orders()
    db.create_item_combo()
    db.create_order_menu()

def populate_database():
    db.populate_restraunts()
    db.populate_customers()
    db.populate_managers()
    db.populate_items()
    db.populate_combos()
    db.populate_orders()
    db.populate_item_combo()
    db.populate_order_menu()
    db.combo_update_calories_all()
    db.order_update_all()
    db.customer_update_points_all()

def print_one(val):
    print()
    if val == '1':
        print("RESTAURNTS:")
        db.print_restraunts()
    elif val == '2':
        print("MANAGERS: ")
        db.print_managers()
    elif val == '3':
        print("ITEMS: ")
        db.print_items()
    elif val == '4':
        print("COMBOS:")
        db.print_combos()
    elif val == '5':
        print("ITEM_COMBO:")
        db.print_item_combo()
    elif val == '6':
        print("CUSTOMERS:")
        db.print_customers()
    elif val == '7':
        print("ORDERS:")
        db.print_orders()
    elif val == '8':
        print("ORDER_MENU:")
        db.print_order_menu()
    print()

def print_all():
    print()
    print("RESTAURANTS:")
    db.print_restraunts()
    print()
    print("MANAGERS: ")
    db.print_managers()
    print()
    print("ITEMS: ")
    db.print_items()
    print()
    print("COMBOS:")
    db.print_combos()
    print()
    print("ITEM_COMBO:")
    db.print_item_combo()
    print()
    print("CUSTOMERS:")
    db.print_customers()
    print()
    print("ORDERS:")
    db.print_orders()
    print()
    print("ORDER_MENU:")
    db.print_order_menu()
    print()



if __name__ == '__main__':
    #create_database()
    #populate_database()
    main()
    #print_all()
    #db.clear_database()
    