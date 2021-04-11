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

coffee_list = []
for student in students:
    if student['course'] == 'data science':
        coffee_preference = student['coffee_preference']
        coffee_list.append(coffee_preference)
blends = dict()
for drink in coffee_list:
    blends[drink] = coffee_list.count(drink)   
blends_pref = max(blends, key = blends.get)
print(f'The most frequent coffee preference for data science students is {blends_pref}.')

# 11. What is the least frequent coffee preference for web development students?

coffee_list = []
for student in students:
    if student['course'] == 'web development':
        coffee_preference = student['coffee_preference']
        coffee_list.append(coffee_preference)
blends = dict()
for drink in coffee_list:
    blends[drink] = coffee_list.count(drink)
least_choice = []
for key in blends:
    if blends[key] == min(coffee_list.values()):


# 12. What is the average grade for students with at least 2 pets?

grades_total = 0
number_grades = 0
for student in students:
    if len(student['pets']) > 1:
        grades_total += sum(student['grades'])
        number_grades += len(student['grades'])
print('The average grade for students with at least 2 pets is:', (grades_total / number_grades))

# 13. How many students have 3 pets?

more_than_3 = 0
for student in students:
    if len(student['pets']) > 3:
        more_than_3 += 1
print('The number of students that have more than 3 pets is:', more_than_3)

# 14. What is the average grade for students with 0 pets?

grades_total = 0
number_grades = 0
for student in students:
    if len(student['pets']) == 0:
        grades_total += sum(student['grades'])
        number_grades += len(student['grades'])
print('The average grade for students with no pets is:', (grades_total / number_grades))

# 15. What is the average grade for web development students? data science students?

grades_total = 0
number_grades = 0
for student in students:
    if student['course'] == 'web development':
        grades_total += sum(student['grades'])
        number_grades += len(student['grades'])
print('The average grade for web development students is:', (grades_total / number_grades))

grades_total = 0
number_grades = 0
for student in students:
    if student['course'] == 'data science':
        grades_total += sum(student['grades'])
        number_grades += len(student['grades'])
print('The average grade for data science students is:', (grades_total / number_grades))

# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark 
# coffee drinkers?

average_grades = []
for student in students:
    if student['coffee_preference'] == 'dark':
        average_grades.append(sum(student['grades']) / len(student['grades']))
    
print('The highest average grade for dark coffee drinkers is:', max(average_grades))
print('The lowest average grade for dark coffee drinkers is:', min(average_grades))

# 17. What is the average number of pets for medium coffee drinkers?

medium_drinkers = 0
number_pets = 0
for student in students:
    if student['coffee_preference'] == 'medium':
        medium_drinkers += 1
        number_pets += len(student['pets'])
print('The average number of pets for medium coffee drinkers is:', (number_pets / medium_drinkers))

# 18. What is the most common type of pet for web development students?

pet_list = []
for student in students:
    if student['course'] == 'web development':
        pets = student['pets']
        for species in pets:
            pet_species = species['species']
            pet_list.append(pet_species)
pets = dict()
for animal in pet_list:
    pets[animal] = pet_list.count(animal)
pet_pref = max(pets, key = pets.get)
print(f'The most common type of pet for web development students is {pet_pref}.')

# 19. What is the average name length?

sum_length = 0
num_students = 0
for student in students:
    num_students += 1
    sum_length += len(student['student'].replace(' ', ''))
print('The average name length is:', (sum_length / num_students))

# 20. What is the highest pet age for light coffee drinkers?

