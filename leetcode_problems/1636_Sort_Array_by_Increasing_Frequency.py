from collections import defaultdict

class Solution:
    def frequencySort(self, nums):
        dic_freq = defaultdict(int)

        for num in nums:
            dic_freq[num] += 1

        #print(dic_freq)

        sorted_dict = sorted(dic_freq.items(), key=lambda x: (x[1],x[0]))
        #print(sorted_dict)

        sort_by_value = defaultdict(list)

        for key,val in sorted_dict:
            sort_by_value[val].append(key)
        #print(sort_by_value)

        ans = []

        for key, val in sort_by_value.items():
            if len(val) > 1:
                val = sorted(val, reverse=True)
            for each in val:
                ans += [each]*dic_freq[each]
        return ans







sol = Solution()
nums = [1,1,2,2,2,3]
print(sol.frequencySort(nums))

nums = [2,3,1,3,2]
print(sol.frequencySort(nums))

nums = [2]
print(sol.frequencySort(nums))

nums = [-1,1,-6,4,5,-6,1,4,1]
print(sol.frequencySort(nums))  