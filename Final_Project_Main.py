'''here to pull everything together for one code to run the whole project 
using modualar approach.'''

from Milestone_One_Final_Project import ItemsToPurchase
from Milestone_Two_Final_Project import ShoppingCart, print_menu, get_valid_date

def main():
    print('Welcome to the shopping cart program!')
    customer_name = input('Enter customer\'s name: ')
    current_date = get_valid_date()
    
    my_cart =ShoppingCart(customer_name, current_date)
    
    print_menu(my_cart)
    
if __name__ == "__main__":
    main()
    
