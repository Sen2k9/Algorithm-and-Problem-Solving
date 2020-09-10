"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        total_list = len(lists)
        interval = 1
        
        while interval < total_list:
            for i in range(0, total_list - interval, interval * 2):
                lists[i] = self.merge2lists(lists[i], lists[i + interval])
            
            interval = interval * 2
            
        return lists[0] if total_list > 0 else None
        
    
    def merge2lists(self, list1, list2=None):
        
        if not list2:
            return list1
        
        
        dummy = ListNode(0)
        head = dummy
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
                
            dummy = dummy.next
            
        if list1:
            dummy.next = list1
        
        if list2:
            dummy.next = list2
            
        return head.next
            
                
                
            
        