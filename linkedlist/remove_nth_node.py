class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = head.next
        slow, fast = dummy, dummy

        # maintain distance n between slow and fast
        for i in range(0, n):
            fast = fast.next
        
        # make fast equal last node
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # remove target node = slow.next
        slow.next = slow.next
        return dummy.next