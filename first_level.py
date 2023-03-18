import second_level 
"""when I import first_level in python session and reload(first_level)
it doesnt reload this second_level, i.e. it doesnt reload the import statement"""

r = 'this is the top level module/script.'
k = 111
v = second_level.t
print(v)
print(r)
print(k)
print('end of top level script')
