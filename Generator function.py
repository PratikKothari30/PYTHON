#Generator func
'''def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)'''

#METNHOD First
# A simple generator for Fibonacci Numbers
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Create a generator object
fib_gen = fib(5)

# Iterate over the generator using a for loop
for num in fib_gen:
    print(num)

'''# Alternatively, we can use a while loop and catch the StopIteration exception
fib_gen = fib(5)
while True:
    try:
        num = next(fib_gen)
        print(num)
    except StopIteration:
        break'''


'''#x is a generator object 
#METHOD Two
def simplegeneratorFun():  
    x = simplegeneratorFun()

# iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))

#fib
#A simple generator for Fibonacci Numbers
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
x=fib(5)

#Iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))

#Iterating over the generator object using for
print("\nUsing for in loop")
for i in fib(5):
    print(i)'''