#Day 1 - Learning python till AI/ML Challenge
# Introduction - In this lesson u will learn basics of python

print("Hello world")    #the print function is used for printing outputs

#print can be used for calculations as follows

print(4+5)        #add
print(4-5)        #subtract
print(4 * 5)      #multiply
print(4 / 5)      #division
print(4 ** 5)     #exponential(powers or finding the square cube so on)
print(4 % 5)      #modulus
print(3 // 2)     #Floor division

# Data types
# Python consists of 9 common data types here we will first see how to check data types

print(type(11))               #Int
print(type(1 +3j))            #Complex
print(type(1.67))             #Float
print(type('Alexander'))      #String
print(type([2,4,6]))          #List
print(type({'name':'Alex'}))  #Dictionary
print(type({9.2,3.16,2.46}))  #Set
print(type((7.8,3.14,1.3)))   #Tuple
print(type(9 == 9))           #Bool

#Varibales
# Variables are used to store values or data.Here I am giving just the basic overview we will explore later
ex_string = 'Alexander'
num = 15
lift = 1.23
boo_lean1 = True
nothing = None
print(ex_string)
print(num)
print(lift)
print(boo_lean1)
print(nothing)


# in a situation where u have to change the text in print statement u need to go and do it individually but there is a shortcut for it
name = 'bob'
company = 'google'

print(f'This guy' + name + 'works in'+ company)

#there are more ways as to string formatting follows
# before Python 3.6.6 - .format()
print('Name:{}'.format(name))

#after python 3.6.6 - f-string or .format()
print(f'Name: {name}')


