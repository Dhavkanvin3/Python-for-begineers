# Input and data conversion
#----------------------------------------------------------------
# we use the input() for getting user input example as follows:
answer = int(input("Enter the number:"))
# now when we get the input from user and produce output inform of calculation we do as follows:
num_a = int(input("Enter the first number:"))
num_b = int(input("Enter the second number:")) #note that this method is only valid for int datatype
total = num_a + num_b
print (total)
#now in order to get input in various data types in other words we want to convert in various data types
# we can do the follows:
str_num_a = str(num_a) #in string
float_num_a = float(num_a) #converts in float
bool_num_a = bool(num_a)  #convert integer to bool: true(non-0 is true)
neg_bool_numa= bool(0)  #convert 0 to boolean: False
# now for string to num
s = "123"
int_s= int(s)
float_s =float(s)  #converts string to float: 123.0
bools = bool(s) # string to boolean (if not empty) True
bool_empty = bool("") #for empty string... gives False

# Collection data types (lists , tuple, set , dictionary)

# 1) LISTS (Mutable Ordered Collection) - Used in 98% cases!
#-------------------------------------------------------------
empty_lists = []
lists = ['wall','floor','roof','sword','shield','AI','ML','Genai','computer vision','robotics']
list2=['door','phone']
# get item as follows
print(lists[2])
print(lists[-1])
# list slicing
print(lists[:2])
print(lists[3:])
print(lists[0:2])
# print(lists[::3])
# print(lists[2:5:3])
# print(lists[::-1])

#list methods
lists.append('door')
lists.extend(list2)
lists += list2
lists.sort()
print(lists.count('door'))
print(lists)
lists.insert(2,'sofa')
lists.remove('sofa')
item = lists.pop(3)
lists.reverse()
y = lists.copy()
