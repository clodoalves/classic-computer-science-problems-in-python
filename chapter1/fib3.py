'''
Using memoization to save the Fibonacci numbers that have already to calculated before. 
Using this approach now is possible to calculate greater numbers (such as 50)
'''

memo = {0:0, 1:1} 

def fib3(number):
    if (number not in memo):
        memo[number] = fib3(number - 1) + fib3(number - 2) 

    return memo[number]

if __name__ == "__main__":
    print(fib3(50))