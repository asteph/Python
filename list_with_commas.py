#Converts array into list n1, n2, ..., and n3
def humanizedList(array, sort = False):
 	#Your solution goes here!
 	if sort == True:
 		array.sort()
	lastItemPosition = len(array) - 1
	array[lastItemPosition] = "and %s." %(array[lastItemPosition])
	newArray = ', '.join(array)
	return newArray


#List of famous peeps
physicistsString = 'Gordon Freeman, Samantha Carter, Sheldon Cooper, Quinn Mallory, Bruce Banner, Tony Stark'

#TODO: Convert the string into an array
physicistsList = physicistsString.split(', ')

#Humanize that list
famousFakePhysicists = humanizedList(physicistsList, True)

#Output sentence
print "Some of the most famous fictional theoretical physicists are %s" %(famousFakePhysicists)