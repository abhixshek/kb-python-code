# some different forms of floating point numbers(floats)
a = 1.2
b = 0.5
c = .45
d = -.32
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
e = 2e3
f = 3.0E2
g = 2.45e-2
print(e, f, g)
print(type(e), type(f), type(g))

# mixed types are converted up
a = 5
b = 12.0
c = a + b
print(c, type(c))

b = 4j
c = a + b
print(c, type(c))

b = 2 + 3.5j
c = a + b
print(c, type(c))

#evaluations of some mixed expressions
a = 2 ** 3 ** 2 # computes 3 ** 2 first, i.e. = 9 and then 2 ** 9 = 512
b = 2 ** 3 + 1 ** 2 # since exponentiation has higher precedence than +, it evaluates 1**2=1 and 2**3=8
# and then adds the results 8+1 = 9
print(a, b)

a = 4 * 5 / 2 #since * and / are in the same row, they have same precedence and the operations are grouped from left to right
# therefore 4*5= 20 happens first, then 20 /2 = 10 final result.
print(a)
a = 4 / 5 * 2 # 4 / 5 = 0.8 then 0.8*2 = 1.6
print(a)

