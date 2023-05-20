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
