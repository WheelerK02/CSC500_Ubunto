# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

# imports from py library.
from datetime import date, datetime, timedelta 

#defining out change time from 12 hour to 24 hour clock.

def change_time(time):
    in_time = datetime.strptime(time, "%I%M %p %d-%B-%Y")
    return in_time

# Define out inputs from user. 

input_period = input("Is the time in AM or PM? ")
input_time = (input("What is the current time in hours and minutes?"))
input_wait_time = int(input("How many hours do you want to wait for the alarm? "))

# manipulate the inputs into useable formats.

AM_PM = input_period.upper()
today = date.today().strftime("%d-%B-%Y") #confirming todays date to track. 
clean_time = input_time.replace(":", "").replace(" ", "") #factoring for different inputs of time with or without a colon and space.
adjusted_time = clean_time.zfill(4) #forcing the input to be 4 digits taking into account inputs before 10 AM/PM
combined_time_period = (f'{adjusted_time} {AM_PM} {today}') #provides total input time, period and date for manipulation,



#using timedelta to account for anyting that exceeds 2359 on the 24 hour clock and track it in the future. 

start_point = change_time(combined_time_period) # defines the current time as the input adjusted into proper format for timedelta.
end_point = start_point + timedelta(hours=input_wait_time) # takes that change time as start point and add hours based on user input.
alarm_time = end_point.strftime("%H%M") # creates the time the alarm should go off in 24 hour clock format.
alarm_date = end_point.strftime("%d-%B-%Y") # creates the date the alarm will go off based on the start point and hours added.

# printing user inputs and what the output would be taking into account rollover of the 24 hour clock and the date.
    
print(f'Current time entered: {combined_time_period}') # user input with time and date
print(f'Requested time till alarm: {input_wait_time} hours') # time in hours of when the user wants the alarm to go off.
print(f'When the alarm goes off: {alarm_time} on {alarm_date}') # combined output of time and date using timedetla to wrap around the 24 hour clock. 





# Resources:
# https://realpython.com/python-time-module/#dealing-with-python-time-using-seconds, accessed 3 April 26, Section Dealing with Time in Seconds.
# https://www.youtube.com/watch?v=be0_CJ0YqoE, accessed 4 April 26, starting at 2:00 minutes       
# https://www.youtube.com/watch?v=bzX7gJdI8Dk, acccessed 4 April 25, entire video. 
# https://thepythoncodingbook.com/dates-and-times-in-python/, accessed 4 April 26, entire article.
# https://www.geeksforgeeks.org/python/python-string-zfill/, accessed 4 April 26, entire article.

                  