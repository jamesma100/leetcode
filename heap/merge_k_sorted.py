class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists):
        def printList(head):
            print("-----print list start-----")
            cur = head
            while cur:
                print("node: ", cur.val)
                cur = cur.next
            print("-----print list end------")
        dummy = cur = ListNode(0)
        heap = [(li.val, idx) for idx, li in enumerate(lists) if li]
        heapq.heapify(heap)

        while heap:
            new_val, new_idx = heapq.heappop(heap)
            cur.next = ListNode(new_val)
            cur = cur.next
            lists[new_idx] = lists[new_idx].next
            if lists[new_idx]:
                heapq.heappush(heap, (lists[new_idx].val, new_idx))
        return dummy.next


