
print("Decorator Example")
def decorator(func):
    def wrapper():
        print("Decorator: Before function")
        func()
        print("Decorator: After function")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()

print("Iterator Example")
nums = [1, 2, 3]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))

print("Generator Example")
def generate():
    yield 10
    yield 20
    yield 30

for x in generate():
    print(x)

print("Closure Example")
def outer(msg):
    def inner():
        print(msg)
    return inner

func = outer("Hello from Closure!")
func()

#Output

"""
Decorator Example
Decorator: Before function
Hello!
Decorator: After function
Iterator Example
1
2
3
Generator Example
10
20
30
Closure Example
Hello from Closure!

"""