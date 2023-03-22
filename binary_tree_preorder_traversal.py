# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        if not root:
            return []

        self.inner_func(root)
        return self.result

    def inner_func(self, root):
        if root:
            self.result.append(root.val)
            self.inner_func(root.left)
            self.inner_func(root.right)
