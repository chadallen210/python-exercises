# Imports Exercises

# 1. Import and test 3 of the functions from your functions exercise file. 
# Import each function in a different way:

# a. Run an interactive python session and import the module. Call the is_vowel 
# function using the . syntax.

import function_exercises

function_exercises.is_vowel('a')

# b. Create a file named import_exericses.py. Within this file, use from to import 
# the calculate_tip function directly. Call this function with values you choose 
# and print the result.

from function_exercises import calculate_tip

print(calculate_tip(0.2, 100))

# c. Create a jupyter notebook named import_exercises.ipynb. Use from to import 
# the get_letter_grade function and give it an alias. Test this function in your 
# notebook.

from function_exercises import get_letter_grade as grade

print(grade(87))

# 2. Read about and use the itertools module from the python standard library to 
# help you solve the following problems:

# - How many different ways can you combine the letters from "abc" with the 
# numbers 1, 2, and 3?

import itertools

products = len(list(itertools.product('abc', '123')))
products

# - How many different combinations are there of 2 letters from "abcd"?

combos = len(list(itertools.combinations('abcd', 2)))
combos

# - How many different permutations are there of 2 letters from "abcd"?

perms = len(list(itertools.permutations('abcd', 2)))
perms

# 3. Save this file as profiles.json inside of your exercises directory 
# (right click -> save file as...).
# Use the load function from the json module to open this file.
# Your code should produce a list of dictionaries. Using this data, 
# write some code that calculates and outputs the following information:

import json
profiles = json.load(open('profiles.json'))

# - Total number of users

len(profiles)

# - Number of active users

count = 0
for profile in profiles:
    if profile['isActive'] == True:
        count += 1
count

# - Number of inactive users

count = 0
for profile in profiles:
    if profile['isActive'] == False:
        count += 1
count

# - Grand total of balances for all users

grand_total = 0
for profile in profiles:
    balance = float(profile['balance'].replace(',', '').replace('$', ''))
    grand_total += balance
grand_total

# - Average balance per user

grand_total = 0
for profile in profiles:
    balance = float(profile['balance'].replace('$', '').replace(',', ''))
    grand_total += balance
    average_balance = (grand_total / len(profiles))
round(average_balance, 2)

# - User with the lowest balance

lowest_balance = float('inf')
min_user = {}

for profile in profiles:
    balance = float(profile['balance'].replace('$', '').replace(',', ''))
    if balance < lowest_balance:
        lowest_balance = balance
        min_user = profile
        
min_user

# - User with the highest balance

highest_balance = 0
max_user = {}

for profile in profiles:
    balance = float(profile['balance'].replace('$', '').replace(',', ''))
    if balance > highest_balance:
        highest_balance = balance
        max_user = profile

max_user

# - Most common favorite fruit

fruit_list = [accnt['favoriteFruit'] for accnt in profiles]

fruit_counts = {}

for fruit in fruit_list:
    if fruit not in fruit_counts.keys():
        fruit_counts[fruit] = 1
    else:
        fruit_counts[fruit] += 1

for k, v in fruit_counts.items():
    if v == max(fruit_counts.values()):
        print(k)

# - Least most common favorite fruit

for k, v in fruit_counts.items():
    if v == min(fruit_counts.values()):
        print(k)

# - Total number of unread messages for all users

sum([int(''.join([val for val in accnt['greeting'] if val.isdigit()])) for accnt in profiles])