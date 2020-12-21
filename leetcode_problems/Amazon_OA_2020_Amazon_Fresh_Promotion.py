"""
Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. The code list contains groups of fruits. Both the order of the groups within the code list and the order of the fruits within the groups matter. However, between the groups of fruits, any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in that location within the group.

Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the following purchases would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana

Write an algorithm to output 1 if the customer is a winner else output 0.

Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.

Output
Return an integer 1 if the customer is a winner else return 0.

Note
'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."
'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

Example 1:

Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [orange, apple, apple, banana, orange, banana]
Output: 1
Explanation:
codeList contains two groups - [apple, apple] and [banana, anything, banana].
The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.

Example 2:

Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [banana, orange, banana, apple, apple]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in order of groups but group [banana, orange, banana] is not following the group [apple, apple] in the codeList.

Example 3:

Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [apple, banana, apple, banana, orange, banana]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in an order which is not following the order of fruit names in the first group.

Example 4:

Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]
Output: 0
Explanation:
The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.
"""


class Solution:

    def __init__(self):
        pass

    def isMatched(self, source, target):

        return source == 'anything' or source == target

    def freshPromotion(self, codeList, shoppingCart) -> int:

        cart_index = 0
        code_index = 0
        code_word_index = 0

        while cart_index < len(shoppingCart) and code_index < len(codeList):
            if self.isMatched(codeList[code_index][code_word_index], shoppingCart[cart_index]):
                # increment code_word_index and cart_index for every match
                code_word_index += 1
                cart_index += 1

                # if code_word_index is equal to the length of the current group
                # go to the next group
                if code_word_index == len(codeList[code_index]):
                    code_index += 1
                    code_word_index = 0
                    
            else:
                # we do not want to increase the cart_index if code_word_index is not in starting point
                # we want to check whether the first index word match with the current cart_index word
                # edge case:
                #    codeList8 = [["apple", "orange"], ["orange", "banana", "orange"]]
                #    shoppingCart8 = ["apple", "orange", "banana", "orange", "orange", "banana", "orange", "grape"]
                if code_word_index > 0: 

                    code_word_index = 0
                    # but if the first word is anything, then we do not care what is the word in the current cart_index
                    # edge case:
                    #    codeList9 = [["anything", "anything", "anything", "apple"], ["banana", "anything", "banana"]]
                    #    shoppingCart9 = ["orange", "apple", "banana", "orange", "apple", "orange", "orange", "banana", "apple", "banana"]
                    if codeList[code_index][code_word_index] == 'anything': 
                        cart_index += 1

                    # there can be multiple 'anything' word side-by-side, 
                    # edge case:
                    #    codeList9 = [["anything", "anything", "anything", "apple"], ["banana", "anything", "banana"]]
                    #    shoppingCart9 = ["orange", "apple", "banana", "orange", "apple", "orange", "orange", "banana", "apple", "banana"]
                    while codeList[code_index][code_word_index] == 'anything':
                        code_word_index += 1
                else:
                    # increment cart_index otherwise
                    cart_index += 1

        if code_index == len(codeList):
            return 1
        else:
            return 0


sol = Solution()

codeList1 = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart1 = ["orange", "apple", "apple", "banana", "orange", "banana"]

codeList2 = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart2 = ["banana", "orange", "banana", "apple", "apple"]

codeList3 = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart3 = ["apple", "banana", "apple", "banana", "orange", "banana"]

codeList4 = [["apple", "apple"], ["apple", "apple", "banana"]]
shoppingCart4 = ["apple", "apple", "apple", "banana"]

codeList5 = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart5 = ["orange", "apple", "apple", "banana", "orange", "banana"]

codeList6 = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart6 = ["apple", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]

codeList7 = [["anything", "apple"], ["banana", "anything", "banana"]]
shoppingCart7 = ["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]

codeList8 = [["apple", "orange"], ["orange", "banana", "orange"]]
shoppingCart8 = ["apple", "orange", "banana", "orange", "orange", "banana", "orange", "grape"]

codeList9 = [["anything", "anything", "anything", "apple"], ["banana", "anything", "banana"]]
shoppingCart9 = ["orange", "apple", "banana", "orange", "apple", "orange", "orange", "banana", "apple", "banana"]

assert sol.freshPromotion(codeList1, shoppingCart1) == 1
assert sol.freshPromotion(codeList2, shoppingCart2) == 0
assert sol.freshPromotion(codeList3, shoppingCart3) == 0
assert sol.freshPromotion(codeList4, shoppingCart4) == 0
assert sol.freshPromotion(codeList5, shoppingCart5) == 1
assert sol.freshPromotion(codeList6, shoppingCart6) == 1

assert sol.freshPromotion(codeList7, shoppingCart7) == 1
assert sol.freshPromotion(codeList8, shoppingCart8) == 1
assert sol.freshPromotion(codeList9, shoppingCart9) == 1