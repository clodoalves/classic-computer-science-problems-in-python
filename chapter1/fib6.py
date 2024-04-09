'''Implementing a generator number using the instruction yield to list the complete Fibonacci 
numbers until a specific value'''

def fib6(num):
    
    #base case
    yield 0 
    
    #base case
    if num > 0:
        yield 1
    
    last = 0
    next = 1

    for _ in range(1, num):
        last, next = next, last + next
        yield next

if __name__ == "__main__":
    for number in fib6(50):
        print(number)