#initializing a class
class Things:
	pass
#parent class goes in parenthesis
#children classes inherit functions 
class Inanimate(Things):
	pass
class Animate(Things):
	pass
class Sidewalks(Inanimate):
	pass
class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move(self):
		print('moving')
	def eat_food(self):
		print('eating food')
class Mammals(Animals):
	def feed_young_with_milk(self):
		print('feeding young')
class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print('eating leaves')
#creating objects in a class
reginald = Giraffes()
harold = Giraffes()
#calling functions on objects
reginald.move()
harold.eat_leaves_from_trees()

#working with the turtle module
import turtle
#creating turtle objects of the Pen class
avery = turtle.Pen()
kate = turtle.Pen()
#drawing with the turtles
avery.forward(50)
avery.right(90)
avery.forward(20)
kate.left(90)
kate.forward(100)
#keeps canvas window open
turtle.done()






