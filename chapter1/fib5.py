'''
Solving the Fibonacci sequence using a traditional iterative approach
'''

def fib5 (number):    

    if (number == 0):
        return number
    
    last = 0
    next = 1

    for _ in range(1, number):
        last, next = next, last + next

    return next

if __name__ == "__main__":
    print(fib5(50))