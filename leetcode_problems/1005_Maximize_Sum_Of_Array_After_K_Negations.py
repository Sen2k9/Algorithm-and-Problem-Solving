"""
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].

Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

Note:

    1 <= A.length <= 10000
    1 <= K <= 10000
    -100 <= A[i] <= 100

"""


class Solution:
    def largestSumAfterKNegations(self, A, K):
        # Solution 1: self, slow
        # A = sorted(A)
        # i = 0
        # k = K
        # # print(A)
        # while k > 0 and i < len(A):
        #     if A[0] < 0:
        #         A[0] = A[0] * (-1)
        #         i += 1
        #         k -= 1
        #     elif A[0] == 0:
        #         k = 0

        #     elif A[0] > 0:
        #         k = k % 2
        #         if k == 0:

        #             A[0] = A[0]
        #         else:
        #             A[0] = -A[0]
        #             k -= 1

        #     A.sort()
        #     print(A, A[0], k)
        # return sum(A)

        # Solution 2: self, faster

        # neg_arr = []
        # pos_arr = []
        # for each in A:  # dividing the array into negative and postive elements
        #     if each < 0:
        #         neg_arr.append(each)
        #     else:
        #         pos_arr.append(each)
        # neg_arr.sort(reverse=True)
        # print(neg_arr)

        # while neg_arr and K > 0:  # making the negative elements positive
        #     neg_arr[-1] = neg_arr[-1] * (-1)

        #     K -= 1
        #     pos_arr.append(neg_arr.pop())
        # if K == 0:  # if there is no process left then the sum of total change is the answer
        #     return sum(pos_arr + neg_arr)

        # pos_arr.sort()  # when there is some process left we need to sort all positive number for next process
        # print(neg_arr, pos_arr)

        # if pos_arr[0] == 0:  # if the smallest one is zero then we found the largest possible sum array
        #     return sum(pos_arr + neg_arr)

        # else:  # no value is zero then we need to change the positive value carefully like below
        #     K = K % 2
        #     if K == 0:

        #         pos_arr[0] = pos_arr[0]
        #     else:
        #         pos_arr[0] = -pos_arr[0]

        #     return sum(pos_arr+neg_arr)

        # Solution 3: fastest

        i = 0
        A.sort()

        while i < len(A) and K > 0:
            if A[i] < 0:
                A[i] = -A[i]
                K -= 1
            elif A[i] == 0:
                return sum(A)

            else:
                K = K % 2

                if K == 0:
                    return sum(A)
                else:

                    if A[i] < A[i - 1]:
                        A[i] = -A[i]
                        return sum(A)

                    else:
                        A[i - 1] = -A[i - 1]
                        return sum(A)
            i += 1
        return sum(A)


sol = Solution()
A = [2, -3, -1, 5, -4]
K = 2


print(sol.largestSumAfterKNegations(A, K))
