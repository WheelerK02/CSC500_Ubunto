
#This is the class or my workshop where I create things for the market and store the things I find.
class ItemsToPurchase:
    
    item_count = 0
    
    def __init__(self, item_name='none', item_price=0, item_quantity=0):#Constructor with default values for attributes
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_cost = item_price * item_quantity
        ItemsToPurchase.item_count += 1
        
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}')
        
    
#This is the market where everything happens, main fuction.
#Blocking off to use Streamlit for the user interface, but this is the original code for the market.
if __name__ == "__main__":      
    # Capture user input for the attributes. This is a very rigid and not scalable way. I know for the future of this project we will have to loop this and I expect a WHILE loop. 
    print('Item 1')
    name_one = input('Enter the item name: ')
    price_one = int(input('Enter the item price: '))
    quantity_one = int(input('Enter the item quantity: '))   

    print('Item 2')
    name_two = input('Enter the item name: ')
    price_two = int(input('Enter the item price: '))
    quantity_two = int(input('Enter the item quantity: '))
        

    # Initlize the 2 required items for MS1 based on the class above.
            
    item1 = ItemsToPurchase(name_one, price_one, quantity_one)
    item2 = ItemsToPurchase(name_two, price_two, quantity_two)

    #Determine total cost of each item. Very linear action not scalable.  
    item1_total_cost = item1.item_price * item1.item_quantity
    item2_total_cost = item2.item_price * item2.item_quantity
    total_cost = item1_total_cost + item2_total_cost

    #Set up output from input and based on the class above. This is very rigid and not scalable. 
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print(f'Total: ${total_cost}')



"""Resourses:
https://www.youtube.com/watch?v=ZDa-Z5JzLYM, Corey Schafer, Python Object _Oriented Programming Tutorial 1: Classes and Instances, accessed 10 April 2026
https://www.youtube.com/watch?v=BJ-VvGyQxho, Corey Schafer, Python Object _Oriented Programming Tutorial 2: Class Variables, accessed 10 April 2026
https://www.youtube.com/watch?v=rq8cL2XMM5M, Corey Schafer, Python Object _Oriented Programming Tutorial 3: Class Methods and Static Methods, accessed 10 April 2026
https://www.geeksforgeeks.org/python/using-a-class-with-input-in-python/, Geeks for Geeks, Using a Class with Input in Python, accessed 10 April 2026
https://www.w3schools.com/python/python_oop.asp, W3 Schools, Python Object Oriented Programming, accessed 10 April 2026
https://stackoverflow.com/questions/40880474/class-and-objects-in-python, Class and objects in Python, Stack Overflow, accessed 10 April 2026

"""
