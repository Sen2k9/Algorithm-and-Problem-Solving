"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".

Example 2:

Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode):
        # Solution 1: self
        # if not t:
        #     return ""

        # def string(t, s):
        #     if not t:
        #         return "()"
        #     s += str(t.val)

        #     if not t.left and not t.right:
        #         return s
        #     # print(s)
        #     if t.left:
        #         s += "("
        #         s = string(t.left, s) + ")"
        #     else:
        #         s = s + "()"

        #     if t.right:
        #         s += "("
        #         s = string(t.right, s)+")"

        #     return s

        # s = ""
        # return string(t, s)

        # Solution 2: clean, and simple
        if not t:
            return ""

        if not t.right and not t.left:
            return "{}".format(t.val)
        elif not t.right:
            return "{}({})".format(t.val, self.tree2str(t.left))
        elif not t.left:
            return "{}()({})".format(t.val, self.tree2str(t.right))
        else:
            return "{}({})({})".format(t.val, self.tree2str(t.left), self.tree2str(t.right))
