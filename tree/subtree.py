class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # returns true if the two trees with roots root and subRoot are equivalent
    def isSubtree(self, root, subRoot):
        def isSameTree(root, subRoot):
            # NULL trees are equivalent
            if not root and not subRoot:
                return True
            # return false if trees are structurally different i.e. one has a left
            # node while the other doesn't
            if (root and not subRoot) or (not root and subRoot):
                return False
            if root.val==subRoot.val and \
                isSameTree(root.left, subRoot.left) and \
                isSameTree(root.right, subRoot.right):
                    return True
            return False
        # base case: recurse till bottom nodes of tree without finding match with
        # subTree
        if not root or not subRoot:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)
        
