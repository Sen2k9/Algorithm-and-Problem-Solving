"""
Print odd and even numbers in two threads

"""

import threading

odd_event = threading.Event()
even_event = threading.Event()
TIMEOUT = 0.1

def printEven(n):
    
    for val in range(0, n, 2):
        print(f"Print Even: {val}", flush=True)
        
        odd_event.set()
        even_event.clear()
        even_event.wait(timeout=TIMEOUT) # wait 0.1 sec until another thread finishes their work and set the flag to true
    
    print("Print Even functions complete")

def printOdd(n):
    
    for val in range(1, n, 2):
        print(f"Print Odd: {val}", flush=True)
        
        even_event.set()
        odd_event.clear()
        odd_event.wait(timeout=TIMEOUT) # wait 0.1 sec until another thread finishes their work and set the flag to true
    
    print("Print Odd functions complete")


if __name__ == "__main__":
    number = 10
    
    even_thread = threading.Thread(target=printEven, args=(number,), daemon=False)
    odd_thread = threading.Thread(target=printOdd, args=(number,), daemon=False)
    
    even_thread.start()
    odd_thread.start()