 # full lesson from Francis Royce1

# day1 assigning values to variables

site_name = 'programiz.com'
print(site_name)

site_name = 'apple.com'
print(site_name)

# assigning multiple values to multiple variables
a, b, c, = 5, 3.2, 'hello'
print(a)
print(b)
print(c)

# same value to multiple variable

a = b = 'francis Royce'
print(a)
print(b)

# case sensitivity
num = 6
Num = 44
print(num)
print(Num)

# python constants/creating constant

# special literals
value = None
print(value)

# 4 literal collections:
# 1- list Literal
fruits = ['apple', 'mango', 'orange']
print(fruits)

# 2 tuple literal
numbers = (1, 2, 3)
print(numbers)

# 3 dictionary literal
alphabets = {'a':  'apple', 'b': 'ball', 'c': 'cat'}
print(alphabets)

# 4 set literals
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)

# Day 2
# python data types

# 1- numerical data type
num1 = 1
print(num1, 'is of type', type(num1))   # integer
num2 = 2.1
print(num2, 'is of type', type(num2))   # float
num3 = 1 + 2j
print(num3, 'is of type', type(num3))   # complex
# number system: Binary- 0b, Octal- 0o, hexadecimal- 0x
print(0b1101011)
print(0o15)
print(0x123)
print(0xFB + 0b10)
# type conversion - the process of converting one type of number into another
print(1 + 2.0) #    operators convert integers to float implicitly (automatically)
# explicit conversion
num1 = int(2.3)
print(num1)

num2 = int(-2.9)
print(num2)

num3 = float(3)
print(num3)

num4 = complex('3+6j')
print(num4)

# random module (import random module)
import random
print(random.randrange(10, 20))

list = ['a', 'b', 'c', 'd', 'e']
print(random.choice(list))
print(list)
random.shuffle(list)
print(list)
print(random.random())

import random
random.seed(2)
print(random.random())
print(random.random())
print(random.random())

import random
a = 1
b = 3
print(random.uniform(a, b))
# look up for more random functions
# mathematics (math module): carries different mathematical functions
import math
print(math.pi)
print(math.gcd(2))
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))
print(math.sqrt(4))
sq = math.sqrt(4)
b = int(sq)
print(b)
# 2-list data type []
languages = ['swift', 'java', 'python']
print(languages)

# python list methods

# 1- access list items (indexing)
languages = ['swift', 'java', 'python']
# indexing (positive and negative indexing)
print(languages[0])
print(languages[1])
print(languages[2])
print(languages[-1])
print(languages[-2])
print(languages[-3])

# empty list
my_list = []
print(my_list)

# slicing of python list
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
print(my_list[2:5])
print(my_list[5:])
print(my_list[:])
print(my_list)
print(my_list[-9:])

# add elements to a python list
# 1- using (append): add an item at the end of the list
numbers = [21, 34, 54, 12]
print('Before Append:', numbers)
numbers.append(67)
print('After append:', numbers)

# 2- using extend(): to add all items of one list to another.
prime_numbers = [2, 3, 5]
print('list1:', prime_numbers)
even_numbers = [4, 6, 8]
print('list2:', even_numbers)
prime_numbers.extend(even_numbers)
print('list after extent', prime_numbers)

# change list items
'''python lists ara mutable: meaning lists are changeable'''
languages = ['swift', 'java', 'python']
languages[2] = "C++"
print(languages)

# remove item from the list using (del)
languages = ['swift', 'java', 'python']
del languages[0]
print(languages)

languages = ['swift', 'java', 'python']
del languages[0:2]
print(languages)

# 3- using (remove) to delete a list items
languages = ['swift', 'java', 'python']
languages.remove('java')
print(languages)

# clear()
languages = ['swift', 'java', 'python']
languages.clear()
print('list after clear:', languages)

# 4- del can be used also to empty the list
languages = ['swift', 'java', 'python']
del languages[:]
print('languages:', languages)

# 5-copying a list: it returns a new list and doesn't modify the original list
my_list = ['cat', 0, 6, 7]
new_list = my_list.copy()
print('copied list', new_list)

# 5-list copying using operator (=)
old_list = ['cat', 0, 6, 7]
new_list = old_list
print('New list:', new_list)
print('Old list', old_list)

# copy list using slicing syntax
my_list = ['cat', 0, 6, 7]
new_list = my_list[:]
new_list.append('dog')
print('Old list', my_list)
print('New list', new_list)

my_list = ['cat', 0, 6, 7]
new_list = my_list
print('Old list', my_list)
new_list[1] = 'dog'
print('New list', new_list)

# Day 3 continuation
# Deep copy and Shallow copy
# copying using operator (=)
old_list = [[1, 2, 3,], [4, 5, 6], [7, 8, 'a']]
new_list = old_list
new_list[1][0] = 9
print('old list:', old_list)
print('ID of old list', id(old_list))

print('new list:', new_list)
print('ID of old list', id(new_list))
# both variable share the same ID

# Shallow and Deep copy
'''here, original value unchanged and only modify the new values or vise versa'''
# here, to make it work we use 'copy module'

# Shallow Copy
'''it creates a new object which stores the reference of the original elements'''

import copy
old_list = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
print('old list:', old_list)
print('new list:', new_list)

'''to confirm that 'new list' is different from 'old list', we try to add new nested object'''
import copy
old_list = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
old_list.append([3, 3, 3])
print('old list:', old_list)
print('new list:', new_list)

import copy
old_list = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
old_list.append([3, 3, 3])
new_list.append([4, 4, 4])
print('old list:', old_list)
print('new list:', new_list)
# note, when you change any nested object in the 'old list, it will appear in the new liest
import copy
old_list = [[1, 2, 3,], [4, 5, 6], [7, 8, 55]] # changed 9 to 55, it will affect both
new_list = copy.copy(old_list)
old_list.append([7, 7, 7])
print('old list:', old_list)
print('new list:', new_list)

# using indexing for shallow copy
import copy
old_list = [[1, 2, 3,], [4, 5, 6], [7, 8, 55]]
new_list = copy.copy(old_list)
old_list[1][1] = 'AA'
print('old list:', old_list)
print('new list:', new_list)

# Deep copy
"""it creates a new object and recursively adds the copies of nested objects present in the original"""
# (deepcopy())
import copy
old_list = [[1, 2, 3,], [4, 5, 6], [7, 8, 55]]
new_list = copy.deepcopy(old_list)
print('old list:', old_list)
print('new list:', new_list)
"""if you make changes in the old list, it will affect the new list"""
import copy
old_list = [[1, 2, 3,], [4, 5, 6], [7, 8, 55]]
new_list = copy.deepcopy(old_list)
old_list[1][0] = 'Royce'
print('old list:', old_list)
print('new list:', new_list)

# 6-Python list count (count())
"""it returns the number of times the specified elements appears in the list"""
numbers = [2, 3, 5, 2, 11, 2, 7, 3]
count = numbers.count(2)
new_list = numbers
new_count = new_list.count(3)
print('count of 2:', count)
print('count of 3:', new_count)

# syntax of List Count() = list.count(elements)
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
vowel_count = vowels.count('i')
print('count of i is :', vowel_count)
vowel_count = vowels.count('p')
print('the count of p:', vowel_count)

# Count Tuple and list Elements inside list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4, 5,]]
count = random.count(('a', 'b'))
print("the count of ('a', 'b') is:", count)
count = random.count([3, 4, 5,])
print("the count of [3, 4, 5,] is :", count)

# Day 4
# python list insert()

vowels = ['a', 'e', 'i', 'u']
vowels.insert(3, 'o')
print('list:', vowels)

prime_numbers = [2, 3, 5, 7]
prime_numbers.insert(4, 11)
print('list:', prime_numbers)

Mixed_list = [{1, 3}, {2, 5} ]
Mixed_list.insert(2, (3, 4))
print('List:', Mixed_list)   #or

Mixed_list = [{1, 3}, {2, 5} ]
number_tuple = (6, 8)
Mixed_list.insert(2, number_tuple)
print('updated list:', Mixed_list)

# python list pop()
"""it removes the items at the given index from the list and returns the removed items"""
prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2)
print('removed Element:', removed_element)
print('updated list:', prime_numbers)

prime_numbers = [2, 3, 5, 7]
prime_numbers.pop(2)
print('updated list:', prime_numbers)  # only the updated list


languages = ['python', 'java', 'c++', 'french', 'c']
return_value = languages.pop(3)
print('return val:', return_value)
print('updated list:', languages)

# without an index
languages = ['python', 'java', 'c++', 'french', 'c']
return_value = languages.pop()
print('return val:', return_value)
print('updated list:', languages)   #or

languages = ['python', 'java', 'c++', 'french', 'c']
print('when index is not passed:')
print('return value:', languages.pop())
print('updated list:', languages)

# with negative index
print('\nwhen -1 is passed:')
print('return value', languages.pop(-1))
print('updated list:', languages)

print('\nwhen -3 is passed:')
print('return values:', languages.pop(-3))
print('updated list:', languages)

# python list reverse
"""it reverses the elements of the list: reverse()"""
prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()
print('reversed list:', prime_numbers)

languages = ['python', 'java', 'c++', 'french', 'c']
print('\noriginal list:', languages)
languages.reverse()
print('reversed list:', languages)

# reverse a list using slicing operator
languages = ['python', 'java', 'c++', 'french', 'c']
print('\noriginal list:', languages)
reversed_list = languages[::-1]
languages.reverse()
print('updated list:', reversed_list)

languages = ['python', 'java', 'c++', 'french', 'c']
reversed_list = languages
print('\noriginal list:', reversed_list)
reversed_list.reverse()
print('reversed list::', reversed_list)

# Accessing elements in reversed order
languages = ['python', 'java', 'c++', 'french', 'c']
for o in reversed(languages):
    print(o)

# python list sort()
"""sorts the items of the a list in ascending or descending order"""
prime_numbers = [2, 3, 5, 7]
prime_numbers.sort()
print(prime_numbers)

languages = ['python', 'java', 'c++', 'french', 'c']
languages.sort()
print('\nsorted list:', languages)

# descending order
prime_numbers = [2, 3, 5, 7]
prime_numbers.sort(reverse=True)
print('sorted list (in descending order):', prime_numbers)

# descending
prime_numbers = [2, 3, 5, 7]
prime_numbers.sort(reverse=False)
print('sorted list (in descending order):', prime_numbers)

  # Day 5
# sort with custom function using key
# take seconds element for sort
def takeSeconds(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=takeSeconds)
print('sorted list:', random)

# sorting using custom key
employees = [
    {'Name': 'Francis Royce', 'age': 28, 'salary': 1000},
    {'Name': 'Bethel', 'age': 30, 'salary': 500},
    {'Name': 'Marvelous', 'age': 18, 'salary': 90},
    {'Name': 'Blessing', 'age': 40, 'salary': 20},
]
# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')

def get_age(employee):
    return employee.get('age')

def get_salary(employee):
    return employee.get('salary')

# sort by name (ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# age (ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# salary (descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

# lambda
"""it is a good practice to use lambda function when the function can be summarised in one line"""
employees = [
    {'Name': 'Francis Royce', 'age': 28, 'salary': 1000},
    {'Name': 'Bethel', 'age': 30, 'salary': 500},
    {'Name': 'Marvelous', 'age': 18, 'salary': 90},
    {'Name': 'Blessing', 'age': 40, 'salary': 20},
]
# sort by name (ascending order)
employees.sort(key= lambda x: x.get('Name'))
print(employees, end='\n\n')

# age (ascending order)
employees.sort(key= lambda x: x.get('age'))
print(employees, end='\n\n')

# salary (descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')


# sorting using multiple keys
"""nested list of stuents info in a science class unn
list elements: (student's name, marks out of 100, age.)"""
participant_list = [
    ('Francis', 50, 40),
    ('Royce', 75, 18),
    ('Ifeanyi', 90, 22),
    ('Okoronkwo', 45, 12)
]
def sorter(item):
    # highest mark first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)
sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)

"""since the sorting logic function is small and fits in one line, 'lambda' function
is used instead inside 'key' rather than passing a separate function
"""
articipant_list = [
    ('Francis', 50, 40),
    ('Royce', 75, 18),
    ('Ifeanyi', 90, 22),
    ('Okoronkwo', 45, 12)
]
sorted_list = sorted(participant_list, key=lambda item: (100 - item[1], item[2]))
print(sorted_list)

# python list (index())
animal = ('cat', 'dog', 'rabit', 'horse')
index = animal.index('rabit')
print(index)
# index = animal.index('flies')
# print('the index of flies', index) #valueError cos flies is not in the tuple

# 'b' after 3rd index is searched
alphabets = ['a', 'b', 'c', 'd', 'b', 'c', 'a']
index = alphabets.index('a')
print('the index of a:',index)

index = alphabets.index('b', 3)
print('the index of b:', index)

# Day 6
#  python tuple data type(())
"""tuple is an ordered sequence of items same as a list.
the only difference is that tuples are immutable. tuples can not be modified once created ()"""
product = ('Royce', 'Francis', 60)
print(product[0])
print(product[1])

# different types of tuples
my_tuple = ()
print(my_tuple)
# integers
my_tuple = (1, 2, 3, 4)
print(my_tuple)
# mixed
my_tuple = (1, 'hello', 3.4)
print(my_tuple)
# nested tuple
my_tuple = ('mouse', [8, 4, 6], (1, 2, 3))
print(my_tuple)
# creating tuples without parenthesis
my_tuple = 1, 2, 3
print(my_tuple)
my_tuple = 1, 'hello', 3.2
print(my_tuple)
# python tuple with one element
var1 = ('hello')  # string
print(var1)
var2 = ('hello',) # tuple
print(var2)

var1 = ('hello')
print(type(var1))
var2 = ('hello',)
print(type(var2))
var1 = 'hello'
print(type(var1))
var2 = 'hello',
print(type(var2))

# accessing tuple elements
# indexing

letters = ('a', 'b', 'c', 'd', 'e', 'f')
print(letters[1])
print(letters[0])
print(letters[-3])
print(letters[-5])

# slicing
print(letters[1:4])
print(letters[:-4])
print(letters[4:])
print(letters[:])

# tuple methods
"""methods that add items or remove items are not available with tuple cos it is immutable
only two methods are available:"""
letters = ('a', 'a', 'c', 'a', 'b', 'c', 'd', 'e', 'f')
# 1 (count)
print(letters.count('a'))
print(letters.count('b'))
print(letters.count('c'))
# 2 iterating through a tuple
letters = ('a', 'a', 'c', 'a', 'b', 'c', 'd', 'e', 'f')
for letters in  letters:
    print(letters)
letters = ('a', 'a', 'c', 'a', 'b', 'c', 'd', 'e', 'f')
for letter in letters:
    print(letters)

# checking if item exist
letters = ('a', 'a', 'c', 'a', 'b', 'c', 'd', 'e', 'f')
print('a' in letters)
print('f' in letters)
print('z' in letters)

# Day 7
# python string data type
name = 'francis royce'
print(name)
# double quote
string1 = "python language"
print(string1)
# indexing strings
name = 'francis royce'
print(name[1])
print(name[-4])
# slicing strings
name = 'francis royce'
print(name[1:4])
# strings are immutable
name = 'francis'
print(name)
name =' royce'
print(name)
# python multiline strings: we use triple quotes
message = """Never gonna give up.
Never gonna let you down."""
print(message)

# python string operations
# 1- compare two strings
str1 = 'hello, world!'
str2 = 'i love python'
str3 = 'i love python'
print(str1 == str2)
print(str2 == str3)
# joining two or  more strings
name = 'Francis,'
surname = 'Royce'
result = name + surname
print(result)
# iterating through a python string
name = 'Francis Royce'
for name in name:
    print(name)
# python string length (len)
name = 'royce'
print(len(name))
name = 'Francis Royce'
name = len(name)
print(name)
# string membership
print('a' in 'royce')
print('o' in 'royce')

# upper case (upper())
name = 'francis royce'
print(name.upper())
# upper() return Value
string = 'this should be uppercase!'
print(string.upper())
str = 'th!s sh0uld b3 uPPercas3'
print(str.upper())

# how uppercase is used in a program
str1 = 'python is awesome'
str2 = 'PYTHON IS AWESOME'
if str1.upper() == str2.upper():
    print('the strings are the same')
else:
    print('the strings are not the same')
# lowercase
str2 = 'PYTHON IS AWESOME'
print(str2.lower())

# swapcase
str2 = 'PYTHON IS AWESOME'
print(str2.swapcase())

str2 = 'PYTHON IS AWESOME'
print(str2.swapcase())
print(str2.swapcase().swapcase())
print(str2.swapcase().swapcase() == str2)

# python string partitions (partition())
str = 'python is fun'
print(str.partition('is'))
print(str.partition('not'))  #  'not' is not found

str = "python is fun, isn't it"
print(str.partition('is'))
# Day 8 continuation
# python string rpartition()
"""it splits the string at the last occurrence of the argument"""
# string.rpartition
string = 'python is fun'
print(string.rpartition('is'))
print(string.rpartition('not'))

string = "python is fun, isn't it"
print(string.rpartition('is'))
# python string maketrans()
"""it is a static method that creates a one to one mapping of character to
its translation/replacement"""
# it takes three parameter (x[, y[, z]])
# translation table using a dictionary with maketrans()
dict = {'a': '123', 'b': '456', 'c': '789'}
string = 'abc'
print(string.maketrans(dict))

dict = {97: '123', 98: '456', 99: '789'}
string = 'abc'
print(string.maketrans(dict))
"""here, a dictionary 'dict' is defined. it contains a mapping of chracters a,b and c to 123,
456, 789"""

# translation tabe using two strings with maketrans()
firststring = 'abc'
secondstring = 'def'
string ='abc'
print(string.maketrans(firststring, secondstring))
# translational table with removable string with maketrans()
firststring ='abc'
secondstring = 'def'
thirdstring = 'abd'
string ='abc'
print(string.maketrans(firststring, secondstring, thirdstring))
"""here the mapping between the two strings 1st and 2nd are created
then, the third argument 3rd string resets the mapping of each character in it to none
and also creates a new mapping for none existent character"""

# python string translate()
"""it returns a string where each character is mapped to its corresponding chracter in the transaltion table"""
# string.translate()
firststring ='abc'
secondstring = 'def'
thirdstring = 'abd'
string = 'abcdef'
print('original string:', string)
translate = string.maketrans(firststring, secondstring, thirdstring)
print('translated string:', string.translate(translate))

# mapping with translate() with manual translation table
translate = {97: None, 98: None, 99: 105}
string = 'abcdef'
print('original string:', string)
print('transalted string:', string.translate(translate))

# python string replaace()
"""it replaces each matching occurrence of a substring with another string"""
text = 'bat ball'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)
# replace() method can take max of three arguments

song = 'cold, cold heart'
print(song.replace('cold', 'hurt'))

song = 'let it be, let it be, let it be, let it be'
print(song.replace('let', "don't let", 2))

new_song = song.replace('let', "don't let", 3)
print(new_song)

# Day 9
# python string find()
"""it returns the index of the first occurrence og the substring if found. if not, it returns -1"""
message = 'python is a fun programming language'
print(message.find('fun'))
# find() with no start and end argument
quote = 'let it be, let it be, let it be'
result = quote.find('let it')
print("substring 'let it:", result)

result = quote.find('be')
if (result != -1):
    print("Highest index where 'be,' occurs:", result)
else:
    print("doesn't contain substrings")

result = quote.find('small')
print("substring 'small':", result)

# find() with start and end arguments
quote = 'D0 small things with great love'
print(quote.find('things', 10))
print(quote.find('t', 2))
print(quote.find('o small', 10, -1))
print(quote.find('th', 6, 20))

# python String rfind()
"""returns highest index of the substring (if found). if not found, it returns -1"""
# str.rfind(sub[, start[, end]])

# rfind() with no start and end argument
quote = 'let it be, let it be, let it be'
result = quote.rfind('let it')
print("substring 'let it:", result)

result = quote.rfind('be')
if (result != -1):
    print("Highest index where 'be,' occurs:", result)
else:
    print("doesn't contain substrings")

result = quote.rfind('small')
print("substring 'small':", result)

# rfind() with start and end arguments
quote = 'D0 small things with great love'
print(quote.rfind('things', 10))
print(quote.rfind('t', 2))
print(quote.rfind('o small', 10, -1))
print(quote.rfind('th', 6, 20))

# python string rindex()
"""returns highest index of the substring inside the string(if found). if the substring is not found,
it raises an exception"""
# str.rindex (sub[, start[, end]])
# rfind() with no start and end argument
quote = 'let it be, let it be, let it be'
result = quote.rindex('let it')
print("substring 'let it:'", result)

# result = quote.rindex('small')
# print("substring 'small':", result)   # this will return valueError instead of -1 just the difference

# array of bytes of a given integer size
size = 5
print(bytearray(size))

# rindex() with start and end arguments
quote = 'D0 small things with great love'
# print(quote.rindex('things', 10))  #ValueError
print(quote.rindex('t', 2))
# print(quote.rindex('o small', 10, -1))  #ValueError
print(quote.rindex('th', 6, 20))

# python string format()
"""formats the given string into a nicer output in python"""
# basic formatting with format()
"""it allows the use of simple placeholders for formatting"""
# Basic formatting for default, positional and keyword arguments
# 1-default argument
print('hello {}, your balance is {}.'.format('Adam', 230.2346))

# positioning argument
print('hello {0}, your balance is {1}.'.format('Royce', 230.2346))

# keyword arguments
print('hello {Name}, your balance is {blc}.'.format(Name='Francis', blc=230.2456))

# mixed argument
print('hello {}, your balance is {blc}.'.format('Ifeanyi', blc=230.23456))

# simple number formatting
# integer arguments
print('The number is: {:d}'.format(123))
# float arguments
print('the float number is:{:f}'.format(190.0))
# octal, binary, and hexadecimal format
print('bin: {0:b}, oct: {0:o}, hex:{0:x}'.format(12))

# number formatting with padding for int and floating
# integer numbers with minimum width
print('{:5d}'.format(12))

# width doesn't work for numbers longer than padding
print('{:2d}'.format(1234))

# padding for float numbers
print('{:8.3f}'.format(12.2346))

# integer numbers with minimum width filled with zeros
print('{:05d}'.format(12))

# padding for float numbers filled with zeros
print('{:08.3f}'.format(12.2346))

# number formatting for signed numbers
# show the + sign
print('{:+f} {:+f}'.format(12.23, -12.23))

# show the -sign only
print('{:-f} {:-f}'.format(12.23, -12.23))

# show space for + sign
print('{: f} {: f}'.format(12.23, -12.23))

# number formatting with alignment

# number formatting with left, right and center alignment
print('{:>5d}'.format(12)) # right
print('{:^10.3f}'.format(12.1234)) # center
print('{:<05d}'.format(12)) # left
print('{:=8.3f}'.format(-12.2346))

# string formatting with for format()
# string formatting with padding and alignment
# string padding with left alignment
print('{:5}'.format('cat'))

# with right alignment
print('{:>5}'.format('cat'))

# center alignment
print('{:^5}'.format('cat'))

# padding with center alignment and '*' padding character
print('{:*^5}'.format('cat'*6))

print('{:*^5}'.format('cat'))

# Truncating strings with format()
# truncating to 3 letters
print('{:.3}'.format('caterpillar'))

# truncating to 3 letters and padding
print('{:5.3}'.format('caterpillar'))

# truncating to 3 letters and padding and center alignment
print('{:^5.3}'.format('caterpillar'))

# formatting class members using format()
# define person class
class person:
    age = 28
    name = 'Francis Royce'
# format age
print("{p.name}'s age is: {p.age}".format(p =person))

# formatting dictionary members using format()
# define person dictionary
person ={'age': 28, 'name': 'Francis Royce'}
print("{p[name]}'s age is: {p[age]}".format(p = person))

# easier way to format dictionaries using str.format(**mapping)
person ={'age': 28, 'name': 'Francis Royce'}
print("{name}'s age is: {age}".format(**person))
# day 10
# continuation
# dynamic formatting using format()
string = '{:{fill}{align}{width}}'
print(string.format('cat', fill='*', align='^', width=5))   # passing format codes as arguments

# dynamic float format templates
num = '{:{align}{width}.{precision}f}'
print(num.format(12.236, align='<', width=8, precision=2))  # passing format codes as arguments

# extra formatting options with format()
"""format() also supports type-specific formatting options like datetime's and complex number"""
# type-specific formatting with format() and overriding__format__() method
import datetime
date = datetime.datetime.now()
print("it's now: {:%y/%m/%d, Time: %H:%M:%S}".format(date))

# complex number formatting
complexNumber = 1 + 2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

# custom__format()__ method
class person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'
print("Adam's age is: {:age}".format(person()))

# __str()__ and __repr__ shorthand !r and !s using format()
print('Quotes: {0!r}, without Quotes: {0!s}'.format('cat'))

class person:
    def __str__(self):
        return 'STR'
    def __repr__(self):
        return 'REPR'
print('repr: {p!r}, str: {p!s}'.format(p=person()))

class person:
    def __str__(self):
        return 'STR'
    def __repr__(self):
        return 'REPR'
print('repr: {p!r}, str: {p!s}'.format(p=person))    # without () in person

# python string capitalize()
"""converts first character of a string to an uppercase"""
sentence = 'i love PYTHON'
cap = sentence.capitalize()
print(cap)
# syntax: string.capitalize()

sentence = 'python is Awesome'
cap = sentence.capitalize()
print(cap)
print('python is awesome'.capitalize())

# python string center()
# center() syntax
"""it returns a new centered string after padding it with the specified character"""
sentence = 'python is awesome'
new_string = sentence.center(24, "'")
print(new_string)

sentence = 'python is awesome'
new_string = sentence.center(24, '*')
print(new_string)

sentence = 'python is awesome'
new_string = sentence.center(20, '$')
print(new_string)

# center() with dafault argument
sentence = 'python is awesome'
new_string = sentence.center(24)
print('center string:', new_string)

print('python is awesome'.center(24, '*'))

# python string casefold()
"""converts all characters of the string into lowercase letters and returns a new string"""
text = 'pYtHon'
lower_cased = text.casefold()
print(lower_cased)
text = 'PYTHON IS FUN'
lower_cased = text.casefold()
print(lower_cased)
# casefold() as am agreesive lower() method
"""casfold() converts more characters into lower case than lower()"""

# python string count()
"""returns the number of occurrences of a substring in the given string"""
message = 'python is a popular programming language'
print('number of p', message.count('p'))

# count the number of occurrences of a given substring
string = "python is awesome, isn't it?"
substring = 'is'
count = string.count(substring)
print('the count is:', count)

# count number of occurrences of a given substring using start and end
string = "python is awesome, isn't it?"
substring = 'i'
count = string.count(substring, 8, 25)
print('the count is :', count)

string = 'python', 'royce', 'royce', 'francis'
print('string count is:', string.count('royce'))

# python string endswith()
"""it returns True if a string ends with the specified suffix. if not, it returns False"""
# endswitch() without start and end parameter
message = 'python is fun.'
end = message.endswith('is fun')
print(end)

message = 'python is fun.'
end = message.endswith('is fun.')
print(end)

message = 'python is fun.'
print(message.endswith('is fun'))

# endswitch() with start and end parameter
text = 'python programming is easy to learn.'
result = text.endswith('learn.', 7)  #  7 start parameter
print(result)

text = 'python programming is easy to learn.'
result = text.endswith('is', 7, 26)  #  7 start and end 26 parameter
print(result)
result = text.endswith('easy', 7, 26)
print(result)
# passing Tuple to endswitch()
text = 'programming is easy'
result = text.endswith(('programming', 'python'))
print(result)

result = text.endswith(('python', 'easy', 'java'))
print(result)
result = text.endswith(('is', 'an'), 0, 14)
print(result)

# read up on startswitch()
"""it returns True if a string starts with the specified prefix(string).
if not, it returns false"""

#  Python string expandtabs()
"""it returns copy of string with all tab character '\t' replaced with white space
characters until the next multiple of tabsize parameter."""
# expandtabs() with no argument
str = 'xyz\t12345\tabc'
result = str.expandtabs() # default size is 8
print(result)

# expandtabs() with different character
str = 'xyz\t12345\tabc'
print('original string:', str)
print('tabsize 2:', str.expandtabs(2))
print('tabsize 3:', str.expandtabs(3))
print('tabsize 4:', str.expandtabs(4))
print('tabsize 5:', str.expandtabs(5))
print('tabsize 6:', str.expandtabs(6))

# python string encode()
"""it returns the encoded version of the given string"""
title = 'python programming'
print(title.encode())

string = 'python'
print('the string:', string)
string_utf = string.encode()
print('the encoded version is:', string_utf)

# encoding with error parameter
print('the string is:', string)
print('the encoded version (with ignore) is:', string.encode('ascii', 'ignore'))
print('the encoded version (with replace) is:', string.encode('ascii', 'replace'))

# python string isalnum()
"""it returns True if all characters in the string are alphanumeric (either alphabets or numbers).
if not, it returns False"""

name1 = 'python3'
print(name1.isalnum())
name2 = 'python 3'
print(name2.isalnum())

string1 = 'm2324onica'
print(string1.isalnum())

string2 = 'm3onica royce11' #   contains white space
print(string2.isalnum())

# isalnum() in if...else statement
text = 'python#programming123'
if text.isalnum() == True:
    print('All characters of the string are alphanumeric.')
else:
    print('All characters of the string are not alphanumeric.')

# python string isalpha()
"""it returns True if all characters in the strings are alphabets. if not, it returns False"""
name1 = 'royce'
print(name1.isalpha())

name2 = 'Francis Royce' #   white space
print(name2.isalpha())

name3 = 'Francis2Royce'
print(name3.isalpha())

text = 'FrancisRoyce'
if text.isalpha() == True:
    print('All characters of the string are alphabets.')
else:
    print('All characters of the string are not alphabets.')

# python strings isdecimal()
"""if all characters of the string are decimal characters"""

s = '1234'
print(s.isdecimal())
print('1234'.isdecimal())
s2 = '12sd4'
print(s2.isdecimal())
s3 = '12royce francis'
print(s3.isdecimal())

# python isdigit()
"""all characters of the string are digit, returns True, if not False"""
str = '123'
print(str.isdigit())
str2 = 'python'
print(str.isdigit())

str3 = '123.99'
print(str3.isdigit())

# python string isidentifier()
"""returns True if the string is a valid identifierin python else Faalse"""
str = 'python'
print(str.isidentifier())

str = 'is'
print(str.isidentifier())

str = ''
print(str.isidentifier())
str = '22python'
print(str.isidentifier())

str = 'root33'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

str = '33root'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

str = 'root 33'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

# python string islower()
"""returns True if all alphabets are lowercase else False"""

s = 'this is good'
print(s.islower())

s = 'th!s is also g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())

s = 'this is francis royce'
if s.islower() == True:
    print('does not contain uppercase')
else:
    print('contains uppercase')

# python string isnumeric()
"""checks if all characters in the string are numeric"""
pin = '1234'
print(pin.isnumeric())
text = 'python3'
print(text.isnumeric())

# python string isprintable()
"""returns True if all characters in the string are printable"""
text = 'apple'
print(text.isprintable())
text = 'python programming'
print(text.isprintable())

text = 'python programming\n'
print(text.isprintable())

str = ''
print(str.isprintable())
# insprintable() with string containing ASCII
text = chr(27) + chr(97)
if text.isprintable():
    print('printable')
else:
    print('not printable')

# python string isspace()
"""returns True for only whitespace characters in the string else False"""
s = '   \t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ''
print(s.isspace())

s = '\n'
print(s.isspace())

s = '\n     \t'
if s.isspace() == True:
    print('All whitespace characters.')
else:
    print('contains non-whitespace characters')

s = '2+2 = 4'
if s.isspace() == True:
    print('All whitespace characters.')
else:
    print('contains non-whitespace characters')

# python string istitle()
"""returns True if the string is a titlecased string. if not, it returns False"""
s = 'Python Is Good'
print(s.istitle())
s = 'python is good'
print(s.istitle())
s = 'Python Is @ Symbol'
print(s.istitle())
s =  '99 Is A number'
print(s.istitle())
s = 'PYTHON'
print(s.istitle())
s = 'Francis Royce'
r = s.istitle()
print(r)

s = 'I Love Python'
if s.istitle() == True:
    print('Titlecased string')
else:
    print('Not a titledcased string')
# python isupper() parameter
str = 'THIS IS GOOD'
print(str.isupper())
str = 'THIS IS ALSO GOOD'
print(str.isupper())
str = 'THIS IS not GOOD'
print(str.isupper())

str = 'THIS IS GOOD'
if str.isupper() == True:
    print('Does not contain lowercase letter')
else:
    print('contains lowercase letter')
# python string join()
"""returns a string by joining all the elements of iterable(list, string, tuple),
separated by the given separator"""
text = 'python', 'is', 'a', 'fun', 'programming'
print(' '.join(text))
# list
numlist = ['1', '2', '3', '4', '5']
seperator = ', '
print(seperator.join(numlist))
# tuple
numtuple = ('1', '2', '3', '4', '5')
print(seperator.join(numtuple))


# two elements
s1 = 'abc'
s2 = 'def'
print('s1. join(s2):', s1.join(s2))

s1 = 'abc'
s2 = 'def'
s = s1.join(s2)
print('s1. join(s2):',s)
print('s1. join(s2):', s2.join(s1))
# sets
text = {'3','1', '4'}
s = ', '
print(s.join(text))

text = {'python', 'java', 'ruby'}
s = '->->'
print(s.join(text))
"""a set is an unordered collection of items, so you may get different output (random)"""

# dictionary
text = {'mat': 1, 'that': 2}
s = '->'
print(s.join(text))

# python string ljust()
"""returns a left-justified string of a given minimum"""
# left justify string of minimum width
str = 'cat'
width = 5
print(str.ljust(width))

# left justify string and fill the remaining spaces
str = 'cat'
width = 5
fillchar = '*'
print(str.ljust(width, fillchar))

str = 'cat'
width = 3
fillchar = '*'
print(str.ljust(width, fillchar))

# python string rjust()
str = 'cat'
width = 5
fillchar = '*'
print(str.rjust(width, fillchar))

str = 'cat'
width = 5
print(str.rjust(width))

# python string lstrip()
"""returns a copy of the string with leading characters removed (based on the string argument)"""
str = '     this is good'
print('original string:', str)
print('whitespace removed:', str.lstrip())

print(str.lstrip('sti'))
print(str.lstrip('s ti'))

website = 'https://www.francisroyce.com/'
print(website.lstrip())

website = 'https://www.francisroyce.com/'
print(website.lstrip('https://'))

# python rstrip()
str = '     this is good'
print('original string:', str)
print('whitespace removed:', str.rstrip())
print(str.rstrip('sti'))
print(str.rstrip('s ti'))

website = 'https://www.francisroyce.com/'
print(website.rstrip())

website = 'https://www.francisroyce.com/'
print(website.rstrip('com/'))

title = 'python programming'
result = title.rstrip()
print(result)

# python strip()
"""returns a copy of the string by removing both the leading and the trailing characters
(based on the string argument passed)"""
message = '     learn python'
print('nessage:', message.strip())

string = '     xoxo love xoxo   '
print(string)
print(string.strip())
print(string.strip('  xoe'))
print(string.strip('stx'))
string = 'android is awesome'
print(string.strip('an'))

# python string split()
"""splits a string at the specified separator and returns a list of substrings"""
cars = 'BMW- Tesla-Range Rover'
print(cars.split('-'))

text = 'love thy neighbor'
print(text.split())
grocery = 'milk, chicken, bread'
print(grocery)
print(grocery.split())
print(grocery.split(',  '))
print(grocery.split(':'))
# use of maxsplit(): specifies the maximum number of splits to be performed on string
grocery = 'milk, chicken, bread, butter'
print(grocery.split(',  ', 2))
print(grocery.split(',  ', 1))

# python string rsplit()
"""splits strings from the right"""
text = 'love thy neighbor'
print(text.rsplit())

grocery = 'milk, chicken, bread, butter'
print(grocery.rsplit(', '))
print(grocery.split(':'))

# with maxsplit
print(grocery.rsplit(', ', 2))
print(grocery.rsplit(', ', 1))
print(grocery.rsplit(', ', 5))
print(grocery.rsplit(', ', 0))

# python string splitlines()
# splits the string at line breaks and returns a list
# \n is a line boundary
sentence = 'i\nlove\nphython\nprogramming'
print(sentence.splitlines())

grocery = 'milk\nchicken\nbread\rbutter'
print(grocery.splitlines())

# splitlines() with multi-line string
grocery = ''' milk
chicken
breaed
butter'''
print('original string:', grocery)
print(grocery.splitlines())

# passing boolean value in splitline
grocery = 'milk\nchiken\nbrfead\nbutter'
print(grocery)
print(grocery.splitlines(True))
print(grocery.splitlines(False))

# passing number in splitlines()
print(grocery.splitlines(0))
print(grocery.splitlines(5))

# python string zrfill()
"""returns copy of the string with '0' characters padded to left"""
text = 'python is fun'
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))

# how zfill() works with sign prefix
num ='-230'
print(num)
print(num.zfill(8))
text = '--random+text'
print(text.zfill(20))

# python string format_map()
"""similar to str.format(*mapping) except that str.format creates a new dictionary
whereas str.format_map doesn't"""
point = {'x': 4, 'y': -5}
print('{x} {y}'.format(**point))
point = {'x': 4, 'y': -5}
print('{x} {y}'.format_map(point))
point = {'x': 4, 'y': -5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

# how to format_map works with dic subclass
class coordinate(dict):
    def __missing__(self, key):
        return key
# print('({x}, {y})'.format_map(coordinate(x='6')))
# print('({x}, {y})'.format_map(coordinate(y='9')))
# print('({x}, {y})'.format_map(coordinate(x='6', y='0')))

# # python set Data type
"""set is an unordered collections of unique items.defined by value separated by
commas inside braces{}"""
student_id = {112, 114, 116, 118, 119}
print(student_id)
print(type(student_id))

empty_set = {}
print(empty_set)
print(type(empty_set))

# duplicate items in a set
numbers = {1, 0, 3, 4, 4, 7, 1, 1}
print(numbers)  # no duplicate items

# add items to a set in python
numbers = {21, 22, 23, 24}
print('initial set:', numbers)
numbers.add(34)
print(numbers)
print('update set:', numbers.add(34))

# update python set
companies = {'lacoste', 'francis royce'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)

# remove element from a set, we use 'discard()'
languages = {'swift', 'java', 'python'}
print('initial set:', languages)
removedValue = languages.discard('java')
print('set after removed():', languages)

# iterate over a set in python
fruits = {'apple', 'peach', 'mango'}
for fruit in fruits:
    print(fruit)

fruits = {'apple', 'peach', 'mango'}
for fruit in fruits:
    print(fruits)

# find number of set elements: len()
even_numbers = {2, 4, 6, 8}
print('set:', even_numbers)
print('total element:', len(even_numbers))

# python set operations
"""provides different buit-in methods to perform mathematical set operations"""
# union of two sets: we use (|) or union()
A = {1, 3, 5}
B = {0, 2, 4}
print('union using |:', A | B)
print('union using union():', A.union(B))

# set intersection
# we use & operator or intersection()
A = {1, 3, 5}
B = {0, 2, 4}
print(A & B)
print(A.intersection(B))

A = {1, 3, 5}
B = {1, 2, 3}
print(A & B)
print(A.intersection(B))

# difference between two sets
# we use (-) operator or difference()
A = {1, 3, 5}
B = {0, 2, 4}
print(A - B)
print(A.difference(B))

A = {2, 3, 5}
B = {1, 2, 6}
print(A - B)
print(A.difference(B))

# set symmetric difference
# we use (^) operator or the symmetric_difference()
A = {2, 3, 5}
B = {1, 2, 6}
print(A^B)
print(A.symmetric_difference(B))

# check if two sets are equal: ==
A = {2, 3, 5}
B = {1, 2, 6}
print(A==B)

if A==B:
    print('set A and B are equal.')
else:
    print('Set A and B are not Equal.')

# python set remove()
languages = {'swift', 'java', 'python'}
languages.remove('java')
print(languages)

# deleting element that doesn't exist
languages = {'swift', 'java', 'python'}
# languages.remove('fish')
# print(languages)  KeyError (fish)

languages = {'swift', 'java', 'python'}
languages.discard('fish')
print(languages)
"""discard() removes the specified elements from the set. if trhe element doesn't exist,
 the set remains unchanged unlike Remove() that will return Error"""

# python set Copy()
numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()
print(new_numbers)

# copy using == operator
name = {'francis', "royce", 'okoronkwo', 'ifeanyi'}
new_name = name
print(new_name)

# add items to the set after copy()
numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()
new_numbers.add(5)
print(new_numbers)

numbers = {1, 2, 3, 4}
new_numbers == numbers
new_numbers.add(5)
print(new_numbers)

# python set clear()
"""removes all items from the set"""
prime = {2, 3, 5, 7}
prime.clear()
print(prime)

# python set difference_update()
"""computes the difference between two sets(A-B) and updates set A with the resulting set."""
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}
print(A.difference_update(B))

A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}
A.difference_update(B)
print(A)

# python set intersection_update()
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}
A.intersection_update(B)
print(A)

A = {1, 3, 5, 7}
B = {2, 3, 5, 7, 11}
C = {4, 5, 6, 9, 10}
A.intersection_update(B, C)
print(A)
print(B)
print(C)

# python set isdisjoint()
A = {1, 3, 5, 7, }
B = {4, 5, 6}
A.isdisjoint(B)
print(A)
print(A.isdisjoint(B))

# python disjoint()
A = {1, 3, 5, 7}
B = {2, 3, 5, 7, 11}
C = {4, 5, 6, 9, 10}
print(A.isdisjoint(B))
print(B.isdisjoint(C))

# python set issubset()
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))

# python set pop()
"""randomly removes an item from a set and returns the removed item"""
A = {'a', 'b', 'c', 'd'}
removedItem = A.pop()
print(A)

A = {'a', 'b', 'c', 'd'}
print(A.pop())
print(A)

# python set symmetric_difference_update()
A = {'a', 'c', 'd'}
B = {'c', 'd', 'e'}
A.symmetric_difference_update(B)
print(A)
print(A.symmetric_difference_update(B))

# buit-in fucntions
# python abs()
"""returns absolute value of the given  number"""
number = -20
print(abs(number))

number = -20
ab = abs(number)
print(ab)

number = -20.07
print(abs(number))

number = (-3 - 4j)
print(abs(number))

# python any()
"""returns True if any element of an iterable is True. if not, it returns False"""
boolean_list =['true', 'false', 'true']
print(any(boolean_list))

# using any() on python list
I = [1, 3, 4, 0]
print(any(I))

I = [0, False]
print(any(I))

I = [0, False, 5]
print(any(I))

I =[]
print(any(I))

# using any() on python string
s = 'this is good'
print(any(s))

s = '000'
print(any(s))   #   o is Flase, but here 0 is True since is a string character
s = ''
print(any(s))

# python dictionries using any()
d = {0: "False"}
print(any(d))
d = {0: 'False', 1: 'True'}
print(any(d))
d = {0: 'False', False: 0}
print(any(d))
d = '0:' 'False'
print(any(d))

# python all()
I = [1, 3, 4]
print(all(I))

I = [1, 3, 4, 0]
print(all(I))

I = [0, False]
print(all(I))

I = [0, False, 5]
print(all(I))

I =[]
print(all(I))

d = {0: "False"}
print(all(d))
d = {0: 'False', 1: 'True'}
print(all(d))
d = {0: 'False', False: 0}
print(all(d))
d = '0:' 'False'
print(all(d))

# python ascii()
"""replaces non-printable character withy its correspponding ascii value and returns it"""

# python bin()
"""converts integers to its binary form"""
num = 15
print(bin(num))
num = 5
print(bin(num))

# python bin() with a non-integer class
class quantity:
    apple = 1
    orange = 2
    grapes = 2
    def func():
        return apple + orange + grapes
# print(bin(quantity()))
"""we have passed an object of class (quantity) to the bin()
method and got a typeError """
# this can be fixed using __index__() method

# bin() with __index__() for Non-integer class
class Quantity:
    apple = 1
    orange = 2
    grapes = 2
    def __index__(self):
        return self.apple + self.orange + self.grapes
print(bin(Quantity()))

# python bool(): returns bool value
test = 1
print(test, 'is', bool(test))
test = False
print(test, 'is', bool(test))
test = []
print(test, 'is', bool(test))
test = None
print(test, 'is', bool(test))

# python bytearray
"""returns bytearray object which is an array of the given bytes"""
prime_number = [2, 3, 5, 7]
byte_array = bytearray(prime_number)    # mutable (byearray)
print(byte_array)
print(bytes(prime_number))  # immutable (bye)

# array of bytes from a string
string = 'python is interesting'
arr = bytearray(string, 'utf -8')
print(arr)

# array of bytes of a given integer size
size = 5
print(bytearray(size))

# python callable()
"""returns True if the object passed appears callable. if not, it returns False"""
x = 5
print(callable(x))

def testfunction():
    print('Test')
y = testfunction
print(callable(y))

# callable object
class foo:
    def __call__(self):
        print('print something')
print(callable(foo))

# object appears to be callable but isn't callable
class Foo:
    def printline(self):
        print('print something')
print(callable(Foo))

# python chr()
"""converts an integer to its unicode character and returns it."""
print(chr(97))
a = 98
print(chr(a))
print(chr(1200))
print(chr(65))
# negative integers are out of range and returns error

# chr() with Non-Integer Arguments
# print(chr('royce'))  errorvalue too

# compile()
"""computes python code from a source object and returns it."""
codeInstring = 'a = 8\nb=7\nsum=a+b\nprint("sum =", sum)'
codeObject = compile(codeInstring, 'sumstring', 'exec')
exec (codeObject)
print(codeObject)
print(codeInstring)

codeInstring = 'a = 8\nb=7\nMul=a*b\nprint("Mul =", Mul)'
codeObject = compile(codeInstring, 'Mulstring', 'exec')
exec (codeObject)

# python classmethod()
"""returns class method for the given function"""
class student:
    marks = 0
    def computer_marks(self, obtained_marks):
        marks = obtained_marks
        print('obtained_marks:', marks)
# convert computer_marks() to classmethod()
student.print_marks = classmethod(student.computer_marks)
student.print_marks(99)

 # classmethod is always attached to a class
class person:
    age = 25
    def printAge(cls):
        print("The age:", cls.age)
person.printAge = classmethod(person.printAge)
person.printAge()


class MyClass:
    x = [1, 2, 3]

    @classmethod
    def modify_x(cls, new_val):
        cls.x.append(new_val)

MyClass.modify_x(4)
print(MyClass.x) # prints [1, 2, 3, 4]

obj = MyClass()
obj.modify_x(5)
print(obj.x)  # prints [1, 2, 3, 4, 5]

class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")

MyClass.my_static_method() # Output: "This is a static method."

class MyClass:
    my_variable = 0

    @classmethod
    def increment_variable(cls):
        cls.my_variable += 1

print(MyClass.my_variable) # 0
MyClass.increment_variable()
print(MyClass.my_variable) # 1

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Francis', 28)
person.display()

person1 = Person.fromBirthYear('Royce',  1994)
person1.display()

# python complex()
z = complex(2, 3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)

# creating complex without using complex
a = 2+3j
print('a =', a)
b = -2j
print('b = ', b)
c = 0j
print('c =', c)
print(type(a))
print(type(b))
print(type(c))

# python delattr()
"""deletes an attribute from object(if the object allows it)"""
class Coordinate:
    x = 10
    y = -5
    z = 0
point1 = Coordinate()
print('x =', point1.x)
print('y =', point1.y)
print('z =', point1.z)

delattr(Coordinate, 'z')
print('--After deleting z attribute--')
print('x =', point1.x)
print('y =', point1.y)
# print('z =', point1.z) Error cos it has been deleted
#
# # deleting attribute using del operator
class Coordinate:
    x = 10
    y = -5
    z = 0
point1 = Coordinate()
print('x =', point1.x)
print('y =', point1.y)
print('z =', point1.z)

del Coordinate.y
print('x =', point1.x)
# print('y =', point1.y) error
print('z =', point1.z)

# python dict()
"""creates a dictionary in python"""
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))

# keyword argument is not passed
# numbers1 = dict([('x', 5), ('y', -5)])
# print('numbers1 =',numbers1)
#
# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

# zip() creates an iterable in Python 3
numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print('numbers3 =',numbers3)

numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)

# you don't need to use dict() in above code
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)

# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)

# python dir()
"""returns the list of the valid attributes of the passed object"""
number = [12]

# returns valid attributes of the number list
print(dir(number))

number1 = [1, 2, 3]

#dir with a filled list
print(dir(number1))

number2 = [ ]

# dir() with an empty list
print(dir(number2))

number = {12, 15, 18, 21}

# dir() with a filled set
print(dir(number))

number1 =[ ]

# dir() with an empty set
print(dir(number1))

number = (21, 10, 81, 25)
#dir with a filled tuple
print(dir(number))

number1 =[]
# dir() with an empty tuple
print(dir(number1))

class Person:
  def __dir__(self):
    return ['age', 'name', 'salary']

teacher = Person()
print(dir(teacher))

# python divmod()
"""takes two numbers as an arguments and returns their quotient and remainder in a tuple"""
# returns the quotient and remainder of 8/3
result = divmod(8, 3)

print('Quotient and Remainder = ', result)

# divmod() with integer arguments
print('divmod(8, 3) = ', divmod(8, 3))

# divmod() with integer arguments
print('divmod(3, 8) = ', divmod(3, 8))

# divmod() with integer arguments
print('divmod(5, 5) = ', divmod(5, 5))

# divmod() with float arguments
print('divmod(8.0, 3) = ', divmod(8.0, 3))

# divmod() with float arguments
print('divmod(3, 8.0) = ', divmod(3, 8.0))

# divmod() with float arguments
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))

# divmod() with float arguments
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))

# Use divmod() to divide 7 by 3
result = divmod(7, 3)
print(result)
# Output: (2, 1)

quotient, remainder = divmod(7, 3)
print(quotient) # Output: 2
print(remainder) # Output: 1

quotient = 7 // 3
remainder = 7 % 3
print(quotient)
print(remainder)

# python enumerator()
"""enumerator() function adds a counter to an iterable and returns it(the enumerate object)"""
language = ['python', 'java', 'javascript']
enumerate_prime = enumerate(language)
print(list(enumerate_prime))
print(enumerate_prime)  # no list

# you can convert enumerate objects to list and tuple using list() and tuple()
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

enumerateGrocery = enumerate(grocery, 1)
print(list(enumerateGrocery))

# loop over an enumerate object
grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery, 1):
    print(item)

print()

for count, item in enumerate(grocery):
    print(count, item)

print()

for count, item in enumerate(grocery, 100):
    print(count, item)

for count, item in enumerate(grocery, 100):
    print((count, item))

for count, item in enumerate(grocery, 100):
    print((count), (item))

# python filter()
"""filter() function selects elements from an iterable (list, tuple etc.) based on the output
of a function.
the function is applied to each element of the iterable and if it returns True, the element
is selected by the filter() functions
"""
def check_even(number):
    if number % 2 == 0:
        return True
    return False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if an element passed to check_even() returns True, select it
even_numbers_iterator = filter(check_even, numbers)
# convert to list
even_numbers = list(even_numbers_iterator)
print(even_numbers)

def check_even(number):
    if number % 2 == 0:
        return True
    return False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if an element passed to check_even() returns True, select it
even_numbers_iterator = filter(check_even, numbers)
# convert to list
even_numbers = tuple(even_numbers_iterator)   # tuple
print(even_numbers)

def check_even(number):
    if number % 2 == 0:
        return True
    return False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if an element passed to check_even() returns True, select it
even_numbers_iterator = filter(check_even, numbers)
# convert to list
even_numbers = set(even_numbers_iterator)  # set
print(even_numbers)

letters = ['a', 'b', 'c', 'e', 'i', 'j', 'o']
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in  vowels else False
filter_vowels = filter(filter_vowels, letters)
vowels = tuple(filter_vowels)
print(vowels)

# using lambda function inside filter()
numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)
even_numbers = list(even_numbers_iterator)
print(even_numbers)

# using None as a function inside filter()
random_list = [1, 'a', 0, False, True, '0']
filter_iterator = filter(None, random_list)
filter_list = list(filter_iterator)
print(filter_list)

# python eval()
"""parses the expression passed to this method and runs python expression (code)
within the program."""
number =9
square_number = eval('number * number')
print(square_number)

x = 1
print(eval('x + 1'))

# practical example to demonstrate use of eval

# parameter of square
# Perimeter of Square
def calculatePerimeter(l):
    return 4*l

# Area of Square
def calculateArea(l):
    return l*l

expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break

from math import *
print(eval('dir()'))

# passing empty dictionary as globals parameter

# from math import *
# print(eval('dir()', {}))
#
# # The code will raise an exception
# print(eval('sqrt(25)', {}))

# making certain method available
from math import *
print(eval('dir()', {'sqrt': sqrt, 'pow': pow}))

from math import *
names = {'square_root': sqrt, 'power': pow}
print(eval('dir()', names))

# Using square_root in Expression
print(eval('square_root(9)', names))

#  Passing both globals and locals dictionary
from math import *

a = 169
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))

# python float()
int_number = 25

# convert int to float
float_number = float(int_number)
print(float_number)

# How float() works in Python?
# for integers
print(float(10))

# for floats
print(float(11.22))

# for string floats
print(float("-13.33"))

# for string floats with whitespaces
print(float("     -24.45\n"))

# string float error
# print(float("abc"))

# float() for infinity and Nan(Not a number)?
# for NaN
print(float("nan"))
print(float("NaN"))

# for inf/infinity
print(float("inf"))
print(float("InF"))
print(float("InFiNiTy"))
print(float("infinity"))

# python format()
value = 45

# format the integer to binary
binary_value = format(value, 'b')
print(binary_value)
# b is for binary

# Number formatting with format()
# d, f and b are type

# integer (d)
print(format(123, "d"))

# float arguments (f)
print(format(123.4567898, "f"))

# binary format(b)`
print(format(12, "b"))

# Number formatting with fill, align, sign, width, precision and type
# integer
print(format(1234, "*>+7,d"))

# float number
print(format(123.4567, "^-09.3f"))
"""
Here, when formatting the integer 1234, we've specified the formatting specifier *>+7,d. Let's understand each option:

* - It is the fill character that fills up the empty spaces after formatting
> - It is the right alignment option that aligns the output string to the right
+ - It is the sign option that forces the number to be signed (having a sign on its left)
7 - It is the width option that forces the number to take a minimum width of 7, other spaces will be filled by fill
 character
, - It is the thousands operator that places a comma between all thousands.
d - It is the type option that specifies the number is an integer.
When formatting the floating point number 123.4567, we've specified the format specifier ^-09.3f. These are:

^ - It is the center alignment option that aligns the output string to the center of the remaining space
- - It is the sign option that forces only negative numbers to show the sign
0 - It is the character that is placed in place of the empty spaces.
9 - It is the width option that sets the minimum width of the number to 9 (including decimal point, thousands comma
and sign)
.3 - It is the precision operator that sets the precision of the given floating number to 3 places
f - It is the type option that specifies the number is a float."""

# Using format() by overriding __format__()
# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print(format(Person(), "age"))

# python frozenset()
"""The frozenset() function returns an immutable frozenset object
initialized with elements from the given iterable"""
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
# fSet.add('v')

# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = A.copy()
print(C)

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

# Frozensets
# initialize A, B and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# isdisjoint() method
print(A.isdisjoint(C))  # Output: True

# issubset() method
print(C.issubset(B))  # Output: True

# issuperset() method
print(B.issuperset(C))  # Output: True

# python getattr()
"""The getattr() method returns the value of the named attribute of an object. If not found,
it returns the default value provided to the function.
"""
class Student:
    marks = 99
    name = 'Francis Royce'
person = Student()
name = getattr(person, 'name')
print(name)
marks = getattr(person, 'marks')
print(marks)

# How getattr() works in Python?
class Person:
    age = 28
    name = 'Francis Royce'
person =Person()
print('the age is:', getattr(person, 'age'))
print('the age is:', person.age)
print('the name is:', person.name)
print('the name is:', getattr(person, 'name'))

# getattr() when named attribute is not found
class Person:
    age = 23
    name = "Adam"

person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))

# when no default value is provided
# print('The sex is:', getattr(person, 'sex'))  error

# python global()
"""returns a dictionary with all the global() variables and symbols for the current program"""
print(globals())
age = 28
globals()['age'] = 29
print('the age is:', age)

age = 28
Age = globals()['age']
print('the age is:', Age)

# python exec()
"""executes a dynamically created program, which is either a string or a code object"""
program = 'a = 5\nb=10\nprint("sum =", a+b)'
exec(program)
# exec() multiline input
program = input("Enter a program:")
b = compile(program, 'something', 'exec')
exec (b)

program = input("Enter a program:")
exec (program)

# checking usable code with exec()
from math import *
exec ('print(dir())')

# blocking all the global buitin methods with the code: {'__builtins__' : None}
from math import *
globalsParameter = {'__builtins__' : None}
localsParameter = {'print': print, 'dir' : dir}
exec ('print(dir())', globalsParameter, localsParameter)

# python hasattr()
"""returns true if an object has trhe given named attribute and false if it does not"""
class Person:
    age = 23
    name = 'Francis Royce'
person = Person()
print("person's age:", hasattr(person, 'age'))
print("person's name:", hasattr(person, 'name'))
print("person's salary:", hasattr(person, 'salary'))

print()
class Person:
    age = 23
    name = 'Francis Royce'
    salary = '100$'
person = Person()
print("person's age:", hasattr(person, 'age'))
print("person's name:", hasattr(person, 'name'))
print("person's salary:", hasattr(person, 'salary'))

# python help()
"""calls the built-in python help system"""
print(help(list))
print()
print(help(dict))
print(help(print))
print(help([1, 2, 3]))
print(help('random thing'))
print(help(str))
print(help(help))
print(help('print'))
print(help('def'))
from math import *
help('math.pow')
help(True)
help(quit)

# python hex()
number = 45
print(number, 'in hex =', hex(number))
returnNumber = hex(number)
print(type(returnNumber))

# hex representation of a flaot
number = 2.0
print(number, 'in hex =', float.hex(number))

# python hash
text = 'Python Programming'
hashValue = hash(text)
print(hashValue)

# hash for integer is unchanged
print(hash(123))
# hash for decimal
print(hash(123.99))
# hash for string
print(hash('Francis Royce'))

# hash for immutable tuple object
numbers = (1, 2, 3, 4, 5,)
print(hash(numbers))

# hash() for custom objects ny overriding__hash__()
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name
    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))
person =Person(28, 'Francis Royce')
print(hash(person))

# python input()
strings = input()
print('The inputted string is:', strings)


strings = input('Enter a string:')
print("the inputted string is:", strings)

# python id()
a =3
b =6
sum = a + b
print(sum)
print(id(sum))

class Food:
    banana = 15
food = Food()
print(id(food))

fruits = {'oranges', 'banana', 'mango'}
print(id(fruits))

numbers =[1, 2, 3, 4,5]
print(isinstance(numbers, list))
print(isinstance(numbers, tuple))

class Foo:
    a = 5
fooinstance = Foo()
print(isinstance(fooinstance, Foo))
print(isinstance(fooinstance, (list, tuple)))
print(isinstance(fooinstance,(tuple, list, Foo)))

# python int()
print(int(123))
print(int(9.999))
print(int('123'))
print(int('0b101', 2))
# int() for custom objects
"""even if an object is not a number, we can still convert it to an integer object
we can do this by overriding __index__() and __int__()"""
class Person:
    age = 23
    def __index__(self):
        return self.age
person = Person()
print('int(person) is :', int(person))

# python issubclass()
class Polygon:
    def __init__(polygonType):
        print('Polygon is a', polygonType)
class Triangle(Polygon):
    def __init__(self):
        polygon.__init__('triangle')
print(issubclass(Triangle,Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))  # a class is a subclass of itself

# python iter()
"""returns an iterator for given argument"""
phones = ['apple', 'samsung', 'tecno']
phone_iter = iter(phones)
print(phone_iter)
print(next(phone_iter))
print(next(phone_iter))
print(next(phone_iter))

print()
for item in phones:
    print(item)  # shorter

# iter() for
class PrintNumber:
    def __init__(self, max):
        self.max = max

# iter() method in a class
    def __iter__(self):
        self.num = 0
        return self
# next() method in a class
    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))  # 1
print(next(print_num_iter))  # 2
print(next(print_num_iter))  # 3

# raises StopIteration
# print(next(print_num_iter))
print()

# iter() with sentinel parameter
class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__


my_iter = iter(DoubleIt(), 16)

for x in my_iter:
    print(x)

# python list()
"""the list() constructor rwturns a list in python"""
text = "Francis Royce"
text_list = list(text)
print(text_list)
print(type(text_list))

# empty list
print(list())
# string
name = 'Royce'
print(list(name))
# tuple
tuple1 = ('r', 'o', 'y', 'c', 'e')
print(list(tuple1))
# list
list1 = ['r', 'o', 'y', 'c', 'e']
print(list(list1))
# set
set1 = {'r', 'o', 'y', 'c', 'e'}
print(list(set1))
# dict
dict1 = {'r': 1, 'o': 2, 'y': 3, 'c': 4, 'e': 5}
print(list(dict1))

# create a list from an iterator object
class PowTwo:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.num = 0
        return self
    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result
pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)
print(list(pow_two_iter))

# python local()
# """returns a dict with all the local variable and symbols for the current program"""
print(locals())
class local:
    l = 50
    print('\nlocals() value inside class\n', locals())

def localsPresent():
    present = True
    print(present)
    locals()['present'] = False;
    print(present)
localsPresent()

# how len() works for custom objects
class Session:
    def __init__(self, number):
        self.number = 0
    def __len__(self):
        return self.number
s1 = Session(0)
print(len(s1))
s2 = Session(6)
print(len(s2))

print()
class Session:
    def __init__(self, number = 0):
        self.number = number
    def __len__(self):
        return self.number
s1 = Session()
print(len(s1))
s2 = Session(6)
print(len(s2))

print()
# python max()
""""returns the largest item in an iterable"""
num = [1, 4, 5, 3, 90, 100]
print(max(num))

# largest string in a list
languages = ['python', 'c programming', 'java', 'javascript']
print(max(languages))
print()
# max() in dict
# largest key
square = {2: 4, -3: 9, -1: 1, -2: 4}
print(max(square))

# uss of lambda
# key with largest value
key1 = max(square, key= lambda k: square[k])
print(key1)

# largest value
print(square[key1])

print()
# python min()
""""returns the smallest item in an iterable"""
num = [1, 4, 5, 3, 90, 100]
print(min(num))

# lowest string in a list
languages = ['python', 'c programming', 'java', 'javascript']
print(min(languages))
print()
# max() in dict
# lowest key
square = {2: 4, -3: 9, -1: 1, -2: 4}
print(min(square))

# uss of lambda
# key with lowest value
key1 = min(square, key=lambda k: square[k])
print(key1)

# lowest value
print(square[key1])
#
# python map()
"""map() function applies a given function to each element of an iterable(list, tuple etc) and returns an
iterator containing the results"""
num = [2, 4, 6, 8, 10]
def square(number):
    return number * number
squared_number_iterator = map(square, num)
squared_numbers =list(squared_number_iterator)
print(squared_numbers)
print()
def calculateSquare(n):
    return n*n
numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)
numbersSquared = set(result)
print(numbersSquared)

# lambda function with map()
n = (1, 2, 3, 4)
result = map(lambda x: x*x, n)
print(result)
nn = tuple(result)
print(nn)
print()
# passing multiple iterators to map() using lambda
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
print()
def Sum(numbers):
    return numbers + numbers
n = [1, 2, 3, 4, 5]
result = map(Sum, n)
print(list(result))

n = [1, 2, 3, 4, 5]
result = map(lambda x: x+x, n)
print(tuple(result))

# python next
"""next() function returns the next item from the iterator."""
mark = [65, 71, 68, 74, 61]
iterator_marks = iter(mark)
print(next(iterator_marks))
print(next(iterator_marks))
print(next(iterator_marks))
print(next(iterator_marks))
print(next(iterator_marks))

# passing default value to next()
random = [5, 6]
iterator = iter(random)
print(next(iterator, '-1'))
print(next(iterator, '-1'))
print(next(iterator, '-1'))

# python memoryview()
"""return a memory view object of the given argument"""
random_byte_array = bytearray('ABC', 'utf-8')
mv = memoryview(random_byte_array)
print(mv[0])
print(bytes(mv[0:2]))
print(list(mv[0:3]))
print()
# modify internal data using memory view
random_byte_array = bytearray('ABC', 'utf-8')
print(random_byte_array)
mv = memoryview(random_byte_array)
mv[1] = 90
print(random_byte_array)

# python object()
"""returns a featureless object which is a base for all classes"""
test = object()
print(test)
print(type(test))
print(dir(test))

# python oct()
"""takes an integer number and returns its octal representation"""
a =10
print(oct(a))

b = 90.99
c =int(b)
print(oct(c))
print(oct(0b101))
print(oct(0XA))
print()
class Person:
    age =23
    def __index__(self):
        return self.age
    def __init__(self):
        return None
person = Person()
print(oct(person))

class Person:
    age =23
    def __index__(self):
        return self.age
    def __int__(self):
        return self.age
person = Person()
print(oct(person))

# python ord()
"""returns an integer representing the Unicode character"""
character = 'P'
unicode_char = ord(character)
print(unicode_char)
print(ord('A'))
print()
# python pow(): computes power of a number
print(pow(3, 4))
print(pow(3, 4, 1))
# pow() with modulus
x = 7
y = 2
z = 5
print(x**y % z)
print(pow(x, y, z))
print()
# pytho print()
# print() with separator and end parameters
a = 6
print('a =', a)
print('a =', a, sep='00000', end='\n\n\n')
print('a =', a, sep='0', end='')

sourceFile = open('python.txt', 'w')
print('pretty cool, huh!', file=sourceFile)
sourceFile.close()

 # python property()
 # """returns the property attribute"""
 # create attribute with getter, setter, and deleter

class Person:
     def __init__(self, name):
         self._name = name
     def get_name(self):
        print('getting name')
        return self._name
     def set_name(self, value):
        print('setting name to ' + value)
        self._name = value
     def del_name(self):
        print('deleting name')
        del self._name
     name = property(get_name, set_name, del_name, 'name property')
person = Person('The name is: Francis')
print(person.name)
person.name = 'Royce'
del person.name

# using @property decorator
class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        print("Getting name")
        return self._name
    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value
    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name
person = Person("Francis Royce")
print('The name is:', person.name)
person.name = 'Royce'
del person.name

# python round()
"""returns a floating-point number rounded to the specified number of decimals."""
num =23.9
print(round(num))

print(round(10))
print(round(10.7))

# round a number to the given number of decimal places
print(round(2.945999, 2))

print(round(2.675, 2))
# for precision needed in the case of 2.675 use decimal module
from decimal import Decimal
num = 2.675
print(round(num, 2))
print(Decimal(num))
num = Decimal('2.675')
print(round(num, 2))
print(Decimal(round(num, 2)))
print()
# python setattr()
"""sets the value of the attribute of an object"""
class Student:
    mark: 99
    name = 'Royce'
student = Student()
setattr(student, 'name', 'Francis')
print(student.name)

setattr(student, 'mark', 100)
print(student.mark)
print()
class Person:
    name = "Francis"
p = Person()
print('before modification:', p.name)
setattr(p, 'name', 'Royce')
print('after modification:', p.name)

# when atrribute is not found in stattr(), it creates a new attribute
class Person:
    name = 'Francis Royce'
p = Person()
setattr(p, 'name', 'Okoronkwo Ifeanyi.I.')
print(p.name)

setattr(p, 'age', 28)
print(p.age)
print()
# python slice()
"""returns a slice object that is used to slice any sequence (string, tuple, list, range, or bite)"""
test = 'python programming'
sliced_test = slice(6)
print(test[sliced_test])

# create a slice object for slicing
result = slice(3)
print(result)

result = slice(1, 2, 3)
print(result)

# getting substring using slice object
string = 'python'
slice_object = slice(3)
print(string[slice_object])
slice_object = slice(1, 6, 2)
print(string[slice_object])

# using negative index
string = 'python'
slice_object = slice(-1, -4, -1)
print(string[slice_object])

# get sublist and sub-tuple
pyList = ['p', 'y', 't', 'h', 'o', 'n']
pyTuple = ('p', 'y', 't', 'h', 'o', 'n')
slice_object = slice(3)
print(pyList[slice_object])
print(pyTuple[slice_object])
slice_object = slice(1, 5, 2)
print(pyTuple[slice_object])

# python sorted()
"""sorts the elements of a given iterable in a specific oder (ascending or descending) and returns it as a list.
A list also has the Sort() method which performs the same way as sorted(). The difference is that the sort()
method doesn't return any value and changes the original list
"""
num = [1, 4, 3, 5, 2]
print(sorted(num))

num = [1, 4, 3, 5, 2]
num.sort()
print(num)

num = [1, 4, 3, 5, 2]
num.sort(reverse=True)
print(num)

# sort in descending order
num = [1, 4, 3, 5, 2]
print(sorted(num, reverse=True))

# sort the list using sorted() having a key function
def take_seconds(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
sorted_list = sorted(random, key=take_seconds)
print(sorted_list)

# sorted with multiple keys
participant_list =[
    ('Francis', 50, 18),
    ('Royce', 75, 12),
    ('Ifeanyi', 75, 20),
    ('Okoronkwo', 90, 22),
    ('Roy', 45, 12)
]
def sorter(item):
    error = 100 - item[1]
    age = item[2]
    return (error, age)
sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)

# using lambda
participant_list =[
    ('Francis', 50, 18),
    ('Royce', 75, 12),
    ('Ifeanyi', 75, 20),
    ('Okoronkwo', 90, 22),
    ('Roy', 45, 12)
]
sorted_list = sorted(participant_list, key=lambda item: (100 - item[1], item[2]))
print(sorted_list)
print()
# python sum()
"""adds the items of an iterable and returns the sum"""
marks = [1, 2, 3, 4, 5, 6]
print(sum(marks))

num = sum(marks, 10)
print(num)
print()
# using math.fsum(iterable) for float
import math
num = [1.0, 2.4, 3.5, 7.9]
total = math.fsum(num)
print(total)
print(round(total))

# python vars()
"""returns the __dict__(dictionary mapping) attribute of the given object."""
print(vars(list))
print(vars())

# vars with custom object
class Fruit:
    def __init__(self, apple =5, banana =10):
        self.apple = apple
        self.banana = banana
eat = Fruit()
print(vars(eat))

# python zip()
"""takes iterables (can be zero or more), aggregates them in a tuple, and return it."""
languages = ['java', 'python', 'javaScript']
versions = [14, 3, 6]
result = zip(languages, versions)
print(result)
print(list(result))

num = [1, 2, 3, 4]
string = ['one', 'two', 'three', 'four']
result = zip()
print(list(result))
result = zip(string, num)
print(set(result))
print()

num = [1, 2, 3, 4]
string = ['one', 'two', 'three', 'four']
string2 = ['ONE', 'TWO', 'THREE', 'FOUR']
result = zip()
print(list(result))
result = zip(string, num, string2)
print(set(result))

# unzipping the value usung zip
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
print(list(result))

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)
c, v = zip(*result_list)
print('c =', c)
print('v =', v)

# python super()
"""returns a proxy object (temporary object of the superclass) that allows us to access methods of the base.
super(): allows us to avoid using the base class name explicitly
working with multiple inheritance"""
class Animal(object):
    def __init__(self, animal_type):
        print('Animal Type:', animal_type)
class Mammal(Animal):
    def __init__(self):
        super().__init__('Mammal')
        print('Mammals give birth directly')
dog = Mammal()
print()
# super() with single inheritance
class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')
d1 = Dog()

super() with multiple inheritance
class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');
class Mammal(Animal):
    def __init__(self, mamalName):
        print(mamalName, 'is a warm-blooded animal.')
        super().__init__(mamalName)
class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)
class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)
class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')
d = Dog()
print('')
bat = NonMarineMammal('Bat')

# python dictionary data type
""""it is an ordered collection of items. it stores elements in key/value pairs."""
capital_city = {'Abia': 'Umuahia', 'Delta': "Asaba", 'Ebonyi': 'Abakiliki'}
print(capital_city)
print()

# access dictionary values using keys
capital_city = {'Abia': 'Umuahia', 'Delta': "Asaba", 'Ebonyi': 'Abakiliki'}
print(capital_city['Abia'])
print(capital_city['Delta'])

numbers = {1: 'one', 2: 'two', 3: 'three'}
print(numbers)
print(numbers[1])

# add element to a dictionary
capital_city = {'Abia': 'Umuahia', 'Delta': "Asaba", 'Ebonyi': 'Abakiliki'}
print('initial dictionary:', capital_city)
capital_city['Adamawa'] = 'Yola'
print('updated dictionary:', capital_city)
print()


# change value of dictionary
student_id = {111: 'Royce', 112: 'Francis', 113: 'Ifeanyi'}
print(student_id)
student_id[113] = 'Okoronkwo'
print(student_id)
print()
# removing elements from dictionary: we use del statement
student_id = {111: 'Royce', 112: 'Francis', 113: 'Ifeanyi'}
del student_id[113]
print(student_id)

# dictionary membership
squares = {1: 1, 3: 9, 5: 25, 7:49, 9:81}
print(1 in squares)
print(2 in squares)
print(49 in squares)

# iterating through a dictionary keys
squares = {1: 1, 3: 9, 5: 25, 7:49, 9:81}
for i in squares:
    print(i)
print()
# iterating through a dictionary value
squares = {1: 1, 3: 9, 5: 25, 7:49, 9:81}
for i in squares:
    print(squares[i])
print()
# python dictionary clear()
squares = {1: 1, 3: 9, 5: 25, 7:49, 9:81}
squares.clear()
print(squares)

# python dictionary copy()
squares = {1: 1, 3: 9, 5: 25, 7:49, 9:81}
copied_squares = squares.copy()
print('original squares:', squares)
print('copied squares:', copied_squares)

# using operator to copy (=)
squares = {1: 1, 3: 9, 5: 25, 7:49, 9:81}
new = squares
print(new)
print()
# shallow copy, you can remove the new list and it will not affect the original list
squares = {1: 1, 3: 9, 5: 25, 7:49, 9:81}
new = squares.copy()
print('new:', new)
new.clear()
print('new after clear:', new)
print('original:', squares)

# python dictionary fromkeys()
"""creates a dictionary from the given sequence of keys and values"""
alpha = {'a', 'b', 'c', 'd'}
number = 1
dictionary = dict.fromkeys(alpha, number)
print(dictionary)
print()
# fromkeys() without value
alpha = {'a', 'b', 'c', 'd'}
number = dict.fromkeys(alpha)
print(number)

# fromkeys() to create a dictionary from mutable object
alpha = {'a', 'b', 'c', 'd'}
value = [1]
number = dict.fromkeys(alpha, value)
print(number)
value.append(2)
print(number)
print()

# dictionary comprehension fro mutable objects
"""we can use dictionary comprehension and prevent updating the dictionary when the mutable object
(list, dictionary etc) is updated"""
alpha = {'a', 'b', 'c', 'd'}
value = [1]
number = {key : list(value) for key in alpha}
print(number)
value.append(2)
print(number)
print()

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

# using dictionary comprehension of the above program
square_dict = {num : num*num for  num in range(1, 11)}
print(square_dict)
print()

old_list = {'milk': 1.03, 'bread': 2.23, 'coffee': 2.5}
dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_list.items()}
print(new_price)

# If condition\l dictionary comprehension
original_dict = {'Royce': 38, 'Francis': 48, 'Ifeanyi': 57, 'Okoronkwo': 33 }
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict) # only the items with even value added cos of if clause
print()

# multiple conditional dictionary comprehension
original_dict = {'Royce': 38, 'Francis': 48, 'Ifeanyi': 57, 'Okoronkwo': 33 }
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict) # only the items with an odd value of less than 40 have been added
print()

# if - else conditional dictionary comprehension
original_dict = {'Royce': 38, 'Francis': 48, 'Ifeanyi': 57, 'Okoronkwo': 33 }
new_dict = {k: ('old' if v > 40 else 'young')
            for (k, v) in original_dict.items()}
print(new_dict)
print()

# nested dictionary comprehension
"""we can add dictionary comprehension to dictionary comprehension themselves to create nested dcitionaries"""
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)
print('\n')
# the above code will eb equivalent
dictionary = dict()
for k1 in range (2, 5):
    dictionary[k1] = {k2: k1 * k2 for k2 in range(1, 6)}
print(dictionary)
print('\n')

# it can further be broken down as:
dictionary = dict()
for k1 in range(2, 5):
    dictionary[k1] = dict()
    for k2 in  range (1, 6):
        dictionary[k1][k2] = k1*k2
print(dictionary)
#
# python dictionary get()
"""returns the value for the specified key if the key is in the dictionary"""
marks = {'maths': 90, 'physics': 88}
print(marks.get('physics'))

person = {'name': 'Royce', 'age': 28}
print('name:', person.get('name'))
print('age:', person.get('age'))
print('salary:', person.get('salary'))
print('salary:', person.get('salary', 0.0))

# python dictionary items()
"""returns a view object that displays a list of dictionary's(key, value) tuple pairs"""
marks = {'maths': 90, 'physics': 88}
print(marks.items())

marks = {'maths': 90, 'physics': 88}
items = marks.items()
print('original items:', items)
del[marks['physics']]
print('updated items:', items)

# python dictionary keys()
""""extracts the keys of the dictionary and returns the list of keyts as a view object"""
marks = {1: 'one', 2: 'two', 3: 'three'}
dict_keys = marks.keys()
print(dict_keys)

# python dictionary update
marks = {1: 'one', 2: 'two', 3: 'three'}
dict_keys = marks.keys()
print('before update:', dict_keys)
marks.update({4: 'four'})
print('after update:', dict_keys)

# python dictionary popitem()
"""removes and returns the last element (key, value) pair inserted into the dictionary"""
marks = {1: 'one', 2: 'two', 3: 'three'}
dict_keys = marks.popitem()
print(marks)
print(dict_keys)
marks[4] = 'four'
dict_keys = marks.popitem()
print(marks)
print(dict_keys)

# python dictionary setdefault()
"""returns the value of a key(if the key is in dictionary), if not, it inserts key with a value to the dictionary"""
marks = {1: 'one', 2: 'two', 3: 'three'}
one_1 = marks.setdefault(1)
print(marks)
print(one_1)

# if the key is not in the dictionary
marks = {1: 'one', 2: 'two', 3: 'three'}
dict_keys = marks.setdefault(5)
print(marks)
print(dict_keys)
dict_keys = marks.setdefault(4, 'four')
print(marks)
print(dict_keys)

# python dikctionary pop()
"""removes and returns an element from a dictionary having the given key"""
marks = {1: 'one', 2: 'two', 3: 'three'}
elem = marks.pop(1)
print(elem)
print(marks)

# pop an element not present in the dictionary
marks = {1: 'one', 2: 'two', 3: 'three'}
# elem = marks.pop(4)
# print(marks)  Error
# print(elem)
#
# pop element not present from the dictionary, provided a default value
marks = {1: 'one', 2: 'two', 3: 'three'}
elem = marks.pop(4, 5)
print(elem)
print(marks)

# python dictionary values()
"""returns a view object that displays a list of all the values in the dictionary"""
marks = {1: 'one', 2: 'two', 3: 'three'}
print(marks.values())
print()
marks = {1: 'one', 2: 'two', 3: 'three'}
elem = marks.values()
print(marks)
print(elem)
del [marks[1]]
print(elem)
print(marks)

# python dictionary update
"""updates the dictionary with the elements from another dictionary object"""
marks = {1: 'one', 2: 'two', 3: 'three'}
elem = {4: 'four', 5: 'five'}
marks.update(elem)
print(marks)
print(elem)
print(marks, elem)

# update() when tuple is passed
dictionary = {'x': 2}
dictionary.update([('y', 3), ('z', 0)])
print(dictionary)

python type conversion
implicit = automatic
explicit = manual
python implicit type conversion (integer to float)
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
print('value:', new_number)
print('Data type:', type(new_number))

# explicit type conversion
"users convert data type of an object to required data type"
# addition of string and integer using explicit conversion
number_string = '12'
num_integer = 23
print('data type of num_string before type casting:', type(number_string))
number_string = int(number_string)
print('data type of num_string before type casting:', type(number_string))
num_sum = num_integer + number_string
print('sum:', num_sum)
print('data type of num_sum:', type(num_sum))
print('\n')

# python basic input and output (I\O)
"ways to  display output to users and take input from users in python"
# python print statement
print('Good morning!')
print('it is a rainy day')
# python print with end parameter
print('Good morning!', end=' ')
print('it is a rainy day')

# python print with sep parameter
print('new year', 2023, 'see you soon', sep='. ')

# output formatting
"sometimes we will like to format our output to make it look attractive using (str.format())"
x = 5
y = 10
print('the value of x is {} and y is {}'.format(x, y))

# python user Ipnut
num = input('Enter a number:')
print('You Entered:', num)
print('Data type of num:', type(num))

# converting to integer
num = int(input('Enter a number:'))
print('You Entered:', num)
print('Data type of num:', type(num))

# python operators (types)
print(4 + 5)
# python Arithmetic operator
a = 9
b = 6
print('sum:', a + b)
print(b - a)
print(a -b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print()
# python assignment operators
a = 10
b = 5
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a //= b
print(a)
a %= b
print(a)
a **= b
print(a)
print()
# python comparison operators
a = 10
b = 5
print(a > b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print()

# python logical operators
a = 10
b = 5
print((a > 2) and (b >= 5))
print((a > 2) or (b >= 5))
print((a > 2), not (b >= 5))
print()

print(True and False)
print(True and True)
print(True or False)
print(not True)
print(not False)
print()
# python bitwise operators
a = 5
b = 3
print(a & b)
print(a | b)
print(a, ~ b)
print(a ^ b)
print(a >> b)
print(a << b)
print()
# python identity operators in python
a = 5
b = 5
c = 'hello'
d = 'hello'
e = [1, 2, 3]
f = [1, 2, 3]
print(a is not b)
print(c is d)
print(e is f)  # equal not identical for a list
print()
# membership operator
"""note, in a dictionary we can only test for the presence of key and not the value"""
a = 'hello world'
b = {1: 'one', 2: 'one'}
print('h' in a)
print('hello' in a)
print('Hello' in a)
print(1 in b)
print(2 in b)
print(3 in b)
print()
# Python Namespace and Scope
# Scope and Namespace in Python
# global_var is in the global namespace
global_var = 10

def outer_function():
    #  outer_var is in the local namespace
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace
        inner_var = 30

        print(inner_var)

    print(outer_var)

    inner_function()

# print the value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()
print()
# Use of global Keyword in Python
# define global variable
global_var = 10

def my_function():
    # define local variable
    local_var = 20

    # modify global variable value
    global global_var
    global_var = 30

# print global variable value
print(global_var)

# call the function and modify the global variable
my_function()

# print the modified value of the global variable
print(global_var)

# python if...else statement
number = 10
if number > 0:
    print('Number is positive')
print('The if statement is easy')
print()
number = -10
if number > 0:
    print('Number is positive')
print('The if statement is easy')

# if else statement
number = 10
if number > 0:
    print('Number is positive')
else:
    print('number is negative')
print('The if statement is easy')
print()
number = -10
if number > 0:
    print('Number is positive')
else:
    print('Number is negative')
print('The if statement is easy')

# making a choice more than two alternative
# python if...elif..else statement
number = 0
if number > 0:
    print('Positive number')
elif number == 0:
    print('zero')
else:
    print('Negative number')
print('The statement is always executed')
print()
number = 1
if number > 0:
    print('Positive number')
elif number == 0:
    print('zero')
else:
    print('Negative number')
print('The statement is always executed')
print()
number = -1
if number > 0:
    print('Positive number')
elif number == 0:
    print('zero')
else:
    print('Negative number')
print('The statement is always executed')
print()
# python nested if statements
"""we can use if statement inside an if statement."""
number = 5
if (number >= 0):
    if number == 0:
        print('Number is 0')
    else:
        print('Number is positive')
else:
    print('number is negative')

# python for loop
"""lops are used to repeat a block of code:
two type of loop;
1 - for loop
2 - while loop"""

# loop for python list
languages = ['java', 'python', 'javascript']
for language in languages:
    print(language)

languages = ['java', 'python', 'javascript']
for language in languages:
    print(languages)
print()
# python for loop with python range
values = range(5)
for num in values:
    print(num)
    print()
values = range(5)
for num in values:
    print(values)
print()
# python for loop with else
digits = [0, 1, 5]
for digit in digits:
    print(digit)
print()

digits = [0, 1, 5]
for digit in digits:
    print(digit)
    print(digits)

digits = [0, 1, 5]
for digit in digits:
    print(digit)
else:
    print('No item left')

python while loop
"""while loop is used to run a block code until a certain condition is met"""
i = 1
n = 5
while i <= n:
    print(i)
    i = i + 1
# program to calculate the sum of numbers until the user enters zero
total = 0
number = int(input('Enter a number: '))
while number != 0:
    total += number
    number = int(input('Enter a number: '))
print('total =', total)

# same code as the one above
sum = 0
while True:
    user_input = input("Enter a number (type 'calculate to sum up): ")
    if user_input == 'calculate':
        break
    try:
        number = int(user_input)
        sum += number
    except ValueError:
        print('Invalid input, try again.')
print('sum of numbers:', sum)

# infinite while loop in python
"""if the condition of a loop alsways True, the loop runs for infinite times
(until the memory is full)."""

age = 24
while age > 18:
    # print('You can vote') # you can stop the code from running by using break

# python while loop with else
counter = 0
while counter < 3:
    print('inside loop')
    counter = counter + 1
else:
    print('inside else')
print()
counter = 0
while counter < 3:
    if counter == 1:
        break
    print('inside loop')
    counter = counter + 1
else:
    print('inside else')

# python break statement with for loop
for i in range(5):
    if i == 3:
        break
    print(i)

# python break statement with while loop
i = 1
while i <= 10:
    print('6 * ', (i), '=', 6 * i)
    if i >= 5:
        break
    i = i + 1

# python continue statement
"""the continue statement is used to skip the current iteration of the loop
and the control flow of the program goes to the next iteration"""
# python continue statement with for loop
for i in range(5):
    if i == 3:
        continue
    print(i)
print()
# python continue statement with while loop
number = 0
while number < 10:
    number += 1
    if (number % 2) == 0:
        continue
    print(number)
# in the code above when the number is even, the continue statement skips the current iteration

# python pass statement
"""pass statement is a null statement which can be used as a placeholder for future code"""
# using pass with conditional statement
n = 10
if n > 10:
    pass
print('hello')

# if we didn't use pass in the above code
# n = 10
# if n > 10:
# print('hello') we get an error message
"""the difference between a comment and a pass statement in python is that while the interpreter ignores a
comment entirely, pass is not ignored"""

# python functions
"""function is a block of code that performs a specific task"""
# types of function
"""1 - standard library functions : built-in functions in python that are available to use.
2- user-defined functions: we can create our own functions based on our requirement"""
def greet():
    print('hello')
"""above we have created a function name greet() but the function doesn't have any arguments
and doesn't return any value."""

# calling a function
"""to use a function we need to call it"""
def greet():
    print('hello')
greet()
print('outside function')

# function argument: a function can have argument
"""argument: it is a value accepted by a function"""
def add_number(num1, num2):
    sum = num1 + num2
    print('sum:', sum)
add_number(10, 10)

# the return statement in python
"""a python function may or may not return a value. if we want our function to return some values to a function
call, we use the return statement. return statement also denotes that the function has ended. any code after return
is not executed"""
def find_square(num):
    result =  num * num
    print(result)
    return result
find_square(5)
#  2
def find_square(num):
    result =  num * num
    return result
square = find_square(5)
print(square)

# python library function: built-in use directly in our program
import math
square_root = math.sqrt(4)
print('square root of 4 =', square_root)
power = pow(2, 3)
print('2 to the power 3 is:', power)
print()
# benefits of using a function
# 1- code reusable
def get_square(num):
    sum = num * num
    print('square of i =', sum)
    return sum
for i in  [1, 2, 3]:
    get_square(i)
print()
# or
def get_square(num):
    return num * num
for i in [1, 2, 3]:
    result = get_square(i)
    print('square of i =', result)
# 2 - code readability
#
# python function argument
"""in computer programming, an argument is a value that is accepted by a function"""
def add_number(a, b):
    sum = a + b
    print('sum:', sum)
    return sum
add_number(1, 2)
print()

def add_number(a, b):
    sum = a + b
    print('sum:', sum)
add_number(1, 2)

def add_number(num):
    sum = num + num
    print('sum:', sum)
add_number(int(2.5))

def add_number(num):
    sum = num + num
    print('sum:', sum)
    return sum
add_number(int(2.5))
print()
# argument with default values by the use of (=) operator
def add_number(a = 7, b = 9):
    sum = a + b
    print('sum:', sum)
add_number(2, 3)
add_number(a=2)
add_number()
print()
# python keyword argument
"""here, argument is assigned based on the name of the arguments"""
def display_info(first_name, last_name):
    print(first_name, last_name)
display_info(first_name='Francis', last_name="Royce")

def display_info(first_name, last_name):
    names = (first_name, last_name)
    print(first_name, last_name)
    return names
display_info(first_name='Francis', last_name="Royce")

def display_info(first_name, last_name):
    print('First name:', first_name)
    print("Last name:", last_name)
display_info(first_name='Francis', last_name="Royce")
print()
# python function with arbitrary arguments (*)
"""sometimes, we do not know in advance the number of arguments that will be passed into a function.
to handle this situation, we can use arbitrary arguments in python before parameter name"""
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
        print('sum:', result)
find_sum(1, 2, 3)
find_sum(4, 9)

# python recursion
"""A function that calls itself; Recursion is the process of defining something in terms of itself"""
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print('The factorial of', num, 'is', factorial(num))

# python lambda/anonymous function
"""in python lambda is a special type of function without function name"""
# lambda: print('hello world')

# python lambda function declaration
"""we use lambda instead of def to create lambda function"""
greet = lambda : print('hello world')
greet()

# python lambda function with an argument

greet_user = lambda name: print('Hey dear', name)
greet_user('Francis Royce')

# python variable scope: local, nonlocal, and global variables

# python local variable
"""when we declare variables inside a function, these variables will have a local scope(within the function)
.we cannot access them outside the function"""
def greet():
    # local variable
    message = 'hello'
    print('local', message)
greet()
# print(message) error cos is outside the function
print()
# python global variable
"""A variable declared outside of the function or in global scope is known as a global variable
this means a global variable can be accessed inside or outside of the function"""
message = 'hello'
def greet():
    # declare local variable
    print('local', message)
greet()
# declare global variable
print('global', message)
print()
# python Nonlocal variables (nonlocal)
"""used in nested functions whose local scope is not defined. this means that the variable can be neither in
the local nor the global scope. we use nonlocal keyword to create the variable"""

def outer():
    message = 'local'
    def inner():
        nonlocal message
        message = 'nonlocal'
        print('inner:', message)
    inner()
    print('outer:', message)
outer()
print()

# python global keyword
"""the global keyword allows us to modify the variable outside of the current scope.
it is used to create global variable and make changes to the variable in a local context"""

# access and modify python global variable
c = 1
def add():
    print(c)
add()

c =1
def add():
    c = c + 2
    #  we try to modify the global variable from inside a function gives error
    print(c)
# add()

# changing a global variable from inside a function using global keyword
c = 1
def add():
    global c
    c = c + 2
    print(c)
add()

# global i9n nested function: we can also use the global keyword in nested function
def outer_function():
    num = 20
    def inner_function():
        global num
        num = 25
    print('before calling inner function:', num)
    inner_function()
    print('after calling inner function:', num)
outer_function()
print('outside both function:', num)

# python modules
"""module: it is a file that that contains code to perform a specific task.
A  module may contain variables, functions, classes etc.
as our program grows bigger, it may contain many lines of code. instead of putting everything
in a single file, we can use module to separate files as per their functionality"""
# here, example module is a self created module saved at the directory
import example
print(example.add(9, 10))

# import standard library modules
"""the python standard library contains over 200 modules. we can import a module according to our needs"""
import math
print('the value of pi is:', math.pi)

# python import with renaming
import math as  m
print(m.pi)

# python from...import statement
from math import pi
print(pi)

# import all names (module)
"""we can import all the names(definition) from a module using the following construct:  we use (*)"""
from math import *
print(pi)
print(sqrt(7))

# the dir() built-in function
"""we can use the dir() function gto list all the function names in a module"""
import example
print(dir(example))
print(example.__name__)
print(example.__loader__)
print(example.__file__)
print(example.__doc__)
print(example.__spec__)
print(example.__cached__)
print(example.__builtins__)
print(example.__package__)

# # python package
"""a package is a container that contains various functions to perform specific tasks
example, the math package includes the sqrt() function to perform the square root of a  number.
while working on a big projects, we have to deal with a large amount of code, and writing everything
togetrher in the same file will make our code look messy. instead, we can separate our code
into multiple files by keeping the related code together in packages

Note, a directory must contain a file name (__init__.py)in order for python to consider it as a package.
this file can be left empty but we generally place the initialization code for that package in this file"""

# importing module from a package
"""we can import modules from a package using dot(.) operator"""

# python file I/Opython file operation
# opening files, we use open()
file1 = open('text.txt', 'r')
print(file1.read())
print()

file1 = open('text.txt', 'r')
read_content = file1.read()
print(read_content)
file1.close()
print()

# closing a file, it will free up the file
file2 = open('python.txt')
read_content = file2.read()
print(read_content)
file2.close()

# exception handling in files
"""if an exception occurs when we are performing some operation with the file, the code exits
without closing the files. A safer way is to use a try...finally block"""
try:
    file1 = open('python.txt', 'r')
    read_content = file1.read()
    print(read_content)
finally:
    file1.close()
print()
# use of with...open syntax
"""we can use the with...open syntax to automatically close the file, since we don't have to
about closing the file, make a habit of using with...open syntax"""
with open('python.txt', 'r') as file1:
    read_content = file1.read()
    print(file1)
    print(read_content)

# writing to files in python
# two things to remember when writing to files
"""1- if we try to open a file that doesn't exist, a new file is created
2- if a file already exists, its content is erased, and new content is added to the file"""

with open('test2.txt', 'w') as file3:
    file3.write('python is fun\n')
    file3.write('python for beginners')
    # read_content = file3.read()
    # print(read_content) # error not readable cos of 'w'
# to make it readeable
with open('test2.txt', 'r') as file3:
    read_content = file3.read()
    print(read_content)

with open('test2.txt', 'r') as file3:
    read_content = file3.read()
    print(read_content)
    file3.readline()

# python directory and files management
"""a directory is a collection of files and subdirectories.
A directory inside a directory is known as a subdirectory
python has the os module useful methods to work with directories (and files as well)"""
# get current directory in python using os module and getcwd()
"""this method returns the current working directory in the form of a string"""
import os
print(os.getcwd())

# changing the directory in python
"""we can change the working directory by using the chdir() method.
the new path that we want to change into must be supplied as a string to this method.
we can use both the forward-/ and backword-\ to separate the path elements"""

# import os
# os.chdir('')
# print(os.getcwd())
# list directories and files in python
import os
print(os.getcwd())
print(os.listdir())

# making a new directory in python mkdir()
import os
new_directory = 'example_directory'
try:
    os.mkdir(new_directory)
except OSError:
    print('creation of the directory %s',  new_directory)
else:
    print('successfully created the directory %s ', new_directory)

# Renaming a Directory or a File
"""The rename() method can rename a directory or a file.

For renaming any directory or file, rename() takes in two basic arguments:

the old name as the first argument
the new name as the second argument."""

import os
print(os.listdir())
os.rename('FrancisRoyce', 'masterfrancis')
print(os.listdir())

# removing directory or file in python
"""we can use the remove() method or rmdir() method to remove a file or directory"""
import os
# print(os.remove('python.txt'))
# print(os.remove('text.txt'))

# we can use rmdir() to remove an empty directory
import os
# print(os.rmdir('example_directory'))

# in order to remove non-empty directory, we can use rmtreet() method inside the shutil module
import shutil
# shutil.rmtree('masterfrancis')

# python Exceptions
"""an exception is an unexpected event that occurs during program execution"""
divide_by_zero = 7/0
print(divide_by_zero)

# python built-in exceptions
print(dir(locals()['__builtins__']))

# python exception handling
# try..except..finally

# python try..except block
"""this is used to handle exception.
note that except block can not be used without try block"""

try:
    numerator = 110
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print('Error: Denominator cannot be 0')

# catching specific exceptions in python
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("denominator cannot be 0.")
except IndexError:
    print('Index out of bound')

# python try with else clause
"""in some situations, we might want to run a certain block of code if the code of block inside 'try' runs
without any errors. for these case you can use the optional else keyword with 'try' statement"""
try:
    num = int(input('Enter a number: '))
    assert num % 2 == 0
except:
    print('Not an even number')
else:
    reciprocal = 1/num
    print(reciprocal)

# python try...finally
"""the finally block is always excuted no matter whether there is an exception or not
and it is optional, there can be only one final block"""
try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print('Error: Denominator cannot be 0.')
finally:
    print('This is finally block')

# python custom exception

# defining custom exception
"""we can define custom exceptions by creating a new class that is derived from the built-in
exception class"""

# python user-Defined exception
class InvalidAgeException(Exception):
    'raise when the input value is less than 18'
    pass
number = 18
try:
    input_num = int(input('Enter a number: '))
    if input_num < number:
        raise InvalidAgeException
    else:
        print('Eligible to vote')
except InvalidAgeException:
    print('Exception occured: Invalid Age')

customizing Exception classes
class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message = 'salary is not (5000, 15000) range'):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
salary = int(input('Enter salary amount: '))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

# python object oriented programmming
"""An object is any entity that has attributes and behaviour.
example: parrot
attribute: name, ager, color etc
behaviour: dancing, singing, etc"""

# python class and object
class parrot:
    name = ''
    age = 0
parrot1 = parrot()
parrot1.name = 'Royce'
parrot1.age = 10

parrot2 = parrot()
parrot2.name = 'Francis'
parrot2.age = 20
print(f'{parrot1.name} is {parrot1.age} years old ')
print(f'{parrot2.name} is {parrot2.age} years old ')
print()
# python Inheritance
"""inheritance is a way of creating a new class for using details of an existing class without modifying it.
the newly formed class is a derived class (or child class). similarly, the existing class is a base class or
parent class"""

# use of inheritance in python
class Animal:
    def eat(self):
        print('I can eat!')
    def sleep(self):
        print('I can sleep')
 # derived class
class dog(Animal):
    def bark(self):
        print('I can bark! woof woof!!')
dog1 = dog()
dog1.eat()
dog1.sleep()
dog1.bark()

# python Encapsulation
"""it is one of the keys features of object-oriented  programming. it refers to the bundling of attributes and
methods inside a single, it helps in achieving data hiding"""
# in python, we denote private attributes using underscore as the prefix i.e single(_) or double (__)
print()
class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print('selling price: {}'.format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()
print()
# polymorphism
"""polymorphism is another important concept of OOP. it simply means more than one.
that is, the same entity(method or operator or object) can perform different operations
in different scenarios"""
class Polygon:
    def render(self):
        print('rendering polygon.....')
class Square(Polygon):
    def render(self):
        print('rendering square....')
class Circle(Polygon):
    def render(self):
        print('rendering circle....')
s1 = Square()
s1.render()
c1 = Circle()
c1.render()
p1 = Polygon()
p1.render()

# python objects and classes
"""a class is considered as a blueprint of objects. we can think of the class as a sketch (prototype)
of a house. it contains all the details about the floors, doors, windows etc.Based on these
descriptions we build the house. house is the object, since many houses can be made from the description,
we can create objects from a class"""
class bike:
    name = ''
    gear = 0
bike1 = bike()
"""we created a class named: bike
attributes: name, and gear
object: bike1"""

# access class attributes using objects.
"""we use dot(.) notation to access the attribute of the class"""
bike1.name = 'Honda'
bike1.gear
pass

# python class and objectike
class Bike:
    name = ''
    gear = 0
Bike1 = Bike()
Bike1.name = 'Honda'
Bike1.gear = 11
print(f'name: {Bike1.name}, Gears: {Bike1.gear}')
print()
# create multiple objects of python class
class Employee:
    employee_id = 0
employee1 = Employee()
employee2 = Employee()
employee1.employee_id = 1001
employee2.employee_id = 1002
print(f'Employee ID: {employee1.employee_id}')
print(f'Employee ID: {employee2.employee_id}')

# python methods
"""we can also define a function inside a python class.
A python function defined inside a class is called a method"""
print()
class Room:
    length = 0.0
    breadth = 0.0
    def Calculate_area(self):
        print('Area of Room = ', self.length * self.breadth)
study_room = Room()
study_room.length = 43.9
study_room.breadth = 30.9
study_room.Calculate_area()

# python Inheritance
"""inheritance allows us to create a new class from an existing class"""
# # python inheritance syntax
# class super_class:
# class sub_class (super_class):
print()
# python inheritance
class Animal:
    name = ''
    def eat(self):
        print('i can eat')
class dog(Animal):
    def display(self):
        print('my name is', self.name)
labrator = dog()
labrator.name = 'Bright'
labrator.eat()
labrator.display()

# inheritance in python
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input('Enter side ' + str(i + 1) + ' : ')) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print('side', i+1, 'is', self.sides[i])
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
above, the object of the subclass can access the method of the superclass

# method overriding in python inheritance
"""in this case, the method in the overrides the method in the superclass. The concept
is known as overridding """
class Animal:
    name = ''
    def eat(self):
        print('i can eat')
class Dog(Animal):
    def eat(self):
        print('i like to eat bones')
labrador = Dog()
labrador.eat()
print()
# The super() method in python inheritance to access the superclass
class Animal:
    name = ''
    def eat(self):
        print('i can eat')
class Dog(Animal):
    def eat(self):
        super().eat()
        print('i like to eat bones')
labrador = Dog()
labrador.eat()
print()
# python multiple inheritance
class Mammal:
    def mammal_info(self):
        print('mammals can give birth directly')
class WingedAnimal:
    def winged_animal_info(self):
        print('Winged animals can flap')
class Bat(Mammal, WingedAnimal):
    pass
b1 = Bat()
b1.mammal_info()
b1.winged_animal_info()
print()
# python multiple inheritance
class Superclass:
    def super_method(self):
        print('super class method called')
class Derivedclass1(Superclass):
    def derived_method(self):
        print('derived class method called')
class Derivedclass2(Derivedclass1):
    def derived2_method(self):
        print('derived class 2 method called')
d2 = Derivedclass2()
d2.super_method()
d2.derived_method()
d2.derived2_method()

# python Resolution order(MRO)
"""if two superclass have the same method name and the derived class calls that method,
python uses the MRO to search for the right method to call"""
class SuperClass1:
    def info(self):
        print('super class 1 method called')
class SuperClass2:
    def info(self):
        print('super class 2 method called')
class Derived(SuperClass1, SuperClass2):
    pass
d1 = Derived()
d1.info()

# python operator overloading
""""we can change the way operators work for user-defined types.This feature in python allows
the same operator to have different meaning according to the context, we use special functions for the operation
(double underscore prefix and suffix = special function)"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return ('{0}, {1}'.format(self.x, self.y))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)
print()
# overloading comparison operators
"""python does not limit operator overloading to arithmetic operators only"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # overload < operator
    def __lt__(self, other):
        return self.age < other.age
p1 = Person('Francis', 20)
p2 = Person('Royce', 30)
print(p1 < p2)
print(p2 < p1)
print()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # overload < operator
    def __ge__(self, other):
        return self.age >= other.age
p1 = Person('Francis', 20)
p2 = Person('Royce', 30)
print(p1 <= p2)
print(p2 >= p1)

# python iterator
"""iterator methods that iterate collection like list, tuples etc. using an iterator method, we can loop through
an object and return its elements. Technically, a python iterator object must implement two special method,
__iter__() and __next__, collectively called the iterator protocol"""

# iterating through an iterator
myList = [1, 2, 3, 4]
iterator = iter(myList)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print()
# using for loop

myList = [1, 2, 3, 4]
for element in myList:
    print(element)
print()
# working of for loop for iterator
myList = [1, 2, 3, 4]
iterator = iter(myList)
for element in iterator:
    print(element)
print()
# Building custom iterator using special function
class PowTwo:
    def __init__(self, max=0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
numbers = PowTwo(3)
i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print()

# we can also use for loop
for i in PowTwo(3):
    print(i)
print()
# python infinite iterators
"""infinite iterator is an iterator that never ends, meaning that it will continue to
produce elements indefinitely, we use the count() function from the itertools module"""

from itertools import count
infinte_iterator = count(1)
for i in range(5):
    print(next(infinte_iterator))

# python Generators
"""a generator is a function that returns an iterator that produced a sequence of value
when iterated over. Generators are useful when we want to produce a large sequence of values,
but we don't want to store all of them in memory at once"""

# create python generator
"""similar to defining a normal function, we can define a generator function using def
keyword, but instead of the return statement we use the yield statement"""

# python generator
def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1
for value in my_generator(3):
    print(value)

print()
# python generator expresssion
square_generator = (i * i for i in range(5))
for i in square_generator:
    print(i)
print()

# use of python generator
# 1- easy to implement
class PowTwo:
    def __init__(self, max=0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
"""the above program was lengthy and confusing. now, lets do the same using a genrator function"""

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n +=1
for n in PowTwoGen(3):
    print(n)
print()
# even number using generator (infinte stream)
def even_numbers(n):
    n = 0
    while True:
        yield n
        n += 2
        break #remove break to run
for n in  even_numbers(10):
    print(n)
print()
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci()
for i in  range(10):
    print(next(fib))

print()
# pipelining generators
"""multiple generator can be used to pipeline a series of operations"""
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
def square(nums):
    for num in nums:
        yield num**2
print(sum(square(fibonacci_numbers(10))))
print()
def even_squares(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num**2
def odd_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num
def pipeline(numbers):
    return list(even_squares(odd_numbers(numbers)))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = pipeline(numbers)
print(result)

Python closures
""""python closure is a nested function that allows us to access variables of the outer
function even after the outer function is closed. lets revise nested function in python"""
# nested function in python
def greet(name):
    def display_name():
        print('Hi', name)
    display_name()
greet('Francis Royce')

# python closure
def greet():
    # variable defined outside the inner function
    name = "Francis Royce"
    # return a nested anonymous function
    return lambda: "Hi " + name
# call the outer function
message = greet()
# call the inner function
print(message())

# Print odd Numbers using Golang closure
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func
odd = calculate()
print(odd())
print(odd())
print(odd())
print()
odd2 = calculate()
print(odd2())
print()
"""however, for larger cases with multiple attributes and methods, a class
implememntation may be more appropriate"""
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier
times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)
print(times3(9))
print(times5(3))
print(times3(2))
print()
python decorator
"""remember that everything in python is an object, even functions"""
# nested function where we can include a function in another function
def outer(x):
    def inner(y):
        return x + y
    return inner
add_five = outer(5)
result = add_five(6)
print(result)
print()
# pass function as an argument
def add(x, y):
    return x + y
def calculate(func, x, y):
    return func(x, y)
result = calculate(add, 4, 12)
print(result)
print()
# return a function as a value
def greeting(name):
    def hello():
        return 'Hello, ' + name + '!'
    return hello
greet = greeting('Francis Royce')
print(greet())
print()
# python decorator
"""a python decorator is a function that takes in a function and returns it by
adding some functionality"""
def make_pretty(func):
    def inner():
        print('i got decorated')
        func()
    return inner
def ordinary():
    print('i am ordinary')
ordinary()
print()
# now lets call it using decorator function
def make_pretty(func):
    def inner():
        print('i got decorated')
        func()
    return inner
def ordinary():
    print('i am ordinary')
decorated_func = make_pretty(ordinary)
decorated_func()
print()
# using @ symbol with decorator
"""instead of assigning the function call to a variable, python provides a much
more elegant way to achieve this functionality using the @ symbol"""
def make_pretty(func):
    def inner():
        print('i am decorated')
        func()
    return inner
@make_pretty
def ordinary():
    print('i am ordinary')
ordinary()
print()
# decorating functions with parameter
def smart_divide(func):
    def inner(a, b):
        print('i am going to divide', a, 'and', b)
        if b == 0:
            print('whoops! cannot divide')
            return
        return func(a, b)
    return inner
@smart_divide
def divide(a, b):
    print(a/b)
divide(2, 5)
divide(2, 0)
divide(10, 2)

# chaining decorators in python
"""to chain decorator in python, we can apply multiple decorators to a
single function by placing them one after the other with the most inner decorator
being applied first"""
def star(func):
    def inner(*args, **kwargs):
        print('*' * 15)
        func(*args, **kwargs)
        print('*' * 15)
    return inner
def percent(func):
    def inner(*args, **kwargs):
        print('%' * 15)
        func(*args, **kwargs)
        print('%' * 15)
    return inner
@star
@percent
def printer(msg):
    print(msg)
printer('hello')

# python @property decorator
"""python programming provides us with a built-in @property decorator which makes usage
of getter and setter much easier in object oriented programming. before going into details
on what @property decorator is, let us first build an institution on why it would be needed
in the first place."""
print()
# class without getters and setters
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
# create a new object
human = Celsius()
# set the temperature
human.temperature = 37
# get the temperature attribute
print(human.temperature)
print(human.to_fahrenheit())

# using getters and setters
"""suppose we want to extend the usability of the celsius class defined above.
we know that the temperature of any object cannot reach below -273.15 degree celsius"""
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError('Temperature below -273.15 is not possible.')
        self._temperature = value
human = Celsius(37)
print(human.get_temperature())
human.set_temperature(-300)
print(human.to_fahrenheit())

lower value (40)
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError('Temperature below -273.15 is not possible.')
        self._temperature = value
human = Celsius(37)
print(human.get_temperature())
human.set_temperature(40)   # 40
print(human.to_fahrenheit())
""""all in all, our update above was not backwards compatible. this is where @property comes to rescue"""
print()
# the property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
#     getter
    def get_temperature(self):
        print('Getting value....')
        return self._temperature
#     setter
    def set_temperature(self, value):
        print('Setting value..')
        if value < -273.15:
            raise ValueError('Temperature below -273.15 is not possible')
        self._temperature = value
        temperature = property(get_temperature, set_temperature)
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300

# the @property decorator
"""in python, property() is built-in function that creates and returns a property object"""
# temperature = property()
# temperature = temperature.getter(get_temperature)
# temperature = temperature.setter(set_temperature)

 # using @property decorator
class Celsius:
     def __init__(self, temperature=0):
         self.temperature = temperature
     def to_fahrenheit(self):
         return (self.temperature * 1.8) + 32
     @property
     def temperature(self):
         print('Getting value...')
         return self._temperature
     @temperature.setter
     def temperature(self, value):
         print('Setting value...')
         if value < -273.15:
             raise ValueError ('Temperature below -273 is not possible')
         self._temperature = value
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
coldest_thing = Celsius(20)

# python RegEx (Regular Expression)
"""a regular expression (RegEx) is a sequence of characters that defines a search pattern
a python has a module named re to work with RegEx"""
# use of re
import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print('search successful')
else:
    print('search unsuccessful')

# specify pattern using RegEx
"""to specify regular expressions, metacharacters are used. in the above example
^ and $ are metacharacters"""

# metacharacters
"""metacharacters are characters that are interpreted in a special way by a RegEx engine
lists of metacharacters: [] . $ * + ? {} () \|"""

# [] square brackets-it specifies a set of characters you wish to match

# python RegEx(import re)
# python re.findall()
"""returns a list of strings containing all matches"""
import re
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)

# re.split()
"""re.split method splits the string where there is a match and returns a list of strings
where the splits have occured"""

import re
string = 'Twelve: 12 Eighty nine: 89 Nine: 9.'
pattern = '\d+'
result = re.split(pattern, string)
print(result)
print()
# re.sub()
"""returns a string where matched occurrences are replaced with the content of replace variable"""
import re
string = 'abc 12' \
         ' de 23 \n f45 6'
pattern = '\s+'
replace = ''
new_string = re.sub(pattern, replace, string)
print(new_string)
print()
# re.subn()
"""it is similar to re.sub() except it returns a tuple of items containing the new
string and the number of substitution made"""
import re
string = 'abc 12' \
         ' de 23 \n f45 6'
pattern = '\s+'
replace = ''
new_string = re.subn(pattern, replace, string)
print(new_string)

# re.search() method
"""takes two arguments: a pattern and a string"""

import re
string = 'Python is fun'
match = re.search('\APython', string)
if match:
    print('pattern found in the string')
else:
    print('pattern not found')

# match.group()
"""this method returns the part of the string where there is a match"""
import re
string = '39801 356, 2102 1111'
pattern = '(\d{3}) (\d{2})'
match = re.search(pattern, string)
print(match)
if match:
    print(match.group())
else:
    print('pattern not found')
print()
# using r prefix before RegEx
"""when using r or R prefix is used before a regular expression. it means raw string"""
# raw string using r prefix
import re
string = '\n and \r are escape sequance'
result = re.findall(r'[\n\r]', string)
print(result)

# python datetime
"""python has a module named datetime to work with dates and times.
it provides a variety of classes for representing and manipulating dates and times
as well as parsing dates and times in a variety of formats"""

# get current date and time
import datetime
now = datetime.datetime.now()
print(now)

# get current date
import datetime
current_date = datetime.date.today()
print(current_date)

# attributes of datetime module
import datetime
print(dir(datetime))

# python datetime.date class
# date object to represent a date
import datetime
d = datetime.date(2022, 2, 22)
print(d)

# import only date class
from datetime import date
d = date(2022, 2, 22)
print(d)

# get current date using today()
from datetime import date
todays_date = date.today()
print(todays_date)

# get date from a timestamp
from datetime import date
timestamp = date.fromtimestamp(1326244364)
print('Date', timestamp)

from datetime import date
timestamp = date.fromtimestamp(1642062855)
print('Date', timestamp)
print()
# print today's year, month and day
from datetime import date
today = date.today()
print('current year:', today.year)
print('current month:', today.month)
print('current day:', today.day)

# more on dates
# look them up
