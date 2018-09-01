import math
import time

print('Hello World') #output: Hello World

# name = input('What is your Name? ')

# print('Hello'+ str(name) )

# Imports 
print(math.pi)

print( "Start : " + str( time.ctime() ))
time.sleep( 3 )
print( "End : " + str( time.ctime() ))
print("HELLO WORLD")

print("This is a text that {} is trying to {} fommat ".format("Austine", "whatever"))

# Conditional statements 

num = 0
if num > 0:
    print(num, "is a positive number.")

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# LOOP/ Iteration

# FOR LOOP

# Program to find the sum of all numbers stored in a list
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0
# iterate over the list
for val in range(3,10):
	sum = sum+val
print("The sum is", sum) # Output: The sum is 48

#  WHILE LOOP

# Program to get the sum fo the first n numbers where 

n = 10
# initialize sum and counter
sum = 0
i = 0
while i <= n:
    sum = sum + i
    i = i+1    # update counter
    print(i)
    if i == 4:
    	break
# print the sum
print("The sum is ", sum)



def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")


#calling a function
greet('Ada')


# function to check the type class of a number (even, or odd)

def checkNumber(num):

	if (num % 2) == 0:
		print(str(num) + ' is an Even number')
	else:
		print(str(num) + ' is an odd number since its remmender after division is  '+ str((num % 2)))
	

checkNumber(0)


def compareStrings(str1, str2):
	if len(str1) > len(str2) :
		print(str1 + ' is longer than ' + str2)
	else:
		print(str2 + ' is longer than '+  str1)

string1 = input("ENter the first string ")	
string2 = input("ENter the second string ")

compareStrings(string1, string2)


# PURE function 

def getSumOfAList(number):
		
	# Program to find the sum of all numbers stored in a list
	# List of numbers
	
	# variable to store the sum
	sum = 0
	# iterate over the list
	for val in number:
		sum = sum+val
	
	return "The sum is", sum  # Output: The sum is 48

result = getSumOfAList([6, 5, 3, 8, 4, 2, 5, 4, 11])

print(result)


# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
