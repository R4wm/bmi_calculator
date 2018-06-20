
import sys
########################
# Create functions here
#########################
def something(stuff):
	print "im doing stuff"

def function1(function):
	print "THis is another function"

def function2(something):
	print something

def turnsOnWater(temperature):
	print "Turning on %s water.." % temperature


def takeShower(place):
	'''
	place is a STRING, should only be upstairs or downstairs
	check arg
	'''
	turnsOnWater("hot")
	print "Taking shower in %s" %place



####################################
# Call functions here
####################################
function2("hahahah")
takeShower("upstairs")
something("im doing stuff")
function1("this is another function")




def bmi(weight, name):
	#print "this is your bmi"
	#print"1"
	height_f = 6
	#weight_kg = 40

	bmi = weight / (height_f ** 2)
	print ("bmi: ")
	print (bmi)
	if bmi < 25:
		print(name)
		print("is not overweight")
	else:
		print(name)
		print("is overweight")



bmi(25, "jeremiah")
bmi(5999, "Ray")