'''
Construct binary tree from preorder and inorder traversals

Example: 
- preorder: 3 9 20 15 7
- inorder: 9 3 15 20 7

     3 
    / \ 
   9   20
       / \ 
      15  7

- Preorder always gives root first, so keep index in preorder and increment every recursive call
- Given index in preorder, preorder[index] gives root, find the node in inorder
    - everything left of it is left subtree
    - everything right of it is right subtree
    - left and right params used to terminate: i.e. when right < left
- Use hashmap for (inorder val, inorder index) to speed up searching left & right subtrees given root node
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        def helper(start, end):
            if end < start:
                return None
            nonlocal root_index
            # find root value by index, create root node
            root_val = preorder[root_index]
            root = TreeNode(root_val)
            # use root value and find position in inorder
            inorder_pos = dic[root_val]
            root_index+=1

            root.left = helper(start, inorder_pos-1)
            root.right = helper(inorder_pos+1, end)
            return root
        
        dic = {}
        for i, val in enumerate(inorder):
            dic[val] = i
        root_index = 0
        node = helper(0, len(preorder)-1)
        return node