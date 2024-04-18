from time import time
#In Python, decorators are a powerful feature that allow you to modify the behavior of a function or class. Can you explain what a Python decorator is, and provide an example of a simple decorator that logs the execution time of a function?

def my_decorator(func):
    def wrapper(*args_for_func):
        x = time()
        result = func(*args_for_func)
        y = time()
        print(y - x)
        return result
    return wrapper
    
@my_decorator
def adder(x, y):
    print(x+y)

adder(2, 3)