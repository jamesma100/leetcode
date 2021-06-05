class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		if not p and not q:
			return True
class Solution:
	def isSameTree(self, p, q):
		if not p and not q:
			return True
		if (p and not q) or (q and not p):
			return False
		return p.val==q.val and self.isSameTree(p.left,q.left) and \
			self.isSameTree(p.right,q.right)
