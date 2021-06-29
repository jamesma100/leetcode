class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

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
    def reorderList(self, head):
        # find middle of list
        slow, fast = head, head
        # moves fast pointer to the last node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        cur = slow.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        slow.next = None

        # merge lists
        head1, head2 = head, prev
        while head1 and head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp

    def printList(self, li):
        cur = li
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    l1 = ListNode(0, ListNode(5, ListNode(8, ListNode(9, ListNode(14, None)))))
    l2 = ListNode(1, ListNode(2, ListNode(12, ListNode(13, ListNode(100, None)))))

    print("-----l1-----")
    Solution().printList(l1)
    print("-----l2-----")
    Solution().printList(l2)
    print("-----l3-----")
    Solution().printList(Solution().mergeTwoLists(l1, l2))
