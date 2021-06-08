'''
Serialize/deserialize binary tree
- use preorder traversal
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        def helper(root):
            nonlocal my_str
            if root:
                my_str.append(str(root.val))
                helper(root.left)
                helper(root.right)
            else:
                my_str.append("#")
        my_str = []
        helper(root)
        return " ".join(my_str)
    def deserialize(self, data):
        def helper():
            nonlocal cur_index
            if cur_index > len(data)-1:
                return
            root_val = data[cur_index]
            if root_val == "#":
                cur_index+=1
                return None
            root = TreeNode(root_val)
            cur_index+=1
            root.left = helper()
            root.right = helper()
            return root
        
        cur_index = 0
        return helper(data.split(" "))

if __name__ == "__main__":
    root=TreeNode(1,TreeNode(2,None,None),TreeNode(3,TreeNode(4,None,None),TreeNode(5,None,None)))
    ser = Codec()
    deser = Codec()
    print(ser.serialize(root))