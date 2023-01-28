
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
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

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