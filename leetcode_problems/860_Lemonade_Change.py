"""
At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.

Example 1:

Input: [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: [5,5,10]
Output: true

Example 3:

Input: [10,10]
Output: false

Example 4:

Input: [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.

Note:

    0 <= bills.length <= 10000
    bills[i] will be either 5, 10, or 20.


"""


class Solution:
    def lemonadeChange(self, bills):
        # Solution 1: self
        # dic = {}
        # for each in bills:
        #     if each == 5:
        #         dic[5] = dic.get(5, 0)+1
        #     elif each == 10:
        #         if dic.get(5, 0) > 0:
        #             dic[10] = dic.get(10, 0) + 1
        #             dic[5] -= 1
        #         else:
        #             return False

        #     elif each == 20:
        #         if dic.get(5, 0) > 0 and dic.get(10, 0) > 0:
        #             dic[5] -= 1
        #             dic[10] -= 1
        #         elif dic.get(5, 0) > 2:
        #             dic[5] -= 3
        #         else:
        #             return False
        # return True

        # Solution 2: dynamic programming
        if bills[0] == 10 or bills[0] == 20:
            return False

        dp = [0]*len(bills)
        dp[0] = bills[0]
        change = 0

        for i in range(1, len(bills)):
            if bills[i] == 10 or bills[i] == 20:
                dp[i] = dp[i - 1] + bills[i] - 5
            else:
                dp[i] = dp[i - 1] + bills[i]
        print(dp)


sol = Solution()
bills = [5, 5, 10]
print(sol.lemonadeChange(bills))
