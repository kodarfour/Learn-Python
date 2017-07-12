print("Chapter 4: \n")

print("Compare with if, elif and else:\n")

smart = True
if smart:
	print("What a genius!")
else:
	print("Such a doofus!")

muscular = True
hairy = True
if muscular:
	if hairy:
		print('Found a bear.')
	else:
		print('That\'s a bodybuilder.')
else: 
	if hairy:
		print('It\'s a hamster.')
	else:
		print('EWW! There is a naked mole-rat!')	

print('\nRepeat with while:\n')


count = 1
while count <= 9:
	#this means the while loop will end when 'count' is less than or equal to
	#9, becomes false
	print(count)
	count += 2
	# incremented the value by +2
print("Python Compiler: Finished!")

while True:
	rdm = input("Automatic String Capitalizer, Try It! (type q to quit): ")
	if rdm == "q": #quit
		break
	print(rdm.capitalize())
