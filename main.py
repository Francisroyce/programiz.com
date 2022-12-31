# full lesson from Francis Royce1

# day one assigning values to variables

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

# numerical data type
num1 = 1
print(num1, 'is of type', type(num1))   # integer
num2 = 2.1
print(num2, 'is of type', type(num2))   # float
num3 = 1 + 2j
print(num3, 'is of type', type(num3))   # complex

# list data type []
languages = ['swift', 'java', 'python']
print(languages)

# access list items
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

# using (remove) to delete a list items
languages = ['swift', 'java', 'python']
languages.remove('java')
print(languages)

# clear()
languages = ['swift', 'java', 'python']
languages.clear()
print('list after clear:', languages)

# del can be used also to empty the list
languages = ['swift', 'java', 'python']
del languages[:]
print('languages:', languages)

# copying a list: it returns a new list and doesn't modify the original list
my_list = ['cat', 0, 6, 7]
new_list = my_list.copy()
print('copied list', new_list)

# list copying using operator (=)
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
new_list[1] = 'dog'
print('Old list', my_list)
print('New list', new_list)
