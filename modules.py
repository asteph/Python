class Animal:
	def __init__(self,species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color

#copy module to copy an object
import copy
harry = Animal('hippogriff', 6, 'pink')
harriet = copy.copy(harry)
print harry.species
print harriet.species
# using copy module to copy a list
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogill', 0, 'paisley')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[1].species)
print(more_animals[2].species)
#copy function is a shallow copy meaning:
#it doesn't copy objects inside the objects copied
my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species)
#if a new animal is added to first list it doesn't appear in copy
#objects on same level not affected
sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)
print len(my_animals)
print len(more_animals)
#deepcopy gets copy that is complete with copies of:
#all of the associated objects
more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'wyrm'
print my_animals[0].species
#copied list doesn't save
print more_animals[0].species

#keyword module
import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('ozwald'))
print(keyword.kwlist)

#random module
import random
print(random.randint(1, 100))
print(random.randint(100, 1000))
#higher lower guessing game
num = random.randint(1, 100)
# while True:
# 	print('Guess a number between 1 and 100')
# 	guess = input()
# 	i = int(guess)
# 	if i == num:
# 		print('You guessed right')
# 		break
# 	elif i < num:
# 		print('Try higher')
# 	elif i > num:
# 		print('Try lower')
#use 'choice' to pick a random item from a list
desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
print(random.choice(desserts))
#use 'shuffle' to mix up list
random.shuffle(desserts)
print (desserts)




