# I am continuing off the original discussion post for #1 taking into account the cookie algorithm. 
# I would go back to that algorithm and insert a B counter for number of batches each time we meet. 
# Considering we meet at my house once a month this makes this a straight forward deal. 

import array # Resource 1

cookie_batches = array.array('f') 


for month in range(1, 13): # Resource 2
    cookie_batches.append(float(input("Enter the number of cookie batches for month {month}: "))) # Resource 3.
# I would continue this for each month. 
# Using a for statement as we learned in loops this week with 

# Next I would want to track the max value, min and sum of batches over the year.

total_batches = sum(cookie_batches)
max_batches = max(cookie_batches)
min_batches = min(cookie_batches)

# Finally we could print them out. 

print("Total cookie batches for the year: ", total_batches)
print("Maximum cookie batches in a month: ", max_batches)
print("Minimum cookie batches in a month: ", min_batches)

# Resources
# Resource 1: https://www.youtube.com/watch?v=6a39OjkCN5I, Telusko YouTube channel, 2:20 into video. 
# Resource 2: Python Crash Course, Eric Matthes, Chapter 4, page 57-60.
# Python Crash Course, Eric Matthes, Chapter 3, page 37-38.


# It would be easier to do this would be just using a list instead of an array, but I wanted to try out arrays for this discussion.
# Using a list would be set up the following way: cookie_batches = [] to create an empty list for each year. 
# I could create a user input to ask for the number of batches each month and store them in that list. 
# Finally I would do the same total, max and min calculations to know how much or little supplies to have on hand.
# I am missing the break portion to have at the end of each month to stop the append and show the total, max and min for the year.