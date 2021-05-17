class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = temp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        return dummy.next