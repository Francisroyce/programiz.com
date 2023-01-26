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
print('({x}, {y})'.format_map(coordinate(x='6')))
print('({x}, {y})'.format_map(coordinate(y='9')))
print('({x}, {y})'.format_map(coordinate(x='6', y='0')))

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

# deleting attribute using del operator