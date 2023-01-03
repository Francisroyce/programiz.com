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

# 1- numerical data type
num1 = 1
print(num1, 'is of type', type(num1))   # integer
num2 = 2.1
print(num2, 'is of type', type(num2))   # float
num3 = 1 + 2j
print(num3, 'is of type', type(num3))   # complex

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

# sort with custom function using key







