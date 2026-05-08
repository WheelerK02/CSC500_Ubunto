
#imports from Milestone One and Two to keep this modular and organized.
from Milestone_One_Final_Project import ItemsToPurchase
from Milestone_Two_Final_Project import ShoppingCart, get_valid_date, print_menu

def main():
    #get the name of the customer for the cart. 
    customer_name = input("Enter customer's name: ")
    
    #get the date from the user and make sure it's in the right format. 
    current_date = get_valid_date()
    
    #create a new shopping cart for the customer with the current date. 
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)
    
    
if __name__ == "__main__":
    main()
        