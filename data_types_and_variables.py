# Data Types, Operators, and Variables
# Exercises

# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and 
# Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

little_mermaid = 3
brother_bear = 5
hercules = 1

rental_fee = 3

total_fees = (little_mermaid * rental_fee) + (brother_bear * rental_fee) + (hercules * rental_fee)

print (f'Total rental fees are {total_fees}.')

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, and they pay 
# you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350

g_hours = 6
a_hours = 4
f_hours = 10

earnings = (google * g_hours) + (amazon * a_hours) + (facebook * f_hours)

print (f'Total earnings are {earnings}.')

# A student can be enrolled to a class only if the class is not full and the class 
# schedule does not conflict with her current schedule.

class_not_full = True or False
no_conflict = True or False

if class_not_full and no_conflict:
    print ('You CAN enroll in this class.')
else:
    print ('You CAN NOT enroll in this class.')

# A product offer can be applied only if people buys more than 2 items, and the offer has 
# not expired. Premium members do not need to buy a specific amount of products.

premium_member = True or False
offer_valid = True or False

if premium_member and offer_valid:
    total_cost = (product_cost * discount) * item_count
elif offer_valid and item_count >= 2:
    total_cost = (product_cost * discount) * item_count
else:
    total_cost = product_cost * item_count

print (total_cost)

# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# the password must be at least 5 characters

is_greater_than_5 = len(username) > 5

print (is_greater_than_5)

# the username must be no more than 20 characters

no_more_than_20 = len(password) <= 20

print (no_more_than_20)

# the password must not be the same as the username

not_same = password == username

print (not_same)

# bonus neither the username or password can start or end with whitespace

spaces = not (username.startswith(' ') or username.endswith(' ') or password.startswith(' ') 
or password.endswith(' '))

print (spaces)
