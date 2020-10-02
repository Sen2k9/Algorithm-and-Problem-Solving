"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:

Input: nums = [1]
Output: "1"

Example 4:

Input: nums = [10]
Output: "10"

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 109

"""


class LargerNumberKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums) -> str:

        asStr = list(map(str, nums))
        print(asStr)

        sorted_asStr = self.customized_merge_sort(asStr)

        print(sorted_asStr)

        if sorted_asStr[0] == "0": # corner case
            return "0"
        else:
            return "".join(sorted_asStr)

    def customized_merge_sort(self, asStr):

        if not asStr or len(asStr) == 1:
            return asStr

        low = 0

        high = len(asStr)

        mid = (low + high) // 2

        left_array = self.customized_merge_sort(asStr[: mid])
        right_array = self.customized_merge_sort(asStr[mid:])

        i = j = 0

        new_array = []

        while i < len(left_array) and j < len(right_array):
            # concatenating two string and comparing with each other

            if left_array[i] + right_array[j] > right_array[j] + left_array[i]:
                new_array.append(left_array[i])
                i += 1

            elif left_array[i] + right_array[j] <= right_array[j] + left_array[i]:
                new_array.append(right_array[j])
                j += 1

        while i < len(left_array):
            new_array = new_array + left_array[i:]
            break

        while j < len(right_array):
            new_array = new_array + right_array[j:]
            break

        return new_array


sol = Solution()
nums = [3,30,34,5,9]
print(sol.largestNumber(nums))

nums = [1]
print(sol.largestNumber(nums))

nums = [10]
print(sol.largestNumber(nums))

nums = [0, 0, 0]
print(sol.largestNumber(nums))