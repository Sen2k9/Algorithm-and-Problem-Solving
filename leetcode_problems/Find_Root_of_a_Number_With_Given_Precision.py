"""
Given a positive number n and precision p, 
find the square root of number upto p decimal places using binary search. 
"""

def squareRoot(n, p):
    
    def get_integerRoot(n):
        low = 0
        high = n
        while low <= high:
            #print(low, high)
            mid = low + (high - low) / 2
            
            if mid**2 == n:
                return mid
            
            elif mid**2 > n:
                high = mid - 1
            
            elif mid**2 < n:
                low = mid + 1
        
        return low
        
    def get_precision(root, n, precision):
        increment = 0.1
        # iterate upto the precision point
        for _ in range(precision):
            while root * root <= n:
                root  = root + increment
            
            # went over, reduce it to previous one
            root = root - increment
            increment = increment / 10 # precision place
        
        return round(root, precision)
    
    root = get_integerRoot(n)
    
    return get_precision(root, n, p)
    

# driver code
if __name__ == "__main__":
    print(squareRoot(
        5, 4
    ))
    print(squareRoot(
        7, 4
    ))