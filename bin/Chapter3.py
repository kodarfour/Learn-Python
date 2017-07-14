print('Chapter 3:')

#lists quick review
#in a slice it is in the [first:last:step]
#the .append() function adds an item to the end of the list


print('Part 3.4:\n')

programmers = ['Kofi','Danielle','Bill']
languages = ['Python','JavaScript','C#']
employers = ['Google','Amazon','Micro$oft']

tuple_of_lists = (programmers,languages,employers)
#tuples dont have to have a parenthesis around them but it makes it easier to see
list_of_lists = [programmers,languages,employers]
dict_of_lists = {'Programmers' : programmers, 'Languages' : languages,
'Employers' : employers}

print(str(tuple_of_lists) + '\n')
print(str(list_of_lists) + '\n')
print(str(dict_of_lists) + '\n') 

print('Things To Do:')

years_list =  [2003,2004,2005,2006,2007,2008]

third_bday = years_list[3]
print('My third birthday was:')
print(str(third_bday) + '\n')

oldest_year = years_list[-1]
print('The oldest year in the list is:')
print(str(oldest_year) + '\n')

things = ['pizza','alexis','ebola']

things[1] = things[1].capitalize()
print(things)

things[0] = things[0].upper()
print(things)

del things[0]
print(things)

surprise = ["Groucho","Chico","Harpo"]
print('\n' + str(surprise))

surprise[0] = surprise[0].lower()
print(surprise)

surprise = surprise[::-1]
# if you think about it, it starts at -1, then goes to -2, then -3.
#the result is a reversed list
surprise[-1] = surprise[-1].capitalize()
print(surprise)

e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
print('\n' + str(e2f))
print(e2f['walrus'])

f2e = {'chien' : 'dog', 'chat' : 'cat', 'morse' : 'walrus'}
print(f2e)
print(f2e['chien'])

print(list(e2f.keys()))

life = {
	'animals' : 
	{ #made the bracket indented for readability
		'cats' : ['Henry,','Grumpy','Lucy'],
		'octopi' : {},
		'emus' : {}
	},
	'plants' : {},
	'other' : {}
}

print('\n' + str(life))
print(list(life.keys()))
print(list(life['animals'].keys()))
print(list(life['animals'[:]].values()))