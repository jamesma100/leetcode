# heaps are binary trees where each parent node has vaalue less than or equal to any of its
# children
# one implementation: heap[k] <= heap[2k+1] and heap[k] <= heap[2k+2] for all k (min heap)
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

heap = []
node1 = ListNode(2, None)
heapq.heappush(heap, (node1.val, node1))
print("heap: ", heap)
node2 = ListNode(1, None)
heapq.heappush(heap, (node2.val, node2))
print("heap: ", heap)
