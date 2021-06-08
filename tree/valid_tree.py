class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def helper(root, imin, imax):
            if not root:
                return True
            return root.val > imin and root.val < imax and \
                helper(root.left, imin, root.val) and \
                helper(root.right, root.val, imax)
        return helper(root, -float('inf'), float('inf'))