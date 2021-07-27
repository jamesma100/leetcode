class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        q = [node]
        imap = {node: Node(node.val)}
        while q:
            cur = q.pop(0)
            for neighbor in cur.neighbors:
                # if neighbor has not been visited
                if neighbor not in imap:
                    new = Node(neighbor.val)
                    imap[neighbor] = new
                    imap[cur].neighbors.append(new)
                    q.append(neighbor)
                # neighbor already visited, which means it has already
                # been copied, so retrieve copy and add to cur's copy's
                # neighbors
                # only add forward i.e. explore from cur to its neighbors
                # never from neighbors back to cur
                else:
                    imap[cur].neighbors.append(imap[neighbor])
        return imap[node]
