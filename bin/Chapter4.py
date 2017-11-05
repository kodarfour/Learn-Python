print("Chapter 4\n")

print("Part 4.1, Compare with if, elif, and else:\n")

smart = True
if smart:
	print("What a genius!")
else:
	print("Such a doofus!")

muscular = True
hairy = True
if muscular:
	if hairy:
	#this is if it is muscular AND hairy
		print('Found a bear.')
	else:
	#this is if its JUST muscular   
		print('That\'s a bodybuilder.')
else: 
	if hairy:
	#this is if its JUST hairy
		print('It\'s a hamster.')
	else:
	#this is if its NEITHER muscular OR hairy
		print('EWW! There is a naked mole-rat!')    

#elifs are used when there are more than two possibilities.
#they basically act as a shorter version of use else: if: therefore having the
#name elif 

#These are all of the comparison operators
# == 'equality'
# != 'inequality'
# < 'less than'
# <= 'less than or equal'
# > 'greater than
# >= 'greater than or equal'
# in 'membership'

beverage = 'butterbeer'
if beverage == 'orange juice': 
	print('Oh, it must be for breakfast.\n')
elif beverage == 'water':
	print('Great, you\'re staying hydrated.\n')
elif beverage == 'soda':
	print('Don\'t drink to much! It rots your teeth.\n')
elif beverage == 'hennesey':
	print('That is QUITE expensive mate.\n')
else:
	print('I\'ve never heard of this drink. It must be magical.\n')

print('\nPart 4.2, Repeat with while:\n')

count = 1
while count <= 9:
	#this means the while loop will end when 'count' is less than or equal to
	#9, becomes false
	print(count)
	count += 2
	# incremented the value by +2
print("Python Compiler: Finished!\n")

while True:
	rdm = input('Automatic String Capitalizer, Try It! (type q to quit): ')
	if rdm == 'q': #quit
		break
	print(rdm.capitalize())
	#capitalizes the first letter of what the user inputs

while True:
	value = input('\nGive me an odd integer and I\'ll surprise you (type q to '
				  'quit): ')
	if value == 'q':
	#quits the program
		break
	number = int(value)
	if number % 2 == 0:
	#if the number is even it wont square the number
		continue
		#skips the print statement if number is equal to 0
	print(number, "squared is", number*number) 

numbers = [2,3,5]
position = 0
while position < len(numbers):
#while position (0) is less than the number of items in the list "numbers"
	number = numbers[position]
	# this makes number = 1 since 1 is in the position of zero (position
	# has the value of zero)
	if number % 2 == 0:
	#if there is no remainder for number divided by 2 it prints what is below
		print('\nFound an even number!')
		break
else: #continues the while loop even after the break
	print('\nNo even number found.')

print("\nPart 4.3, Iteration with for:\n")

superheroes = ['Flash', 'Blue Beetle', 'Beast Boy', 'Ironman', 'Hulk']
for superhero in superheroes:
#prints every superhero in the list
	print(superhero)

print('')

word = 'pokemon'
for letter in word:
# prints every letter in the word pokemon
	print(letter)

print('')

# when doing an iteration over a dict it prints the keys

starters = { 
	'Rowlett' : 'Grass',
	'Litten' : 'Fire',
	'Popplio' : 'Water'
}

for pokemon in starters: # or starters.keys()
# prints every key in the dict
	print(pokemon)

print('')

for type in starters.values():
# prints every value in the dict
	print(type)

print('')

for pokemon in starters.items():
#prints both values and keys in the dict
	print(pokemon)

print('')

for name, type in starters.items():  
#each variable represent either key or value
#has to include .items for it to include values in the loop
	print('The pokemon', name, 'is a', type, 'pokemon.')

print('')

valuables = []

for valuable in valuables:
	print('This house is amazing it has ', valuable, ' !\n')
	break
else:	# if the loop doesnt break that means there is no valuables
	print('Wow these people are broke.\n')

day = ['Mondays', 'Tuesdays', 'Wednesdays']
snack = ['a popsicle', 'a cookie', 'an orange']
homework = ['Geometry', 'Biology', 'World History']
dinner = ['pizza', 'a hamburger', 'a beef pie', 'a hotdog']

for day, snack, homework, dinner in zip(day, snack, homework, dinner):
	print('On', day, 'I have', snack, 'for a snack. After my snack ' 
		  'I have to do my', homework,'homework. Finally, I eat', dinner,
		  'for dinner.\n')
#the zip function allows multiple iterations with for
#the 'a hotdog' string was skipped because the for loop stops if there are
#no more other strings to go along with it

english = ('Strength', 'Fire', 'Death')
dovazhul = ('Mulaag', 'Yol', 'Dinok')

print(list(zip(english,dovazhul)))
#it is possible to use the zip() function as a psuedo dict

print('')

for x in range(5, 0,-1):
	print(x)

print('')

print(list(range(5, 0, -1)))
# the range function works like slices (start, stop, step)
#in this example it will start at 5, stop at one (remember python starts
#at zero), and will go by steps of -1 (so basically subtracting one every step) 

print('\nPart 4.4, Comprehensions\n')

#it is possible to to list integers using the .append() function

nmbr_list = []
nmbr_list.append(1)
nmbr_list.append(2)
nmbr_list.append(3)
nmbr_list.append(4)
nmbr_list.append(5)
print(nmbr_list)

#it is also possible using an iterator and the range() function

print('')

nmbr_list = []
for number in range(1,6):
	nmbr_list.append(number)
print(nmbr_list)

#finally u could use the output of the range() function 

print('')

nmbr_list = list(range(1,6))
print(nmbr_list) 

#the best way is by a list comprehension