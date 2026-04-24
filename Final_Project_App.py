import streamlit as st
from Milestone_One_Final_Project import ItemsToPurchase

st.header('Item 1')
name_one = st.text_input('Enter the item name: ', key='i1')
price_one = st.number_input('Enter the item price: ', min_value=0, key='p1')
quantity_one = st.number_input('Enter the item quantity: ', min_value=0, key='q1')
st.header('Item 2')
name_two = st.text_input('Enter the item name: ', key='i2')
price_two = st.number_input('Enter the item price: ', min_value=0, key='p2')
quantity_two = st.number_input('Enter the item quantity: ', min_value=0, key='q2')
#total it up baddie

if st.button('Calculate Total'): #gatekeep the total calculation until the user clicks the button
# Create the objects using the class you imported
    item1 = ItemsToPurchase(name_one, price_one, quantity_one)
    item2 = ItemsToPurchase(name_two, price_two, quantity_two)

# Calculate the total
    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    
    #final output. 
    st.write('TOTAL COST')
    # Instead of item1.print_item_cost()
    st.write(f"{item1.item_name} {item1.item_quantity} @ ${item1.item_price} = ${item1.item_cost}")
    st.write(f"{item2.item_name} {item2.item_quantity} @ ${item2.item_price} = ${item2.item_cost}")
    st.write(f'Total: ${total_cost}')

