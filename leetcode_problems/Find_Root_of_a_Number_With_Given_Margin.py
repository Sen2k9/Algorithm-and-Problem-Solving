"""
Many times, we need to re-implement basic functions without using any standard 
library functions already implemented. 
For example, when designing a chip that requires very little memory space.

In this question we’ll implement a function root that calculates the n’th root 
of a number. The function takes a nonnegative number x and a positive integer n, 
and returns the positive n’th root of x within an error of 0.001 
(i.e. suppose the real root is y, then the error is: |y-root(x,n)| 
and must satisfy |y-root(x,n)| < 0.001).
"""

def nRoot(x, n, margin):
    low = 0
    high = max(1, x)
    
    approxRoot = low + (high - low) / 2
    # real answer need to be in 0.001 error margin
    while abs(approxRoot**n - x) >= margin:
        
        # too right
        if approxRoot ** n > x:
            high = approxRoot - margin
        # too left
        else:
            low = approxRoot + margin
        
        approxRoot = low + (high - low) / 2
    print(approxRoot, abs(approxRoot**n - x))
    return approxRoot
            
        
    

# driver code
if __name__ == "__main__":
    print(nRoot(
        9, 2, 0.001
    ))
    print(nRoot(
        7, 3, 0.001
    ))