"""
Given two arrays, arr[] and dep[], that represent the arrival and departure times of trains respectively, 
the task is to find the minimum number of platforms required so that no train waits.

Examples: 

    Input: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
    Output: 3 
    Explanation: There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.

    Input: arr[] = [1,  5], dep[] = [3, 7] 
    Output: 1 
    Explanation:  All train times are mutually exclusive. So we need only one platform

"""
import unittest


def minPlatform(arr, dep):
    # arr.sort()
    # dep.sort()
    
    arr = sorted(arr)
    dep = sorted(dep)
    
    j = 0
    platform_cnt = 0
    res = 0
    
    for i in range(len(arr)):
        
        # if there is a departure during or before arrival
        while j < len(dep) and dep[j] < arr[i]:
            platform_cnt -= 1
            j += 1 # look for next departure
        
        # otherwise increase platform
        platform_cnt += 1
        res = max(res, platform_cnt)
    
    return res


class TestSuite(unittest.TestCase):
    
    def test_minPlatform(self):
        arr = [900, 940, 950, 1100, 1500, 1800]
        dep = [910, 1200, 1120, 1130, 1900, 2000]
        self.assertEqual(
            minPlatform(
                arr,
                dep
            ),
            3
        )


if __name__ == "__main__":
    unittest.main()