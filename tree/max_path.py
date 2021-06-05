
'''
Given root of a binary tree, return maximum path sum of any path

Example: max path sum = 29 (7+1+3+8+10)
             3
            / \ 
           1   8
          /\   /\ 
         6  7 9  10

Algorithm:
1. max_branch(root) finds maximum singular path (only extends in one direction) consisting of root node 
that can be further extended upwards i.e. max_branch(3) will return 21 (3+8+10), not 29 (7+1+3+8+10) 
2. take max between left/right and 0 because path could be negative - if negative, exclude since
it will not give us a larger path
3. cur_path stands for maximum path consisting of current node that cannot be extended upwards, i.e.
root.val + max_branch(left) + max_branch(right), update final imax with this value
4. return NOT cur_path but root.val + max(left, right) because (1) result has to be able to extend upwards

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def max_path(self, root):
        imax = -float('inf')
        def max_branch(root):
            nonlocal imax
            if not root:
                return 0
            max_left_branch = max(max_branch(root.left), 0)
            max_right_branch = max(max_branch(root.right), 0)
            max_path_with_cur = root.val + max_left_branch + max_right_branch
            imax = max(imax, max_path_with_cur)
            return root.val + max(max_left_branch, max_right_branch)
        max_branch(root)
        return imax
