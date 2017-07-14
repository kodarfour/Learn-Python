print("Chapter 4: \n")

print("Part 4.1:\n")

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
#name elif (this is put into my terms of understanding)

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

print('\nPart 4.2:\n')

count = 1
while count <= 9:
	#this means the while loop will end when 'count' is less than or equal to
	#9, becomes false
	print(count)
	count += 2
	# incremented the value by +2
print("Python Compiler: Finished!\n")

while True:
	rdm = input("Automatic String Capitalizer, Try It! (type q to quit): ")
	if rdm == "q": #quit
		break
	print(rdm.capitalize())
	#capitalizes the first letter of what the user inputs
