# Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax.  Display each of these amounts and the total price.

# variables and constants

tax_percent = .07
tip_percent = .18

# input from customer
bill_amount = float(input('Enter the amount of your bill in dollars and cents: $'))

# calculations
tax_amount = float(bill_amount * tax_percent)
tip_amount = float(bill_amount * tip_percent)
total_bill = float(bill_amount + tax_amount + tip_amount)

# printing all the results 
# Using the formate method to keep it all to 2 decimal places.
print(f'Bill before taxes and tip: $ {bill_amount:.2f}')
print(f'Taxes: $ {tax_amount:.2f}')
print(f'Tip: $ {tip_amount:.2f}')
print(f'Total bill: ${total_bill:.2f}')

#Resources:
# https://www.youtube.com/watch?v=8GIqXqHDNfY, Ryan and Matt Data Science, starting at 8:17 nmiunutes, 
# https://www.youtube.com/watch?v=FrvBwdAU2dQ, Bro Code, starting at 1.35 minutes to 2:40 minutes.

