#trying this out.

rooms_dict = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

instructor_dict = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}   

meeting_time_dict = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}
user_input = ""
while user_input != 'exit':
    user_input = input("Enter a course code: ")
    user_input = user_input.upper().replace(" ", "")
    if user_input in rooms_dict:
        print()
        print(f"Course: {user_input}" )
        print(f"Room number: {rooms_dict[user_input]}")
        print(f"Instructor: {instructor_dict[user_input]}")
        print(f"Meeting time: {meeting_time_dict[user_input]}")
    elif user_input == 'EXIT':
        print("Exiting the program.")
        break
    else:
        print("Invalid course code. Please try again.")


'''Resources:
https://learn.zybooks.com/zybook/CSC500-1_17/chapter/6/section/14, accessed 3 May 2024.
https://www.w3schools.com/python/python_dictionaries.asp, accessed 3 May 2024.

'''