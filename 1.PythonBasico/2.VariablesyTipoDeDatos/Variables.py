"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
September 24, 2017
"Variables"
"""

#A variable is a location in memory used to store some data (value).

'''
We don't need to declare a variable before using it. 
In Python, we simply assign a value to a variable and it will exist. 
We don't even have to declare the type of the variable. 
This is handled internally according to the type of value we assign to 
the variable.
'''

'''
We use the assignment operator (=) to assign values to a variable. 
Any type of value can be assigned to any valid variable.
'''

number = 2

real = 2.2

word="Hi"

'''Multiple assignments
In Python, multiple assignments can be made in a single statement as follows:
'''
one, two, three = 1, "two", 3.0

#If we want to assign the same value to multiple variables at once, we can do this as
a=b=c=3.1416
print(a,b,c)
#in one line we use ;
print(one);print(two);print(three)

#Python Numbers

'''
Integers, floating point numbers and complex numbers falls under Python numbers category. 
They are defined as int, float and complex class in Python.

We can use the type() function to know which class a variable or a value belongs to and 
the isinstance() function to check if an object belongs to a particular class.
'''

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


#Python List
'''
List is an ordered sequence of items. 
It is one of the most used datatype in Python and is very flexible. 
All the items in a list do not need to be of the same type.

Declaring a list is pretty straight forward. 
Items separated by commas are enclosed within brackets [ ].

a = [1, 2.2, 'python']

'''
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

#Python Tuple
'''
Tuple is an ordered sequence of items same as list.
The only difference is that tuples are immutable. 
Tuples once created cannot be modified.

Tuples are used to write-protect data and are usually 
faster than list as it cannot change dynamically.

It is defined within parentheses () where items are 
separated by commas.

t = (5,'program', 1+3j)
'''
t = (5,'program', True)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable   ->   t[0] = 10

#Python Strings
'''
String is sequence of Unicode characters. 
We can use single quotes or double quotes to represent strings. 
Multi-line strings can be denoted using triple quotes, ''' 

'''
s = "This is a string"
s = '''#a multiline
''''''
s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python   ->  s[5] ='d'


#Python Set
'''
Set is an unordered collection of unique items. 
Set is defined by values separated by comma inside braces { }. 
Items in a set are not ordered.
'''

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

#Python Dictionary

'''
Dictionary is an unordered collection of key-value pairs.

It is generally used when we have a huge amount of data. 
Dictionaries are optimized for retrieving data. 
We must know the key to retrieve the value.

In Python, dictionaries are defined within braces {} with each 
item being a pair in the form key:value. 
Key and value can be of any type.
'''

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

# Generates error ->   print("d[2] = ", d[2]);


