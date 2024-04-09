'''
Purposefully wrong Fibonacci implementation to cause an infinite loop because there is no base
case to stop the recursion
'''

def fib1(number):
    return fib1(number - 1) + fib1(number - 2)

if __name__ == "__main__":
    print(fib1(5))