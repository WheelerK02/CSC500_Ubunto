'''The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. 
The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month 
and then display the number of points awarded.'''




#while statement to handle invalid input of neg numbers. Does not deal with 
while True:
    books_purchased = int(input("Enter the number of books purchased this month: ")) #user input for number of books purchased
    if books_purchased >= 0:
        break
    else:
        print("Invalid input. Please enter a non-negative value.")
        
        
#create if based on input for points awarded
if books_purchased >= 8:
    points_awarded = 60 
elif books_purchased >= 6:
    points_awarded = 30
elif books_purchased >= 4:
    points_awarded = 15
elif books_purchased >= 2:
    points_awarded = 5
else:
    points_awarded = 0

print(f"Points awarded: {points_awarded}")

'''https://pythonguides.com/python-check-if-the-variable-is-an-integer/, accessed 6/10/2024, 
used to help with error handling for non-integer input.'''