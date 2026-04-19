num_years = int(input("Enter the number of years: "))

running_tot = 0
for year in range(num_years):
    for month in range(1, 13):
        rain_mon_inches = float(input(f"Enter the rainfall for the month of {month} in inches: "))
        while rain_mon_inches < 0:
            print("Invalid input. Please enter a non-negative value.")
            rain_mon_inches = float(input(f"Enter the rainfall for the month of {month} in inches: "))
        running_tot += rain_mon_inches
           

total_months = num_years * 12
total_rainfall = running_tot
avg_rainfall = total_rainfall / total_months

print(f'Total months: {total_months}')
print(f'Total rainfall: {total_rainfall:.2f} inches')
print(f'Average monthly rainfall: {avg_rainfall:.2f} inches')

    