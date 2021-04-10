# 20 Python Data Structure Manipulation Exercises
# The following questions reference the students data structure below. 
# Write the python code to answer the following questions:

# 1. How many students are there?

len(students)

# 2. How many students prefer light coffee? For each type of coffee roast?

light_count = 0
for student in students:
    if student['coffee_preference'] == 'light':
        light_count += 1
print(light_count)

light_count = 0
medium_count = 0
dark_count = 0
for student in students:
    if student['coffee_preference'] == 'light':
        light_count += 1
    elif student['coffee_preference'] == 'medium':
        medium_count += 1
    elif student['coffee_preference'] == 'dark':
        dark_count += 1
print(f'light = {light_count}')
print(f'medium = {medium_count}')
print(f'dark = {dark_count}')

# 3. How many types of each pet are there?

horses = []
dogs = []
cats = []
for student in students:
    pets = student['pets']
    for species in pets:
        pet_species = species['species'] 
        if pet_species == 'horse':
            horses.append(pet_species)
        elif pet_species == 'dog':
            dogs.append(pet_species)
        elif pet_species == 'cat':
            cats.append(pet_species)
print(f'horses = {len(horses)}')
print(f'dogs = {len(dogs)}')
print(f'cats = {len(cats)}')

# 4. How many grades does each student have? Do they all have the same number of grades?

for student in students:
    print(student['student'], 'has ', len(student['grades']), 'grades.')
print('\nAll students have', len(student['grades']), 'grades.')

# 5. What is each student's grade average?

for student in students:
    print(student['student'], "'s grade average is", sum(student['grades']) / len(student['grades']))

# 6. How many pets does each student have?

for student in students:
    print(student['student'], 'has', len(student['pets']), 'pets.')

# 7. How many students are in web development? data science?

web = 0
data = 0
for student in students:
    if student['course'] == 'web development':
        web +=1
    elif student['course'] == 'data science':
        data += 1
print(f'Web Development has {web} students.')
print(f'Data Science has {data} students.')

# 8. What is the average number of pets for students in web development?

web = 0
pets = 0
for student in students:
    if student['course'] == 'web development':
        web += 1
        pets += len(student['pets'])
print('Web Development students have an average of ', (pets / web), ' pets.')

# 9. What is the average pet age for students in data science?

total_age = 0
number_pets = 0
for student in students:
    if student['course'] == 'data science':
        pets = student['pets']
        for pet in pets:
            total_age += pet['age']
            number_pets += 1
average_age = (total_age / number_pets)            
print(f'The average pet age for students in Data Science is {average_age}.')

# 10. What is most frequent coffee preference for data science students?
# 11. What is the least frequent coffee preference for web development students?
# 12. What is the average grade for students with at least 2 pets?
# 13. How many students have 3 pets?
# 14. What is the average grade for students with 0 pets?
# 15. What is the average grade for web development students? data science students?
# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?

