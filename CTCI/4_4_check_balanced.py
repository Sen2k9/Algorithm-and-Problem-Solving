"""
check balanced:
Implement a function to check if a binary tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never
differ by more than one.
"""
flag = True


def check_balanced(root):
    global flag

    if not root:
        return 0

    left = check_balanced(root.left)

    right = check_balanced(root.right)
    if not flag:
        return

    if abs(left - right) > 1:
        flag = False
        return

    return max(left, right)+1


check_balanced(root)
