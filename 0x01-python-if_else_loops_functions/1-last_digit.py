#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# if number is negative:
# Converts negative to positive to get last digit
# Then coverted the last digit to negative

last_number = number
if number < 0:
    last_number = number * -1
    last_number = last_number % 10 * -1
else:
    last_number = last_number % 10

if last_number > 5:
    print('Last digit of', number, 'is', last_number, 'and is greater than 5')
elif last_number == 0:
    print('Last digit of', number, 'is', last_number, 'and is 0')
else:
    print('Last digit of', number, 'is', last_number, 'and is less than 6 '
          'and not 0')
