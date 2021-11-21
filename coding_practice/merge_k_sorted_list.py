import heapq

class Solution:

    def merge_k_sorted_list(self, sorted_lists):
        # this array will hold k number of elements
        # O(k)
        heap = []
        for sorted_list in sorted_lists:
            # klogk
            heapq.heappush(heap, (sorted_list.value, sorted_list))
        
        resultHead = resultTail = None
        # for all element in (N - k) one by one
        # sort operation logk
        # (N - k) * logk
        while heap:
            value, curr_node = heapq.heappop(heap)
            if resultHead is None:
                resultHead = resultTail = curr_node
            else:
                resultTail.next = ListNode(value)
                resultTail = resultTail.next
            if curr_node.next:
                heapq.heappush(heap, (curr_node.next.value, curr_node.next))
        # total = klogk + (N - k)logk = Nlogk
        return resultHead

class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __lt__(self, node):
        return self.value < node.value

import unittest


class TestSolution(unittest.TestCase):
    
    def test_merge_k_sorted_list(self):
        list1 = ListNode(3)
        list1.next = ListNode(4)
        list1.next.next = ListNode(5)

        list2 = ListNode(4)
        list2.next = ListNode(6)
        list2.next.next = ListNode(8)

        list3 = ListNode(7)
        list3.next = ListNode(10)
        list3.next.next = ListNode(15)

        sol = Solution()

        ans = sol.merge_k_sorted_list([list1, list2, list3])
        print(ans)
        self.assertTrue(ans)
        while ans:
            print(ans.value, " ", end='')
            ans = ans.next

if __name__ == '__main__':
    unittest.main()
