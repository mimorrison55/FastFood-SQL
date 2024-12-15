import mysql.connector
from datetime import datetime

class operations:

    def __init__(self):
        # if the conn_path (.db) DNE, it will be created in thos step
        self.connection = mysql.connector.connect(host="localhost",
                               user = "root",
                               password = "Pause80lie!",
                               auth_plugin = "mysql_native_password",
                               database = "FastFood")
        self.cursor = self.connection.cursor()
        print("connection established")

    # create tables ---------------------------------------------------------------------------------------------------------
    # create customers table
    def create_customers(self):
        query = '''
        CREATE TABLE customers(
            customerID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            username VARCHAR(30) NOT NULL,
            password TEXT NOT NULL,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            points INT);
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print('customers table created. ')

    # create managers table
    def create_managers(self):
        query = '''
        CREATE TABLE managers(
            managerID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            password TEXT NOT NULL,
            restrauntID INT NOT NULL,
            FOREIGN KEY (restrauntID) REFERENCES restraunts(restrauntID));
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print('managers table created. ')

    # create restraunts table
    def create_restraunts(self):
        query = '''
        CREATE TABLE restraunts(
            restrauntID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name TEXT NOT NULL,
            rating FLOAT, 
            location TEXT);
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print('restaurunts table created. ')

    # create orders table
    def create_orders(self):
        query = '''
        CREATE TABLE orders(
            orderID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            cost FLOAT,
            calories FLOAT,
            customerID INT NOT NULL,
            restrauntID INT NOT NULL,
            FOREIGN KEY (customerID) REFERENCES customers(customerID),
            FOREIGN KEY (restrauntID) REFERENCES restraunts(restrauntID));
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print('orders table created. ')

    # create items table
    def create_items(self):
        query = '''
        CREATE TABLE items(
            itemID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name TEXT NOT NULL,
            cost FLOAT NOT NULL,
            calories FLOAT NOT NULL,
            restrauntID INT NOT NULL,
            FOREIGN KEY (restrauntID) REFERENCES restraunts (restrauntID));
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print('items table created. ')

    # create combos table
    def create_combos(self):
        query = '''
        CREATE TABLE combos(
            comboID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name TEXT NOT NULL,
            cost FLOAT NOT NULL,
            calories FLOAT,
            restrauntID INT NOT NULL,
            FOREIGN KEY (restrauntID) REFERENCES restraunts (restrauntID));
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print('combos table created. ')

    # create junction tables ----------
    # create item_combo table
    def create_item_combo(self):
        query = '''
        CREATE TABLE item_combo(
            comboID INT NOT NULL,
            itemID INT NOT NULL,
            FOREIGN KEY (comboID) REFERENCES combos (comboID),
            FOREIGN KEY (itemID) REFERENCES items (itemID));
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print('item_combo junction table created. ')

    # create order_menu table
    def create_order_menu(self):
        query = '''
        CREATE TABLE order_menu(
            orderID INT NOT NULL,
            comboID INT,
            itemID INT,
            FOREIGN KEY (orderID) REFERENCES orders (orderID),
            FOREIGN KEY (comboID) REFERENCES combos (comboID),
            FOREIGN KEY (itemID) REFERENCES items (itemID));
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print('order_menu junction table created. ')

    # delete entire database ---------------------------------------------------------------------------------------------------
    def clear_database(self):
        queryEight = '''
        DROP TABLE order_menu;
        '''
        self.cursor.execute(queryEight)
        self.connection.commit()

        querySeven = '''
        DROP TABLE item_combo;
        '''
        self.cursor.execute(querySeven)
        self.connection.commit()

        querySix = '''
        DROP TABLE combos;
        '''
        self.cursor.execute(querySix)
        self.connection.commit()

        queryFive = '''
        DROP TABLE items;
        '''
        self.cursor.execute(queryFive)
        self.connection.commit()

        queryFour = '''
        DROP TABLE orders;
        '''
        self.cursor.execute(queryFour)
        self.connection.commit()

        queryTwo = '''
        DROP TABLE managers;
        '''
        self.cursor.execute(queryTwo)
        self.connection.commit()

        queryThree = '''
        DROP TABLE restraunts;
        '''
        self.cursor.execute(queryThree)
        self.connection.commit()

        queryOne = '''
        DROP TABLE customers;
        '''
        self.cursor.execute(queryOne)
        self.connection.commit()

        print('database cleared. ')
    
    # print each table -----------------------------------------------------------------------------------------------------
    # print customers
    def print_customers(self):
        query = '''
        SELECT customerID, username, firstName, lastName, points
        FROM customers;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["customerID", "username", "firstName", "lastName", "points"]

        # print out headers with fixed col width
        print(f"{headers[0]:<11} {headers[1]:<20} {headers[2]:<15} {headers[3]:<15} {headers[4]:<5}")

        # print seperator
        print('-'*75)

        #iterate through the results
        for row in results:
            customerID, username, firstName, lastName, points = row
            print(f"{customerID:<11} {username:<20} {firstName:<15} {lastName:<15} {str(points):<5}")

    def print_managers(self):
        query = '''
        SELECT managerID, restrauntID
        FROM managers;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["managerID", "restrauntID"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<10}")

        # print seperator
        print('-'*22)

        #iterate through the results
        for row in results:
            managerID, restrauntID = row
            print(f"{str(managerID):<10} {str(restrauntID):<10}")

    def print_restraunts(self):
        query = '''
        SELECT restrauntID, name, rating, location
        FROM restraunts;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["restrauntID", "name", "rating", "location"]

        # print out headers with fixed col width
        print(f"{headers[0]:<14} {headers[1]:<20} {headers[2]:<8} {headers[3]:<30}")

        # print seperator
        print('-'*65)

        #iterate through the results
        for row in results:
            restrauntID, name, rating, location = row
            print(f"{restrauntID:<14} {name:<20} {str(rating):<8} {location:<30}")

    def print_orders(self):
        query = '''
        SELECT orderID, cost, calories, customerID, restrauntID
        FROM orders;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["orderID", "cost", "calories", "customerID","restaurantID"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<6} {headers[2]:<9} {headers[3]:<10} {headers[4]:<10}")

        # print seperator
        print('-'*48)

        #iterate through the results
        for row in results:
            orderID, cost, calories, customerID, restrauntID = row
            print(f"{str(orderID):<10} {str(cost):<6} {str(calories):<9} {str(customerID):<10} {str(restrauntID):<10}")

    def print_items(self):
        query = '''
        SELECT itemID, name, cost, calories, restrauntID
        FROM items;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["itemID", "name", "cost", "calories", "restaurantID"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<6} {headers[3]:<9} {headers[4]:<10}")

        # print seperator
        print('-'*55)

        #iterate through the results
        for row in results:
            itemID, name, cost, calories, restrauntID = row
            print(f"{str(itemID):<10} {name:<20} {str(cost):<6} {str(calories):<9} {str(restrauntID):<10}")

    def print_combos(self):
        query = '''
        SELECT comboID, name, cost, calories, restrauntID
        FROM combos;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["comboID", "name", "cost", "calories", "restaurantID"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<5} {headers[3]:<9} {headers[4]:<10}")

        # print seperator
        print('-'*56)

        #iterate through the results
        for row in results:
            comboID, name, cost, calories, restrauntID = row
            print(f"{str(comboID):<10} {name:<20} {str(cost):<5} {str(calories):<9} {str(restrauntID):<10}")
        
    # print junction tables -----
    def print_item_combo(self):
        query = '''
        SELECT comboID, itemID
        FROM item_combo;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["comboID", "itemID"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<10}")

        # print seperator
        print('-'*20)

        #iterate through the results
        for row in results:
            comboID, itemID = row
            print(f"{str(comboID):<10} {str(itemID):<10}")
    
    def print_order_menu(self):
        query = '''
        SELECT orderID, comboID, itemID
        FROM order_menu;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["orderID", "comboID", "itemID"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<10} {headers[2]:<10}")

        # print seperator
        print('-'*30)

        #iterate through the results
        for row in results:
            orderID, comboID, itemID = row
            print(f"{str(orderID):<10} {str(comboID):<10} {str(itemID):<10}")

    # populate tables with default values --------------------------------------------------------
    # restraunts
    def populate_restraunts(self):
        query = '''
        INSERT INTO restraunts(name, rating, location) VALUES
        ('McDonalds', 3.0, '123 Main St'),
        ('Jack in the Box', 3.5, '101 Parkway Ave'),
        ('In-n-Out', 5.0, '555 Circle Way'),
        ('Taco Bell', 4.0, '90 Jackson Blvd');
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print("restaurants populated.")

    # customers
    def populate_customers(self):
        query = '''
        INSERT INTO customers(username, password, firstName, lastName) VALUES
        ('jSnow', 'ghost', 'John', 'Snow'),
        ('wizard1', 'hedwig', 'Harry', 'Potter'),
        ('reaper', 'virginia', 'Darrow', 'O-Lykos'),
        ('barrelz4lyfe', 'zurfing', 'Chicken', 'Joe');
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print("customers populated.")

    # managers
    def populate_managers(self):
        query = '''
        INSERT INTO managers(password, restrauntID) VALUES
        ('mcds', 1),
        ('jbox', 2),
        ('inout', 3),
        ('tbell', 4);
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print("managers populated.")

    # items
    def populate_items(self):
        query = '''
        INSERT INTO items(name, cost, calories, restrauntID) VALUES
        ('cheeseburger', 3.50, 300, 1),
        ('hamburger', 3.00, 250, 1),
        ('fries', 1.50, 200, 1),
        ('chicken nuggets', 4.00, 200, 1),
        ('chicken sandwich', 4.50, 350, 1),
        ('ice cream cone', 1.50, 100, 1),
        ('milkshake', 2.50, 300, 1),
        ('soda', 1.00, 150, 1),
        ('cheeseburger', 4.50, 350, 2),
        ('hamburger', 4.00, 300, 2),
        ('chicken sandwich', 4.50, 400, 2),
        ('fries', 2.50, 200, 2),
        ('curly fries', 3.00, 250, 2),
        ('taco', 0.50, 100, 2),
        ('milkshake', 3.00, 250, 2),
        ('soda', 1.00, 150, 2),
        ('cheeseburger', 2.50, 300, 3),
        ('hamburger', 2.00, 250, 3),
        ('fries', 2.00, 200, 3),
        ('soda', 1.50, 150, 3),
        ('milkshake', 2.00, 200, 3),
        ('taco', 1.50, 150, 4),
        ('burrito', 4.00, 350, 4),
        ('chips and queso', 2.00, 200, 4),
        ('ice cream cone', 0.50, 100, 4),
        ('loco taco', 2.00, 200, 4),
        ('soda', 1.00, 150, 4);
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print("items populated.")

    # combos
    def populate_combos(self):
        query = '''
        INSERT INTO combos(name, cost, restrauntID) VALUES
        ('number 1', 5.50, 1),
        ('number 2', 6.00, 1),
        ('number 3', 7.00, 1),
        ('happy meal', 5.00, 1),
        ('number 1', 6.00, 2),
        ('number 2', 7.00, 2),
        ('number 3', 8.00, 2),
        ('munchie meal', 9.00, 2),
        ('number 1', 5.00, 3),
        ('number 2', 5.50, 3),
        ('the box', 9.00, 4);
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print("combos populated.")

    # orders
    def populate_orders(self):
        query = '''
        INSERT INTO orders(customerID, restrauntID) VALUES
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 1),
        (3, 2),
        (4, 3),
        (4, 4);
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print("orders populated.")

    # item_combo
    def populate_item_combo(self):
        query = '''
        INSERT INTO item_combo(comboID, itemID) VALUES
        (1, 2),
        (1, 3),
        (1, 8),
        (2, 1),
        (2, 3),
        (2, 8),
        (3, 5),
        (3, 3),
        (3, 8),
        (4, 4),
        (4, 3),
        (5, 10),
        (5, 12),
        (5, 16),
        (6, 9),
        (6, 12),
        (6, 16),
        (7, 11),
        (7, 12),
        (7, 16),
        (8, 10),
        (8, 12),
        (8, 16),
        (8, 14),
        (8, 14),
        (9, 18),
        (9, 19),
        (9, 20),
        (10, 17),
        (10, 19),
        (10, 20),
        (11, 22),
        (11, 23),
        (11, 24),
        (11, 26),
        (11, 27);
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print("item_combo populated.")

    # order_menu
    def populate_order_menu(self):
        query = '''
        INSERT INTO order_menu(orderID, comboID, itemID) VALUES
        (1, 1, NULL),
        (1, 4, NULL),
        (2, 8, NULL),
        (2, NULL, 15),
        (3, 9, NULL),
        (4, 11, NULL);
        '''

        self.cursor.execute(query)
        self.connection.commit()
        print("order_menu populated.")

    ## menu functionality functions -------------------------------------------------------------------------------------------------------------------------------
    # get list of usernames
    def get_usernames(self):
        # get all usernames from customers
        queryOne = '''
        SELECT username
        FROM customers;
        '''

        # execute 
        self.cursor.execute(queryOne)
        results = self.cursor.fetchall()

        username_list = []
        for row in results:
            #print(row[0], "-")
            username_list.append(row[0])
        
        return username_list
        

    # customer username check
    def username_check(self, username):
        #print("!", self.get_usernames())
        if username in self.get_usernames():
            return True
        else:
            return False
        
    # customer password check
    def customer_password_check(self, username, password):
        query = '''
        SELECT password
        FROM customers
        WHERE username = '%s';
        '''

        self.cursor.execute(query % username)
        result = self.cursor.fetchall()

        for row in result:
            check, = row
        
        if check == password:
            return True
        else:
            return False
        
    # get max manager ID
    def get_managerIDs(self):
        # get all IDS from managers
        queryOne = '''
        SELECT managerID
        FROM managers;
        '''

        # execute 
        self.cursor.execute(queryOne)
        results = self.cursor.fetchall()

        maxID = 0
        for row in results:
            maxID += 1
        
        return maxID

    # check if manager ID in table
    def managerID_check(self, id):
        if int(id) <= self.get_managerIDs():
            return True
        else:
            return False
        
    # manager password check
    def manager_password_check(self, id, password):
        query = '''
        SELECT password
        FROM managers
        WHERE managerID = '%d';
        '''

        self.cursor.execute(query % id)
        result = self.cursor.fetchall()

        for row in result:
            check, = row
        
        if check == password:
            return True
        else:
            return False
    
    def customer_welcome_back(self, username):
        query = '''
        SELECT firstName, lastName
        FROM customers
        WHERE username = '%s';
        '''

        self.cursor.execute(query % username)
        result = self.cursor.fetchall()

        for row in result:
            firstName, lastName, = row
        
        print("Welcome back", firstName, lastName)

    def add_customer(self, username, password, firstName, lastName):
        insert = '''
        INSERT INTO customers(username, password, firstName, lastname, points) 
        VALUES ('%s', '%s', '%s', '%s', 0);
        '''

        self.cursor.execute(insert % (username, password, firstName, lastName))
        self.connection.commit()

        print("New customer added to the databse. ")

    def combo_update_calories(self, comboID):
        query = '''
        SELECT SUM(i.calories)
        FROM item_combo AS ic
        INNER JOIN items AS i ON ic.itemID = i.itemID
        WHERE ic.comboID = '%d';
        '''

        self.cursor.execute(query % comboID)
        result = self.cursor.fetchall()

        for row in result:
            calories, = row

        update = '''
        UPDATE combos
        SET calories = '%.1f'
        WHERE comboID = '%d';
        '''

        self.cursor.execute(update % (calories, comboID))
        self.connection.commit()

    def get_combos(self):
        #get all IDS from combos
        query = '''
        SELECT comboID
        FROM combos;
        '''

        # execute 
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        maxID = 0
        for row in results:
            maxID += 1
        
        return maxID
    
    def combo_update_calories_all(self):
        i = 1
        while i <= self.get_combos():
            self.combo_update_calories(i)
            i += 1


    def order_update_cost(self, orderID):
        queryOne = '''
        SELECT SUM(c.cost)
        FROM order_menu AS om
        INNER JOIN combos AS c ON om.comboID = c.comboID
        WHERE om.orderID = '%d';
        '''

        self.cursor.execute(queryOne % orderID)
        result = self.cursor.fetchall()

        for row in result:
            combo_cost, = row

        queryTwo = '''
        SELECT SUM(i.cost)
        FROM order_menu AS om
        INNER JOIN items AS i ON om.itemID = i.itemID
        WHERE om.orderID = '%d';
        '''

        self.cursor.execute(queryTwo % orderID)
        result = self.cursor.fetchall()

        for row in result:
            item_cost, = row

        if combo_cost == None:
            combo_cost = 0
        if item_cost == None:
            item_cost = 0
        
        total_cost = combo_cost + item_cost

        update = '''
        UPDATE orders
        SET cost = '%.2f'
        WHERE orderID = '%d';
        '''
        self.cursor.execute(update % (total_cost, orderID))
        self.connection.commit()

    def order_update_calories(self, orderID):
        queryOne = '''
        SELECT SUM(c.calories)
        FROM order_menu AS om
        INNER JOIN combos AS c ON om.comboID = c.comboID
        WHERE om.orderID = '%d';
        '''

        self.cursor.execute(queryOne % orderID)
        result = self.cursor.fetchall()

        for row in result:
            combo_calories, = row

        queryTwo = '''
        SELECT SUM(i.calories)
        FROM order_menu AS om
        INNER JOIN items AS i ON om.itemID = i.itemID
        WHERE om.orderID = '%d';
        '''

        self.cursor.execute(queryTwo % orderID)
        result = self.cursor.fetchall()

        for row in result:
            item_calories, = row
        
        if combo_calories == None:
            combo_calories = 0
        if item_calories == None:
            item_calories = 0
        
        total_calories = combo_calories + item_calories

        update = '''
        UPDATE orders
        SET calories = '%.2f'
        WHERE orderID = '%d';
        '''
        self.cursor.execute(update % (total_calories, orderID))
        self.connection.commit()

    def get_orderIDs(self):
        #get all IDS from managers
        query = '''
        SELECT orderID
        FROM orders;
        '''

        # execute 
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        maxID = 0
        for row in results:
            maxID += 1
        
        return maxID

    def order_update_all(self):
        i = 1
        while i <= self.get_combos():
            self.order_update_calories(i)
            self.order_update_cost(i)
            i += 1

    def customer_update_points(self, username):
        query = '''
        SELECT SUM(o.cost)
        FROM orders AS o
        INNER JOIN customers AS c ON c.customerID = o.customerID
        WHERE c.username = '%s';
        '''

        self.cursor.execute(query % username)
        result = self.cursor.fetchall()

        for row in result:
            cost, = row
        
        cost /= 10
        
        update = '''
        UPDATE customers
        SET points = '%.2f'
        WHERE username = '%s';
        '''
        self.cursor.execute(update % (cost, username))
        self.connection.commit()
    
    def customer_update_points_all(self):
        for i in self.get_usernames():
            self.customer_update_points(i)

    # manager menu functions -------------------------------------------------------------------------------------------------------------------

    def item_frequency(self, restrauntID):
        query = '''
        SELECT name, COUNT(*) AS num_sold
        FROM orders AS o 
        INNER JOIN order_menu AS om ON om.orderID = o.orderID 
        INNER JOIN items AS c ON c.itemID = om.itemID 
        WHERE o.restrauntID = '%d' 
        GROUP BY name;
        '''

        self.cursor.execute(query % restrauntID)
        result = self.cursor.fetchall()

        headers = ["item_name", "num_sold"]

        # print out headers with fixed col width
        print()
        print(f"{headers[0]:<15} {headers[1]:<8} ")

        # print seperator
        print('-'*23)

        count = 0
        for row in result:
            count += 1
            name, num = row
            print(f"{name:<15} {str(num):<8}")


        if count == 0:
            hold = "none"
            print(f"{hold:<15} {hold:<8}")

        print()

    def combo_frequency(self, restrauntID):
        query = '''
        SELECT name, COUNT(*) AS num_sold
        FROM orders AS o 
        INNER JOIN order_menu AS om ON om.orderID = o.orderID 
        INNER JOIN combos AS c ON c.comboID = om.comboID 
        WHERE o.restrauntID = '%d' 
        GROUP BY name;
        '''

        self.cursor.execute(query % restrauntID)
        result = self.cursor.fetchall()

        headers = ["combo_name", "num_sold"]

        # print out headers with fixed col width
        print()
        print(f"{headers[0]:<15} {headers[1]:<8} ")

        # print seperator
        print('-'*23)

        count = 0
        for row in result:
            count += 1
            name, num = row
            print(f"{name:<15} {str(num):<8}")

        if count == 0:
            hold = "none"
            print(f"{hold:<15} {hold:<8}")

        print()

    # get restrauntID from manager ID
    def get_restraunt_from_manager(self, managerID):
        query = '''
        SELECT restrauntID
        FROM managers
        WHERE managerID = '%d';
        '''

        self.cursor.execute(query % managerID)
        result = self.cursor.fetchall()

        for row in result:
            restraunt, = row

        return restraunt
    
    def total_earnings(self, restrauntID):
        query = '''
        SELECT SUM(cost)
        FROM orders
        WHERE restrauntID = '%d';
        '''

        self.cursor.execute(query % restrauntID)
        result = self.cursor.fetchall()

        for row in result:
            cost, = row

        print()
        print("Total earnings: ", cost)
        print()

    def customer_list(self, restrauntID):
        query = '''
        SELECT DISTINCT c.customerID, firstName, lastName
        FROM orders AS o
        INNER JOIN customers AS c ON c.customerID = o.customerID
        WHERE restrauntID = '%d';
        '''

        self.cursor.execute(query % restrauntID)
        result = self.cursor.fetchall()

        headers = ["customerID", "firstName", "lastName"]

        # print out headers with fixed col width
        print()
        print(f"{headers[0]:<15} {headers[1]:<15} {headers[2]:<15}")

        # print seperator
        print('-'*45)

        count = 0
        for row in result:
            count += 1
            id, first, last = row
            print(f"{str(id):<15} {first:<15} {last:<15}")

        if count == 0:
            hold = "none"
            print(f"{hold:<15} {hold:<15} {hold:<15}")

        print()

    def add_item(self, name, cost, calories, restrauntID):
        insert = '''
        INSERT INTO items(name, cost, calories, restrauntID) 
        VALUES ('%s', '%f', '%f', '%d');
        '''

        self.cursor.execute(insert % (name, cost, calories, restrauntID))
        self.connection.commit()

        print("New item added to the database for restraunt", restrauntID)

    def add_combo(self, name, cost, restrauntID):
        insert = '''
        INSERT INTO combos(name, cost, restrauntID) 
        VALUES ('%s', '%f', '%d');
        '''

        self.cursor.execute(insert % (name, cost, restrauntID))
        self.connection.commit()

        print("New combo added to the database for restaurant", restrauntID)

    def add_combo_items(self, item_list):
        comboID = self.get_combos()
        insert = '''
        INSERT INTO item_combo(comboID, itemID) 
        VALUES ('%d', '%d');
        '''

        for i in item_list:
            self.cursor.execute(insert % (comboID, i))
        
        self.connection.commit()

        print("combo_item table updated")
    
    def print_filtered_items(self, restrauntID):
        query = '''
        SELECT itemID, name, cost, calories, restrauntID
        FROM items
        WHERE restrauntID = '%d';
        '''
        self.cursor.execute(query % restrauntID)
        results = self.cursor.fetchall()

        # print out list in a good way!
        print()
        headers = ["itemID", "name", "cost", "calories", "restaurantID"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<6} {headers[3]:<9} {headers[4]:<10}")

        # print seperator
        print('-'*55)

        #iterate through the results
        for row in results:
            itemID, name, cost, calories, rID = row
            print(f"{str(itemID):<10} {name:<20} {str(cost):<6} {str(calories):<9} {str(rID):<10}")
        print()

    # customer selection functions -----------------------------------------------------------------------------------------------------------
    def print_points(self, username):
        query = '''
        SELECT points 
        FROM customers 
        WHERE username = '%s';
        '''

        self.cursor.execute(query % username)
        results = self.cursor.fetchall()

        for row in results:
            amount, = row
        
        print("You have", amount, "rewards points.")
        value = amount / 10.0
        print("This is equivalent to", str(value), "dollars of store credit.")
    
    def print_past_orders(self, id):
        query = '''
        SELECT orderID, cost, calories, name
        FROM orders AS o
        INNER JOIN restraunts AS r ON r.restrauntID = o.restrauntID
        WHERE customerID = '%d';
        '''
        self.cursor.execute(query % id)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["orderID", "cost", "calories", "name"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<6} {headers[2]:<9} {headers[3]:<10}")

        # print seperator
        print('-'*38)

        #iterate through the results
        for row in results:
            orderID, cost, calories, name = row
            print(f"{str(orderID):<10} {str(cost):<6} {str(calories):<9} {name:<10}")

    def id_from_username(self, username):
        query = '''
        SELECT customerID
        FROM customers
        WHERE username = '%s';
        '''

        self.cursor.execute(query % username)
        results = self.cursor.fetchall()

        for row in results:
            num, = row
        
        return num
    
    def find_items(self, name):
        query = '''
        SELECT itemID, i.name, cost, calories, r.name
        FROM items AS i
        INNER JOIN restraunts AS r ON r.restrauntID = i.restrauntID
        WHERE i.name = '%s';
        '''

        self.cursor.execute(query % name)
        results = self.cursor.fetchall()

        headers = ["itemID", "item", "cost", "calories", "restaurant"]

        # print out headers with fixed col width
        print()
        print("INDIVIDUAL", name, "FROM EACH RESTAURANT: ")
        print(f"{headers[0]:<15} {headers[1]:<15} {headers[2]:<15} {headers[3]:<15} {headers[4]:<15}")

        # print seperator
        print('-'*75)

        count = 0
        for row in results:
            count += 1
            itemID, item, cost, calories, restraunt = row
            print(f"{str(itemID):<15} {item:<15} {str(cost):<15} {str(calories):<15} {restraunt:<15}")

        if count == 0:
            hold = "none"
            print(f"{hold:<15} {hold:<15} {hold:<15} {hold:<15} {hold:<15}")

        print()

    def find_combos(self, name):
        query = '''
        SELECT DISTINCT ic.comboID, c.name, c.cost, c.calories, r.name
        FROM item_combo AS ic
        INNER JOIN combos AS c ON c.comboID = ic.comboID
        INNER JOIN items AS i ON i.itemID = ic.itemID
        INNER JOIN restraunts AS r ON r.restrauntID = c.restrauntID
        WHERE i.name = '%s';
        '''

        # execute 
        self.cursor.execute(query % name)
        results = self.cursor.fetchall()

        headers = ["comboID", "item", "cost", "calories", "restaurant"]

        # print out headers with fixed col width
        print()
        print("COMBOS THAT CONTAIN", name, "FROM EACH RESTAURANT: ")
        print(f"{headers[0]:<15} {headers[1]:<15} {headers[2]:<15} {headers[3]:<15} {headers[4]:<15}")

        # print seperator
        print('-'*75)

        count = 0
        for row in results:
            count += 1
            comboID, item, cost, calories, restraunt = row
            print(f"{str(comboID):<15} {item:<15} {str(cost):<15} {str(calories):<15} {restraunt:<15}")

        if count == 0:
            hold = "none"
            print(f"{hold:<15} {hold:<15} {hold:<15} {hold:<15} {hold:<15}")

        print()

    def print_combos_clean(self):
        query = '''
        SELECT c.comboID, c.name, c.cost, c.calories, r.name
        FROM combos AS c
        INNER JOIN restraunts AS r ON r.restrauntID = c.restrauntID;
        '''
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # print out playlist in a good way!
        headers = ["comboID", "name", "cost", "calories", "restaurant"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<5} {headers[3]:<9} {headers[4]:<20}")

        # print seperator
        print('-'*66)

        #iterate through the results
        for row in results:
            comboID, name, cost, calories, restraunt = row
            print(f"{str(comboID):<10} {name:<20} {str(cost):<5} {str(calories):<9} {restraunt:<20}")

    def combo_details(self, comboID):
        # get a list of every item in a combo
        query = '''
        SELECT i.name
        FROM item_combo AS ic
        INNER JOIN items AS i ON i.itemID = ic.itemID
        WHERE ic.comboID = '%d';
        '''

        self.cursor.execute(query % comboID)
        results = self.cursor.fetchall()

        items = []
        for row in results:
            name, = row
            items.append(name)
        print()
        print("Items included in comboID:", comboID)
        for i in items:
            print(">", i)

        print()

    def print_restraunt_options(self):
        query = '''
        SELECT restrauntID, name, location
        FROM restraunts;
        '''

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        print()
        headers = ["restaurantID", "name", "location"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<20}")

        # print seperator
        print('-'*40)

        #iterate through the results
        for row in results:
            restrauntID, name, location = row
            print(f"{restrauntID:<20} {name:<20} {location:<20}")
        print()

    def print_one_menu_items(self, restrauntID):
        query = '''
        SELECT itemID, name, cost, calories
        FROM items
        WHERE restrauntID = '%d';
        '''

        self.cursor.execute(query % restrauntID)
        results = self.cursor.fetchall()

        print()
        headers = ["itemID", "name", "cost", "calories"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<10} {headers[2]:<10}")

        # print seperator
        print('-'*60)

        #iterate through the results
        for row in results:
            itemID, name, cost, calories = row
            print(f"{itemID:<20} {name:<20} {cost:<10} {calories:<10}")
        print()

    def print_one_menu_combos(self, restrauntID):
        query = '''
        SELECT comboID, name, cost, calories
        FROM combos
        WHERE restrauntID = '%d';
        '''

        self.cursor.execute(query % restrauntID)
        results = self.cursor.fetchall()

        print()
        headers = ["comboID", "name", "cost", "calories"]

        # print out headers with fixed col width
        print(f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<10} {headers[2]:<10}")

        # print seperator
        print('-'*60)

        #iterate through the results
        for row in results:
            comboID, name, cost, calories = row
            print(f"{comboID:<20} {name:<20} {cost:<10} {calories:<10}")
        print()

    def order(self, restrauntID, customerID, items, combos):
        input = '''
        INSERT INTO orders(customerID, restrauntID)
        VALUES ('%d', '%d');
        '''

        self.cursor.execute(input % (customerID, restrauntID))
        self.connection.commit()

        input_items = '''
        INSERT INTO order_menu(orderID, itemID)
        VALUES ('%d', '%d');
        '''

        for i in items:
            self.cursor.execute(input_items %(self.get_orderIDs(), i))

        input_combos = '''
        INSERT INTO order_menu(orderID, comboID)
        VALUES ('%d', '%d');
        '''

        for c in combos:
            self.cursor.execute(input_combos %(self.get_orderIDs(), c))
        
        self.connection.commit()

        self.order_update_all()
        self.customer_update_points_all()

    ## root user functions -----------------------------------------------------------------------------------------------------------------------
    def print_total_orders_all(self):
        query = '''
        SELECT r.name, COUNT(o.orderID) as total_orders
        FROM orders AS o
        INNER JOIN restraunts AS r ON r.restrauntID = o.restrauntID
        GROUP BY r.name;
        '''

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        print()
        headers = ["name", "total_orders"]

        # print out headers with fixed col width
        print(f"{headers[0]:<20} {headers[1]:<10} ")

        # print seperator
        print('-'*30)

        #iterate through the results
        for row in results:
            name, total_cost = row
            print(f"{name:<20} {total_cost:<20}")
        print()

    def print_total_earnings_all(self):
        query = '''
        SELECT r.name, SUM(o.cost) as total_earnings
        FROM orders AS o
        INNER JOIN restraunts AS r ON r.restrauntID = o.restrauntID
        GROUP BY r.name;
        '''

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        print()
        headers = ["name", "total_earnings"]

        # print out headers with fixed col width
        print(f"{headers[0]:<20} {headers[1]:<10} ")

        # print seperator
        print('-'*30)

        #iterate through the results
        for row in results:
            name, total_earnings = row
            print(f"{name:<20} {total_earnings:<20}")
        print()

    def item_frequency_all(self):
        query = '''
        SELECT i.name, COUNT(*) as total
        FROM order_menu AS om
        INNER JOIN items AS i ON i.itemID = om.itemID
        GROUP BY i.name;
        '''

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        print()
        headers = ["item", "total_orders"]

        # print out headers with fixed col width
        print(f"{headers[0]:<20} {headers[1]:<10} ")

        # print seperator
        print('-'*30)

        #iterate through the results
        items = []
        totals = []
        for row in results:
            item, total = row
            items.append(item)
            totals.append(total)
            #print(f"{item:<20} {total:<20}")
        
        query = '''
        SELECT i.name, COUNT(*) as total
        FROM order_menu AS om 
        INNER JOIN item_combo AS ic ON ic.comboID = om.comboID 
        INNER JOIN items AS i ON i.itemID = ic.itemID
        GROUP BY i.name;
        '''

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        place = 0
        for row in results:
            item, total = row
            if items[place] == item:
                total += totals[place]
                place += 1
            print(f"{item:<20} {total:<20}")
        
        if place < len(items):
            for i in items:
                print(f"{i:<20} {totals[place]:<20}")
                place += 1
        

        print()

    def create_new_manager(self, restrauntID, password):
        input = '''
        INSERT INTO managers(restrauntID, password)
        VALUES ('%d', '%s');
        '''

        self.cursor.execute(input %(restrauntID, password))
        self.connection.commit()

        print("Manager for restaurant",restrauntID, "added to the database. ")

    def create_new_restraunt(self, name, rating, location):
        input = '''
        INSERT INTO restraunts(name, rating, location)
        VALUES ('%s', '%f', '%s');
        '''

        self.cursor.execute(input %(name, rating, location))
        self.connection.commit()

        print(name, "added to the database. ")