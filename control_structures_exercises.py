# Control Structures
# Exercises

# 1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not

print('Please enter a day of the week: ')
day = input()

if day.lower() == 'monday':
    print(f'Your day is {day}!')
else:
    print('Not Monday.')

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

print('Please enter a day of the week: ')
day = input()

if day.lower() in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
    print('Your day is a weekday.')
elif day.lower() in ('saturday', 'sunday'):
    print('Your day is a weekend day!')
else:
    print('That is not a day at all!')

# c. create variables and make up values for
# - the number of hours worked in one week

hours_worked = 35

# - the hourly rate

hourly_rate = 400

# - how much the week's paycheck will be

this_weeks_pay = hours_worked * hourly_rate

# write the python code that calculates the weekly paycheck. You get paid time 
# and a half if you work more than 40 hours

if hours_worked <= 40:
    this_weeks_pay = hours_worked * hourly_rate
else:
    this_weeks_pay = (hourly_rate * 40) + (hourly_rate * 1.5 * (hours_worked - 40))
print(this_weeks_pay)

# 2. Loop Basics
# a. While
# - Create an integer variable i with a value of 5.

i = 5

# - Create a while loop that runs so long as i is less than or equal to 15

while i <= 15

# - Each loop iteration, output the current value of i, then increment i by one.

while i <= 15:
    print(i)
    i += 1

# - Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

i = 0

while i <= 98:
    print(i, '\n')
    i = i + 2

# - Alter your loop to count backwards by 5's from 100 to -10.

i = 100

while i >= -10:
    print(i, '\n')
    i = i -5
    
# - Create a while loop that starts at 2, and displays the number 
# squared on each line while the number is less than 1,000,000.

i = 2
while i < 1000000:
    print(i)
    i **= 2

# - Write a loop that uses print to create the output shown below.

i = 100

while i >= 5:
    print(i)
    i -= 5

# b. For Loops
# i. Write some code that prompts the user for a number, then shows 
# a multiplication table up through 10 for that number.

print('Please input a number: ')
number = int(input())
for n in range(1, 11):
    print(number, 'X', n, '=', number * n)

# ii. Create a for loop that uses print to create the output shown below.

for i in range (1, 10):
    print(str(i) * i)

# c.  break and continue
# i. Prompt the user for an odd number between 1 and 50. Use a loop and 
# a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and 
# the continue statement to output all the odd numbers between 1 and 50, except 
# for the number the user entered.

while True:
    number = input('Please input an odd integer between 1 and 50: ')
    if number.isdigit():
        number = int(number)
        if (number > 1 and number < 50) and number % 2 == 1:
            print(f'Number to skip is: {number}')
            break
for n in range(1, 50):
    if n == number:
        print(f'Yikes! Skipping number: {number}')
    if n % 2 == 1 and n != number:
        print(f'Here is an odd number: {n}')
    continue

# d. The input function can be used to prompt for input and use that input in 
# your python code. Prompt the user to enter a positive number and write a loop 
# that counts from 0 to that number. (Hints: first make sure that the value the 
# user entered is a valid number, also note that the input function returns a 
# string, so you'll need to convert this to a numeric type.)

while True:
    number = input('Please input a positive number: ')
    if number.isdigit():
        number = int(number)
        if number > 0:
            break
for n in range(number + 1):
    print(n)

# e. Write a program that prompts the user for a positive integer. Next write a 
# loop that prints out the numbers from the number the user entered down to 1.

while True:
    number = input('Please input a positive integer: ')
    if number.isdigit():
        number = int(number)
        if number > 0:
            break
while number > 0:
    print(number)
    number -= 1

# 3. Fizzbuzz
# One of the most common interview questions for entry-level programmers is 
# the FizzBuzz test. Developed by Imran Ghory, the test is designed to test 
# basic looping and conditional logic skills.
# - Write a program that prints the numbers from 1 to 100.
# - For multiples of three print "Fizz" instead of the number
# - For the multiples of five print "Buzz".
# - For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 20):
    if n % 5 == 0 and n % 3 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)

# 4. Display a table of powers.
# - Prompt the user to enter an integer.
# - Display a table of squares and cubes from 1 to the value entered.
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.

while True:
    number = input('What number would you like to go up to? ')
    if number.isdigit():
        number = int(number)
        if number > 0:
            break
print('Here is your table!')
print('number | squared | cubed')
print('------ | ------- | -----')
for n in range(1, number + 1):
    print(n, n ** 2, n ** 3)

# 5. Convert given number grades into letter grades.
# - Prompt the user for a numerical grade from 0 to 100.
# - Display the corresponding letter grade.
# - Prompt the user to continue.
# - Assume that the user will enter valid integers for the grades.
# - The application should only continue if the user agrees to.
# - Grade Ranges:
# -- A : 100 - 88
# -- B : 87 - 80
# -- C : 79 - 67
# -- D : 66 - 60
# -- F : 59 - 0
# --- Bonus
# --- Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

while True:
    number = input('Please enter a numerical grade from 0 to 100: ')
    if number.isdigit():
        number = int(number)
        if number >= 0 and number <= 100:
            break
if number >= 88:
    print('Your grade is an A!')
elif number in range(80, 88):
    print('Your grade is a B.')
elif number in range(67, 80):
    print('Your grade is a C.')
elif number in range(60, 67):
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

