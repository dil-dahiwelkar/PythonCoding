# Generators
def generator():
    for i in range(5):
        yield i
#
gen = generator()
print(next(gen))
print(next(gen))


# Decorators
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
#
@my_decorator
def say_hello():
    print("Hello, World!")
#
say_hello()

def my_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@my_decorator(2)
def greet(name):
    print(f"Hello, {name}")

greet("Dilasha")

