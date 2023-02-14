# ========The beginning of the class==========
class Shoe:
    # Define shoe class
    # Initialize attributes

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define method to get the cost
    def get_cost(self):
        # This method returns the cost of the item
        return f'Cost: {self.cost}'

    # Define method to get the quantity
    def get_quantity(self):
        # This method returns the quantity of the item
        return f'Quantity: {self.quantity}'

    # Define method to save to file
    def to_file(self):
        # This method returns the format of the file header
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'

    # Define method to save input in a tabular format
    def to_table(self):
        # This method returns the format of a table header
        return [self.country, self.code, self.product, self.cost, self.quantity]

    # Define self string
    def __str__(self):
        # This method returns the string of the class attribute
        return f'''╔══════════════════════════════════╗
Country: {self.country}
Product code: {self.code} 
Product: {self.product} 
Product cost: {self.cost} 
Product quantity: {self.quantity}
╚══════════════════════════════════╝
        
'''



# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
The empty shoe list houses all shoe objects
'''
shoe_list = []


# ==========Functions outside the class==============
# Define function to read shoe data
def read_shoes_data():
    # Open text file for read
    # Use error handling to ensure the file exist and if not print error message
    # Use readline() method to skip the first row of the text file
    try:
        file = open('inventory.txt', 'r')
        file.readline()
    except FileNotFoundError:
        print('File does not exist')
        return
    # Loop through the file, strip file of new line character and split by comma
    # Assign class attributes to each index
    # Create shoe object
    # Append shoe object into shoe list
    for line in file:
        country, code, product, cost, quantity = line.strip('\n').split(',')
        shoe_object = Shoe(country, code, product, int(cost), int(quantity))
        shoe_list.append(shoe_object)


# Define function to capture shoes
def capture_shoes():
    # Create a while loop
    # Use try, except to handle errors
    # Request user input
    # If user enters incorrect value, print error message, go over the while loop again
    while True:
        try:
            country = input("What country is the shoe from: ")
            code = input("What is the shoe code: ")
            product = input("Enter shoe product: ")
            cost = int(input("Enter the cost of the shoe: "))
            quantity = int(input("Enter the quantity: "))
        except ValueError:
            print('You have imputed an invalid value')
            continue
        # Create a new shoe object form the shoe class
        # Append new shoe object to shoe list
        newshoe_object = Shoe(country, code, product, cost, quantity)
        shoe_list.append(newshoe_object)
        print(f"You have successfully captured {quantity} pieces of '{product}' shoe")
        # When you call the view all function, you will be able to see that the new shoe has been
        # appended as the last shoe object in the shoe list.
        view_all()
        break


# Define function to view all the item in the shoe list
def view_all():
    # Loop through the shoe list and print each item on the list
    for shoe in shoe_list:
        print(shoe)


# A function to update the text file
def update_file():
    # Open text file for write.
    # Write in the Header
    # Loop through the shoe list
    # Write in using the shoe to file method
    # Close file
    updated_file = open('inventory.txt', 'w')
    updated_file.write("Country, Code, Product, Cost, Quantity")
    for shoe in shoe_list:
        updated_file.write(f'\n{shoe.to_file()}')
    updated_file.close()


# A function to restock show with the lowest quantity
def re_stock():
    # Initialize the lowest quantity
    # Loop through the shoe list
    # Check if any quantity in index is less than the lowest quantity
    # If it is, set the lowest index as the index with the lowest quantity
    # Print the shoe object with the lowest shoe quantity
    lowest_quantity = shoe_list[0].quantity
    for i in range(len(shoe_list)):
        if shoe_list[i].quantity < lowest_quantity:
            lowest_quantity = shoe_list[i].quantity
            lowest_index = i
    print(shoe_list[lowest_index])

    # Create a while loop
    # Ask if user wants to update the quantity
    # If user chooses No, print response and break out of the loop
    # Else if user chooses Yes, Request user to input quantity
    # Use try, except to handle errors from user input
    while True:
        infor = input('Do you want to add to this quantity? Yes or No: ').lower()
        if infor == "no":
            print('Okay, Thank You!')
            break
        elif infor == "yes":
            try:
                update = int(input('Enter new quantity for product e.g 15: '))
                # Set lowest quantity with users input
                # Call the update file function
                shoe_list[lowest_index].quantity = update
                update_file()
                # Print user response
                print(f'You have updated the product \'{shoe_list[lowest_index].product}\' with {update} quantities. ')
                break
            except ValueError:
                print('You have entered an invalid value')
        else:
            # If user does not enter yes or no, print  error response
            # Go over the while loop again
            print('You have entered an invalid option')
            continue


#      This function will search for a shoe from the list
#      using the shoe code and return this object so that it will be printed.
def search_shoe():
    # Request shoe code from user
    # Initialize shoe position to -1
    shoe_code = input('Enter shoe code: ')
    shoe_position = -1
    # Loop through the shoe list
    # Check if the code of the shoe equals user input
    # If shoe code equals the user input, set shoe position to the index of the shoe code
    # if shoe code equals -1, print shoe code was not found
    # Print the shoe object of the index position.
    for index, shoe in enumerate(shoe_list):
        if shoe.code == shoe_code:
            shoe_position = index
    if shoe_position == -1:
        print(f'{shoe_code} was not found')
    else:
        print(shoe_list[shoe_position])


# A function to get the cost of a shoe
def cost_shoe():
    # Request user input of the shoe product they want to get the cost of
    # Initialize shoe position to -1
    shoe_product = input('Enter shoe product: ')
    shoe_position = -1
    # Loop through shoe list and check if any shoe product equals to user input
    # If shoe product equals user input, set shoe position to the index of the shoe code
    # if shoe product equals -1, print shoe product was not found
    # Print the shoe object of the index position.
    for index, shoe in enumerate(shoe_list):
        if shoe.product == shoe_product:
            shoe_position = index
    if shoe_position == -1:
        print(f'{shoe_product} was not found')
    else:
        print(f'{shoe_product}: {shoe_list[shoe_position].get_cost()}')
        print(shoe_list[shoe_position])


# A function to get the quantity of a shoe
def quantity_shoe():
    # Request user input of the shoe product they want to get the cost of
    # Initialize shoe position to -1
    shoe_product = input('Enter shoe product: ')
    shoe_position = -1
    # Loop through shoe list and check if any shoe product equals to user input
    # If shoe product equals user input, set shoe position to the index of the shoe code
    # if shoe product equals -1, print shoe product was not found
    # Print the quantity of shoe object
    # Print the shoe object of the index position
    for index, shoe in enumerate(shoe_list):
        if shoe.product == shoe_product:
            shoe_position = index
    if shoe_position == -1:
        print(f'{shoe_product} was not found')
    else:
        print(f' {shoe_product}: {shoe_list[shoe_position].get_quantity()}')
        print(shoe_list[shoe_position])


# This function will calculate the total value for each item.
# Value = cost * quantity.
def value_per_item():
    # Print Header
    print('PRODUCT  :   VALUE')
    # Loop through shoe list and print the shoe product and the value
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f'{shoe.product} : {value}')


# A function to determine the product with the highest quantity and
# print this shoe as being for sale
def highest_qty():
    # Initialize show with the highest quantity
    highest_quantity = shoe_list[0].quantity
    # Loop through the shoe list
    # Check if any quantity in index position is greater than the highest quantity
    # If it is, set the highest index as the index with the highest quantity
    # Print the shoe object with the highest shoe quantity
    for i in range(len(shoe_list)):
        if shoe_list[i].quantity > highest_quantity:
            highest_quantity = shoe_list[i].quantity
            highest_index = i
    print(shoe_list[highest_index])
    print(f'The product \'{shoe_list[highest_index].product}\' is on SALE. ')


# ==========Main Menu=============
'''
Create a menu that executes each function above.
'''
# Create a while loop
# Display options for user
# If user chooses an invalid option, print error message and go over loop again
# If user chooses a valid option, perform the function
# Ask if user would like another menu
# Exit when user chooses quit
while True:
    user_choice = input('''
    What would you like to do
    GC - Get cost
    CS - Capture Shoes
    GQ - Get quantity
    RSD - Read shoe data
    VA - View all
    RS - Re-stock
    SS - Search shoe
    VPI - Value per item
    HQ - Highest quantity
    Q - Quit
    :
    ''').lower()
    if user_choice == "gc":
        read_shoes_data()
        cost_shoe()
    elif user_choice == "cs":
        read_shoes_data()
        capture_shoes()
    elif user_choice == "gq":
        read_shoes_data()
        quantity_shoe()
    elif user_choice == "rsd":
        read_shoes_data()
    elif user_choice == "va":
        read_shoes_data()
        view_all()
    elif user_choice == "rs":
        read_shoes_data()
        re_stock()
    elif user_choice == "ss":
        read_shoes_data()
        search_shoe()
    elif user_choice == "vpi":
        read_shoes_data()
        value_per_item()
    elif user_choice == "hq":
        read_shoes_data()
        highest_qty()
    elif user_choice == "q":
        print("Goodbye!!!!!")
        break
    else:
        print('You have entered an invalid input')
        continue
