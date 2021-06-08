class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Traversal:
    # in order traversal: left, visit, right
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.val,end=" ")
        self.in_order(root.right)
    
    # pre order traversal: visit, left, right
    def pre_order(self, root):
        if not root:
            return
        print(root.val,end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    # post order traversal: left, right, visit
    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val,end=" ")

if __name__ == "__main__":
    node = TreeNode(3,TreeNode(1,TreeNode(9,None,None),TreeNode(0,None,None)),\
        TreeNode(2,TreeNode(8,None,None),TreeNode(4,None,None)))
    Traversal().in_order(node)
    print("\n")
    Traversal().pre_order(node)
    print("\n")
    Traversal().post_order(node)
    print("\n")
