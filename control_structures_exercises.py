# Control Structures
# Exercises

# 1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not

print('Please enter a day of the week: ')
day = input()

if day.lower() == 'monday':
    print(f'Your day is {day}!')
elif day.lower() in ('tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
    print(f'Your day is {day}, but not Monday.')
else:
    print('That is not a day at all!')

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

amazon_rate = 400

# - how much the week's paycheck will be

this_weeks_pay = hours_worked * amazon_rate

# write the python code that calculates the weekly paycheck. You get paid time 
# and a half if you work more than 40 hours

if hours_worked <= 40:
    this_weeks_pay = hours_worked * amazon_rate
else:
    this_weeks_pay = (amazon_rate * 40) + (amazon_rate * 1.5 * (hours_worked - 40))
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
print(i, '\n')

while i <= 98:
    i = i + 2
    print(i, '\n')

# - Alter your loop to count backwards by 5's from 100 to -10.

i = 100
print(i, '\n')

while i >= -5:
    i = i -5
    print(i, '\n')

# - Create a while loop that starts at 2, and displays the number 
# squared on each line while the number is less than 1,000,000.

i = 2
while i <= 1000000:
    print(i)
    i *= i

# - Write a loop that uses print to create the output shown below.

i = 100
print(i)
while i >= 10:
    i -= 5
    print(i)

# b. For Loops
# i. Write some code that prompts the user for a number, then shows 
# a multiplication table up through 10 for that number.

print('Please input a number: ')
number = int(input())
for i in range(1, 11):
    print(number, 'X', i, '=', number * i)

# ii. Create a for loop that uses print to create the output shown below.

for i in range (1, 10):
    print(str(i) * i)

# c.  break and continue
# i. Prompt the user for an odd number between 1 and 50. Use a loop and 
# a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and 
# the continue statement to output all the odd numbers between 1 and 50, except 
# for the number the user entered.

