# Function Exercises

# 1. Define a function named is_two. It should accept one input and return True 
# if the passed input is either the number or the string 2, False otherwise.

def is_two(number):
    if number == 2 or number == '2':
        return True
    return False
    
is_two(2)
is_two(4)

# 2. Define a function named is_vowel. It should return True if the passed 
# string is a vowel, False otherwise.

def is_vowel(letter):
    if letter.isalpha() and letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False

is_vowel('a')
is_vowel('b')

# 3. Define a function named is_consonant. It should return True if the passed 
# string is a consonant, False otherwise. Use your is_vowel function to accomplish 
# this.

def is_consonant(letter):
    if letter.isalpha() and letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False

is_consonant('b')
is_consonant('a')

# 4. Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.

vowels = ['a','e','i','o','u']
def cap_it(word):
    word = word.lower()
    if word.startswith(tuple(vowels)):
        return word
    else:
        return word.capitalize()
    
cap_it('tree')
cap_it('apple')

# 5. Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip, bill):
    tip_amount = round(float(bill) * float(tip), 2)
    return tip_amount

calculate_tip(0.2, 15.93)

# 6. Define a function named apply_discount. It should accept an original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, discount):
    price = float(price)
    discount = float(discount / 100)
    discounted_price = round(price - round((price * discount), 2), 2)
    return discounted_price

apply_discount(50, 10)

# 7. Define a function named handle_commas. It should accept a string that is 
# a number that contains commas in it as input, and return a number as output.

def handle_commas(value):
    new_value = int(value.replace(',', ''))
    return new_value

handle_commas('1,000,000')

# 8. Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

def get_letter_grade(number):
    if number >= 90:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 70:
        return 'C'
    elif number >= 60:
        return 'D'
    else:
        return 'F'

get_letter_grade(75)

# 9. Define a function named remove_vowels that accepts a string and returns a 
# string with all the vowels removed.

def remove_vowels(value):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for character in vowels:
        value = value.replace(character, '')
    return value

remove_vowels('tree')

# 10. Define a function named normalize_name. It should accept a string and return 
# a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores

letters = []
for letter in word:
    if letter.isalnum() or letter == ' ':
        letters.append(letter)
        
# 11. Write a function named cumulative_sum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

