# Declare speed and time as user-input variables
speed = float(input('Enter the speed of the vehicle in mph: '))
time = int(input('Enter the number of hours traveled: '))

print("Hours\tDistance Traveled")
print('--------------------------------')

# Loop over time from 1 to ending time given by user
for time in range(1,time+1):
    # Declare distance as the product of speed and time and print
    distance = speed * time 
    print(time,'\t',distance)