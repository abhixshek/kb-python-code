# in python, we do THINGS with STUFF. STUFF are python objects and THINGS are the operations we perform on them.
# Objects are essentially just pieces of memory, with values and sets of associated operations.

# python's core object types include numbers, string, list, dictionary, tuples, sets, booleans, modules, classes, functions, etc, etc

# Strings are examples of sequence in python.
# sequence = a positionally ordered collection of other objects. 
# other examples of sequences are lists and tuples.

S = 'Spam'
print(len(S)) # 4
print(S[1]) # 'p'
# S[1] is a indexing expression
# S is a variable. variables are replaced by their value when used in an expression. that is, in above examples S was replaced by 'Spam' behind the scenes.
print('Spam'[1])

# negative indexes count from the right(end).
print(S[-1], S[-2])

# negative indexes are simply added to the len of the sequence behind the scenes. So, -1 above is simply point to len(S) - 1 = 4-1= 3 , i.e. S[3] which is 'm'

# slicing is another way of indexing. X[I:J] returns everything in X from offset(index) I to (J-1). that is J is not included.
print(S[1:3]) # returns 'pa'
# In a slice, the left bound defaults to zero, and the right bound defaults to the length of the sequence being sliced.

print(S[:3]) # 'Spa'
print(S[1:]) # 'pam'
print(S[:]) # everything in S, i.e. O:len(S), useful to create a copy. 

print(S[:-1]) # 'Spa' , nothing but 0:len(S)-1 i.e. 0:3


# An important property of sequences is that they support **concatenation** and **repetition**.
print(S + 'xyz')
print(S * 3)

# string methods
# find() to find substring in a string. returns -1 is not found. 
# replace() to replace a substring with a replacement value. 
s = 'this is a school building'
print(s.find('build')) # returns the index of the substring(start of the substring) = 17
print(s.find('delhi')) # -1 since delhi is not part of the string anywhere. 

print(s.replace('school', 'office'))


# string formatting
st = 'this is a string'
num = 78
height = 85.561278
print('%s okay %d fine%f'%(st,num,height)) # string formatting expression
print('{} okay {} fine{}{}'.format(st,num,height, 'wow cool')) # .format() - string formatting method call
print('{0} okay {1} fine{2}{3}'.format(st,num,height, 'wow cool')) #you can give the number to indicate which variable from the arguments to .format() to insert at that position
print('{3} okay {1} fine{0}{2}'.format(st,num,height, 'wow cool')) # changed the order

#lists in python
w = [1,7,9.45, 'abhi']
# since lists are sequences, they support all sequence operations we covered above for strings. 
print(len(w))
print(w[-1])
print(w[:-1])
print(w) # w remains unchanged so far. 
print(w + [5,'go', 'ai'])
print(w) # w remains unchanged so far. 

# list methods
w.append('cool')
print(w) # w updated in place
item = w.pop(2) # 2 is the index 
print(item)
print(w) # w updated with item at index 2 previously removed now. 
del w[1]
print(w) # del works the same way as .pop() but doesnt return anything. again, list w updated in place.

#### print(w.sort()) throws Typeerror because w contains int and str objects and they cannot be compared to tell which is smaller or larger.

q = [7,3,9,2,8,1,66]
print(q.reverse()) # .reverse() operation does not return anything and just does what it does. therefore, None is printed in output 
print(q) # q updated in place.

r = [1,5,7]
## assigning beyond index range gives a IndexError. ex. : r[3] = 45. FAILS. Even just quering an index that doesnt exist, will give error. therefore print(r[3]) will give IndexError.
# therefore, to append to a list, always use .append() or .insert()

# list comprehension
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
# how do you extract column 2(middle)?
column2 = [row[1] for row in matrix]
print(column2)
# how do you extract even numbers from column 2?
even_nos = [row[1] for row in matrix if row[1] % 2 == 0]
print(even_nos)


