class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
        return True