fruits = ['Apples', 'Pears', 'Oranges', 'Peaches'] #creates list of fruits 
	print fruits

fruits.append('new') #input new fruit name
	print fruits

fruits[n] #input number from 1 to 5
	print n 
	print fruits[n]

fruits = ['second new'] + fruits #input a second new fruit name
	print fruits
	
fruits.insert(0, 'another new') #input another new fruit name
	print fruits

def first_letter(string):
	return string[0]
	fruits.sort(key=first_letter)
	for i in fruits:
		print fruits

