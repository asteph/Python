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
	def left_foot_forward(self):
		print('left foot forward')
	def left_foot_back(self):
		print('left foot back')
	def right_foot_forward(self):
		print('right foot forward')
	def right_foot_back(self):
		print('right foot back')
	def dance(self):
		self.left_foot_forward()
		self.left_foot_back()
		self.right_foot_forward()
		self.right_foot_back()
#creating objects in a class
reginald = Giraffes()
harold = Giraffes()
#calling functions on objects
reginald.move()
reginald.dance()
harold.eat_leaves_from_trees()

#working with the turtle module
import turtle
#creating turtle objects of the Pen class
avery = turtle.Pen()
kate = turtle.Pen()
josh = turtle.Pen()
tony = turtle.Pen()
#drawing with the turtles
#challenge was to draw pitchfork
avery.forward(100)
kate.forward(100)
josh.forward(110)
tony.forward(110)
avery.left(90)
kate.right(90)
josh.left(90)
tony.right(90)
avery.forward(60)
kate.forward(60)
josh.forward(30)
tony.forward(30)
avery.right(90)
kate.left(90)
josh.right(90)
tony.left(90)
avery.forward(40)
kate.forward(40)
josh.forward(20)
tony.forward(20)
#keeps canvas window open
turtle.done()






