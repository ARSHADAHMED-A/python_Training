'''Q1.'''
numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print(square(5))
print(square(2*5))

'''Q2'''
x = 1
def ab():
    return x
print(x)
print(ab())

'''Q3.'''
x = 1
def db():
    x = 2
    return x
print(x)
print(db())
print(x)

'''Q4'''
x = 1
def ac():
    x = 2
    return x
print(x)
print(ac())
print(x)

'''Q5.'''
x = 1
def abc():
    y = x
    x = 2
    return x+y
print(x)
print(abc())
print(x)

#we needed to declare x first

'''Q6'''
x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x,y)
 
def istrcmp(str1, str2):
    return str1 == str2
print(istrcmp("hello","Hello"))


print(2 < 3 and 3 > 1)
print(2 < 3 or 3 > 1)
print(2 < 3 or not 3 > 1)
print(2 < 3 and not 3 > 1)


x = 4
y = 5
p = x < y or x < z
print(p)


# z is not defined