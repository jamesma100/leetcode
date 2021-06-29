class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

import heapq as hq
class Solution:
    def mergeKLists(self, lists):
        dummy = cur = ListNode(0)
        heap = [(li.val, idx) for idx, li in enumerate(lists) if li]
        hq.heapify(heap)
        while heap:
            new_val, new_idx = hq.heappop(heap)
            cur.next = ListNode(new_val)
            cur = cur.next
            lists[new_idx] = lists[new_idx].next
            # if not end of list, push back what was popped
            # with head of list updated
            if lists[new_idx]:
                hq.heappush(heap, lists[new_idx].val, new_idx)
        return dummy.next