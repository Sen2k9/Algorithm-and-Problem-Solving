import unittest


class Solution:
    
    def __init__(self):
        pass

    def intervalIntersection(self, firstList: list, secondList: list) -> list:
        if not firstList or not secondList:
            return []
        ans = []
        first_ptr = second_ptr = 0
        while first_ptr < len(firstList) and second_ptr < len(secondList):
            low = max(
                firstList[first_ptr][0],
                secondList[second_ptr][0]
            )

            high = min(
                firstList[first_ptr][1],
                secondList[second_ptr][1]
            )

            if low <= high:
                ans.append([low, high])
            
            if firstList[first_ptr][1] < secondList[second_ptr][1]:
                first_ptr += 1
            else:
                second_ptr += 1
        return ans
    

class TestSolution(unittest.TestCase):

    def test_interval_intersection(self):
        sol = Solution()
        self.assertEqual(
            sol.intervalIntersection(
                [
                    [1, 7], [9, 13]
                ],
                [
                    [2, 4], [6, 7], [11, 12]
                ]
            ),
            [[2, 4], [6, 7], [11, 12]]
        )

        self.assertEqual(
            sol.intervalIntersection(
                [
                ],
                [
                    [2, 4], [6, 7], [11, 12]
                ]
            ),
            []
        )

if __name__ == '__main__':
    unittest.main()