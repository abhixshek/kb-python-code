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

