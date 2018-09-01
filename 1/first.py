news = 'This is justB some text'

# print news[8:1]

for i in range(1,11):
    # print(i)
    if i == 5:
        break

# print i

# g, h, k = 2, 5, "HELLO"

g= 2
h= 5
isAvalable = True
k= "HELLO"
k= 'HELLO'

# print(k)

k = "WORLD"
g = "HELLO"

WORLD = 'K'

stringed_int = '29'
p = int(stringed_int)

# chaangeing type of a data 

j = str(h)

# print(j)
# print(type(j))
# print(type(stringed_int))
# print(type(p))
# print(type(h))



# print("HELLO")
#

""" 
This is a 
multi-line 
comment with double quotes  """ 

''' 
This is a 
multi-line 
comment with single quote
''' 


# LISTS 

# Empty list

my_list = []

# print(my_list)

# list of int

my_list_int = [2, -3, 5, 8]

# print(my_list_int)

# list of strings 

my_list_str = ['blue', 'green', 'red', 'brown']

# print(my_list_str)


# list of Mixed type  
my_list_mix = ['blue', 10, 1, False, 'green', 'red', 'brown']

# print(my_list_mix)


# list of Mixed type with nested list 
my_list_mix_list = ['blue', 10, 1, False, 'green', 'red', 'brown', [1, 7, 'me'], my_list_int ]

# print(my_list_mix_list[0][2])
my_list_mix_list[0] = 'Purple'
print(my_list_mix_list)

my_list_mix_list.append('EGG')

new_list = ['Men', 'Women']

my_list_mix_list.extend(new_list)

my_list_mix_list.insert(0, 'EGG2')

# print((my_list_int).sort())
# print(len(my_list_mix_list))


pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# print(pow2)


pow2 = []
for x in range(1,5):
   pow2.append(2 ** x)

# print(pow2)

new_list1 = []

for i in range(len(my_list_int)):
	new_list1.append(my_list_int[i] ** 2)
	# print(my_list_int[i] ** 2)
	# print(i)

print(my_list_int.count(2))

# mean/Average of my_list_int
sum_all = 0
for i in range(len(my_list_int)):
	sum_all = sum_all + my_list_int[i]

avg = sum_all / len(my_list_int)
print("The average of " + str(my_list_int) + " is " + str(avg) )

# Turple 

# empty tuple
my_tuple = ()
# tuple of integers
my_tuple = (1, 2, 3)
# tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(my_tuple)

print(my_tuple.count('mouse'))

# Dictionary 

# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict1= dict({1:'apple', 2:'ball'})
print(my_dict1.get(2))
print(my_dict1[2])
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

# a 	list with dictionary
dict_list = [{'name': 'Joe', 'age': 28, 'gender': 'Male', 'color': 'green'},{'name': 'Mary', 'age': 27, 'gender': 'Female', 'color': 'pink'},{'name': 'Ade', 'age': 30, 'gender': 'Male', 'color': 'Red'}, ]

addy = [ 'Home', 'Home addy', 'Home sweet home']

print(dict_list)

for k in range(len(dict_list)):
	dict_list[k]['address'] = addy[k]
	print( str(  dict_list[k]['name']) + ' is ' +  str(dict_list[k]['age']) + ' years old and likes color '+ str(  dict_list[k]['color']) + ' and live at ' + str(  dict_list[k]['address'])  )



