'''
Assignment: Build a function that creates three dictionaries and prints
the values associated with the key provided by the user.
'''

def main():
    course_number = ''
    # Create room number, instructor, and time dictionaries
    # Coming from a SQL background this is physically painful to write
    room_number = {'ISQS 5347': 'BA 289', 'ISQS 6337': 'BA 015','ISQS 6349': 'BA 287','ISQS 6348': 'BA 021'}
    instructor = {'ISQS 5347': 'Zadeh', 'ISQS 6337': 'Song','ISQS 6349': 'Kim', 'ISQS 6348': 'Benjamin'}
    time = {'ISQS 5347': '8:00 a.m.', 'ISQS 6337': '2:00 p.m.','ISQS 6349': '9:00 a.m.', 'ISQS 6348': '2:00 p.m.'}

    # Get course from user
    course_number = input('Enter a course number: ')

    # Validate course number and print info if correct
    if course_number in room_number:
        print('The details for course ' + course_number + ' are: ')
        # Print values for course_number in all dictionaries
        print('Room: ', room_number[course_number])
        print('Instructor: ', instructor[course_number])
        print('Time: ', time[course_number])
    else:
        print('Enter a valid course number.')
main()