# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

# imports from py library.
from datetime import date, datetime, timedelta 


# Define out inputs from user. 
input_period = input("Is the time in AM or PM? ")
input_time = (input("What is the current time in hours and minutes?"))
input_wait_time = int(input("How many hours do you want to wait for the alarm? "))
AM_PM = input_period.upper()
today = date.today().strftime("%d-%B-%Y")
hours = int(input_time[:-2])
minutes = int(input_time[-2:])
combined_time_period = (f'{hours}:{minutes} {AM_PM} {today}')
delta = timedelta(days=0)


# work out the time converstion of the input. a
if ":" not in input_time:
    input_time = input_time[:-2] + ":" + input_time[-2:]
 
if AM_PM == "AM":
    if hours == 12:
        hours = 00
                 
elif AM_PM == "PM":
    if hours != 12:
       hours += 12
             
return_time = (int(hours) + input_wait_time) % 24

alarm_time = (f'{return_time:02d}{minutes:02d}')

print(f'Current time entered: {combined_time_period}')
print(f'Requested wait time: {input_wait_time} hours')
print(f'Time when alarm goes off: {alarm_time}') 




# Resources:
# https://realpython.com/python-time-module/#dealing-with-python-time-using-seconds, accessed 3 April 26, Section Dealing with Time in Seconds.
# https://www.youtube.com/watch?v=be0_CJ0YqoE, accessed 4 April 26, starting at 2:00 minutes                         