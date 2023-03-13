# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack1 = []

        while root or stack1:
            if root:
                stack1.append(root)
                root = root.left
            else:
                n = stack1.pop()
                result.append(n.val)
                root = n.right
        return result