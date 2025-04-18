"""
def getRoundResult(winning_suit, suit1, number1, suit2, number2):

    if suit1 == winning_suit and suit2 == winning_suit:
        if number1 > number2:
            return "Player 1 wins"
        elif number1 < number2:
            return "Player 2 wins"
        else:
            return "Draw"
    elif suit1 == winning_suit:
        return "Player 1 wins"
    elif suit2 == winning_suit:
        return "Player 2 wins"
    else:
        if number1 > number2:
            return "Player 1 wins"
        elif number1 < number2:
            return "Player 2 wins"
        else:
            return "Draw"


w = "B"
n = 5

print(getRoundResult(w, "A", 2, "B", 1))
"""
from typing import List

def find_duplicates(arr1: List[int], arr2: List[int]) -> List[int]:
    # if same size, linear is optimal
    # if different size, binary search is optimal

    ptr1, ptr2 = 0, 0
    result = []
    M, N = 0, 0

    if len(arr1) < len(arr2):
        N = len(arr1)
    else:
        N = len(arr2)
        arr1, arr2 = arr2, arr1 # swap array

    def binary_search(target, arr2):
        low = 0 # left most index
        high = len(arr2) - 1 # right most index
    
        while low <= high: # base case to exit
            mid = low + (high - low) // 2
            
            if arr2[mid] == target: # match
                return target
            
            if arr2[mid] < target:
                low = mid + 1
            
            elif arr2[mid] > target:
                high = mid - 1

        # no match
        return -1


    while ptr1 < N:
        target = arr1[ptr1]
        match = binary_search(
            target, arr2
            )
        
        print(match, target)
        if match > -1:
            result.append(target)
        
        ptr1 += 1

    
    return result
    
  
# debug your code below
print(find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))