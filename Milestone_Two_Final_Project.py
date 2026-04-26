#this is building the shopping care for the project. 

#importing the class from Milestone one to use in this project. 

#working on a modular principle and importing what I need from Milestone One. 
from Milestone_One_Final_Project import ItemsToPurchase
#importing datetime to handle proper formats
import datetime
#built to get the right date in the right format, otherwise it won't accept.
def get_valid_date():
    formats = [
        "%d %m %Y",  # 31 12 2020
        "%d %m %y",  # 31 12 20
        "%B %d %Y",  # December 31 2020
        "%B %d %y",  # December 31 20
        "%b %d %Y",  # Dec 31 2020
        "%b %d %y",  # Dec 31 20
        "%d %B %Y",  # 31 December 2020
        "%d %B %y",  # 31 December 20
        "%d %b %Y",  # 31 Dec 2020
        "%d %b %y",  # 31 Dec 20
    ]
    #forcing fucntion for the proper date format. 
    while True:
        user_input = input("Enter the current date : ").title()
        
        for fmt in formats:
            try:
                valid_date = datetime.datetime.strptime(user_input, fmt)
                return valid_date.strftime("%d %B, %Y")  # Return in a consistent format
            except ValueError:
                continue
        print("Invalid date format. Please try again.") #respone to bad date format.
#This class is designed for the shopping care to be able to add, remove, modify, view and checkout. 
class ShoppingCart:
    # initlize care at zero.
    cart_count = 0
    #new user date constructor for name and date, could later use this to create tracking of what people buy over time. 
    def __init__(self, customer_name= 'none', current_date= 'January 1 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        
     
    #append for new items added to the cart. 
    def add_item(self, new_item):
        self.cart_items.append(new_item)
        
    #remove for items that need to be removed, just from name of item all information is removed and customer notified.    
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                print(f'{item_name} has been removed from the cart.')
                break
        #this is for items not in the cart and nothing removed. 
        if not found:
            print('Item not found in the cart.')
            
        
    # this allows the user to modify desription, price and quantity of an item in the cart. 
    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                
                if item_to_modify.item_description != 'none':
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                print(f'{item.item_name} has been modified in the cart.')                
                return
        
    #this lays out what is in the cart and descripttions of the items only.         
    def view_cart_descriptions(self):
        if self.get_num_items_in_cart() == 0:
            print('Your shopping cart is empty.')
        else:
            print()
            print("OUTPUT ITEMS' DESCRIPTIONS")
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            print('-' * 40)
            print(f'{'Item':<20}{"Description":<20}')
            print('-' * 40)
            for item in self.cart_items:
                print(f'{item.item_name:<20}{item.item_description:<20}')
        print()
            
    #creates a running total of quanity of items in the cart, not number of items but total items in cart.        
    def get_num_items_in_cart(self):
        num_items_in_cart = 0
        for item in self.cart_items:
            num_items_in_cart += item.item_quantity
        return num_items_in_cart
    #creates a running total of cost to create teh final cost for checkout.         
    def get_cost_of_cart(self): 
        running_cost = 0
        for item in self.cart_items:
            total_cost = item.item_price * item.item_quantity
            running_cost += total_cost
        return running_cost
    #this is the final checkout with full description and total price, attempted to layout like a real reciept.
    def print_total(self):
        if self.get_num_items_in_cart() == 0:
            print('Your shopping cart is empty.')
        else:
            print()
            print('OUTPUT SHOPPING CART')
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            print(f'{"Item":<20}{"Description":<20}{"Quantity":<10}{"Price":<10}{"Total":<10}')
            print('-' * 70)
            for item in self.cart_items:
                item_total = item.item_price * item.item_quantity
                print(f'{item.item_name:<20}{item.item_description:<20}{item.item_quantity:<10}${item.item_price:<10}${item_total:<10}')
            print()
            print(f'{"-" * 20 :>70}')
            print(f'{"Total:":>60} ${self.get_cost_of_cart()}')
        print()
        

#menu to work from to start the process. 
def print_menu(cart):
    menu = ()
    #this is the menu for using the program for the shopping cart. 
    choice = ''
    while choice != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('m - Modify item quantity')
        print('v - View current cart')
        print('c - Checkout')
        print('q - Quit')
        # serveral if elif statements depending on the user choice from the menu. 
        choice = input('Choose an option: ').strip().lower() 
        if choice == 'a':
            print('Proceeding to add an item in the cart...')
            item_name: str = input('Enter the item name: ')
            item_description: str = input('Enter the item description: ')
            item_price = int(input('Enter the item price: '))
            item_quantity = int(input('Enter the item quantity: '))
            new_item = ItemsToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(new_item)
        elif choice == 'r':
            print('Proceeding to remove an item in the cart...')
            remove_item_name = input('Enter the name of the item to remove: ')
            cart.remove_item(remove_item_name)
        elif choice == 'm':
            print('Proceeding to modify an item in the cart...')
            found_in_cart = False
            item_name = input('Enter the name of the item to modify: ')
            for item in cart.cart_items:
                if item.item_name == item_name:
                    found_in_cart = True
                    break
            if found_in_cart:
                temp_item_description = input('Enter the item description: (or type "none" to skip)')
                temp_item_price = int(input('Enter the new price for the item: (or type 0 to skip) '))
                temp_item_quantity = int(input('Enter the new quantity for the item: (or type 0 to skip) '))
                temp_item = ItemsToPurchase(item_name, temp_item_description, temp_item_price, temp_item_quantity)
                cart.modify_item(temp_item)
            else:
                print('Item not found in the cart. Cannot modify an item that is not in the cart.')
        elif choice == 'v':
            cart.view_cart_descriptions()
        elif choice == 'c':
            print('Proceeding to checkout...')
            cart.print_total()
            
        #if they do not chose from the menu response.     
        else:
            if choice != 'q':
                print('Invalid option. Please choose again.')   
    print('Thank you for shopping with us!')                
    
    
        
if __name__ == "__main__":
    #pull the basic info for the cart.
    customer_name = input('Enter the customer name: \n')
    current_date = get_valid_date() #ensures a valid date based on format at the top is input. 
    #create the cart object with the basic info.
    my_cart = ShoppingCart(customer_name, current_date)
    
    #call the menu to start the shopping process.
    print_menu(my_cart)
    