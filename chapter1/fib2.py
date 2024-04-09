'''
Since the case base has been added in the Fibonacci implementation (number < 2), 
the infinite loop doesn't occur anymore. However, this implementation has sufficient performance 
only for low numbers (such as 5 or 10). For greater numbers (such as 50), 
the execution won't end ever because the execution tree will grow exponentially.
'''

def fib2(number):
    if (number < 2):
        return number
    
    return fib2(number - 1) + fib2(number - 2)

if __name__ =="__main__":
    print(fib2(50))