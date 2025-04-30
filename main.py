def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    
    if n == 0: #base case 0
        return 0
    elif n == 1: #base case 1
        return 1

    return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts) #recursive formula return

    
def fib_top_down(n, fibs):
    if n == 0: #base case 0
        return 0
    elif n == 1: #base case 1
        return 1

    if fibs[n] != -1: #if already calculated, return calculation
        return fibs[n]

    fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs) #if not, calculate and return calculation
    return fibs[n]

def fib_bottom_up(n):
    if n == 0: #base case 0
        return 0
    elif n == 1: #base case 1
        return 1

    fibs = [0] * (n + 1) #make an array to store fibonacci calculations
    fibs[1] = 1 #set the 01th value in the arrat to 1

    for i in range(2, n + 1): #recursively sort through array to add last value to the value before and get the new one
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]




