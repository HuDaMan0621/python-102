#Given the following code that prompts the user for a day number
#int function converts a numeric string to a number
day = int(input('please enter Day (0-6)?'))
day = int(day)
if day <= 0 and int(day) >= 6:
    print('Please Enter 0-6')
elif int(day) == 0:
    print('Sunday')
elif int(day) == 1:
    print('Monday')
elif int(day) == 2:
    print('Tuesday')
elif int(day) == 3:
    print('Wednesday')
elif int(day) == 4:
    print('Thursday')
elif int(day) == 5:
    print('Friday')
elif int(day) == 6:
    print('Saturday')
else:
    print('Please Enter 0-6')