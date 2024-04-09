from typing import List

def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    """
    Time taken by k to get out =
    Time taken by people before k --> Either the person gets out, or k gets out
    (+) Time taken by person k --> k gets all of their tickets
    (+) Time taken by people after k --> Either the person gets out, or k has 1 last ticket left
    
    """
    total_time = 0
    
    for idx, val in enumerate(tickets):
        
        if idx <= k:
            # total seconds needed is determined by the minimum between current tickets needed and tickets needed for k
            total_time += min(val, tickets[k]) 
        else:
            total_time += min(val, tickets[k] - 1)
    
    return total_time


#### Test Suite ####

test_cases = [
    [[2, 3, 2], 2],
    [[5, 1, 1, 1], 0],
]

expected = [6, 8,]

def sample_tc(func):
    for idx, test_case in enumerate(test_cases):
        tickets, k = test_case[0], test_case[1]
        actual = func(tickets, k)
        if actual != expected[idx]:
            print(f"Incorrect result for test case {idx}: expected {expected[idx]}, actual {actual}. ")
        else:
            print("Passed")

sample_tc(timeRequiredToBuy)

#### Test Suite ####