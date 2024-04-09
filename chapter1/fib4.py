from functools import lru_cache

'''
Using the lru_cache decorator from fuctools file. When a new Fibonacci number has been calculated,
this decorator allows that new value is saved in cache. This example has the same code
from fib2.py.
'''

@lru_cache(maxsize=None)
def fib4(number):
    if (number < 2):
        return number
    
    return fib4(number - 1) + fib4(number - 2) 


if __name__ == "__main__":
    print(fib4(50))