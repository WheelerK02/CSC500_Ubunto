'''Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of rainfall, 
and the average rainfall per month for the entire period.'''

#user input for number of years
num_years = int(input("Enter the number of years: "))

#initialize running total for rainfall
running_tot = 0

#first loop creating a range in number of years, this tells outer loop how many time to run. 
for year in range(num_years):
    #This is the inner loop for the months. I chose (1, 13) so the months would line up 1 - 12 instead of 0 - 11.
    for month in range(1, 13):
        rain_mon_inches = float(input(f"Enter the rainfall for the month of {month} in inches: ")) #input for rainfall for each month
        #Does not allow input of neagative numbers
        while rain_mon_inches < 0:
            print("Invalid input. Please enter a non-negative value.")
            rain_mon_inches = float(input(f"Enter the rainfall for the month of {month} in inches: "))
        running_tot += rain_mon_inches
           
#basic math for tracking
total_months = num_years * 12
total_rainfall = running_tot
avg_rainfall = total_rainfall / total_months
#display out results and format to 2 decimal places for rainfall
print(f'Total months: {total_months}')
print(f'Total rainfall: {total_rainfall:.2f} inches')
print(f'Average monthly rainfall: {avg_rainfall:.2f} inches')

    