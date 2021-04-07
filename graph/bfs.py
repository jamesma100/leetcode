'''
Breadth first search

- explore nodes in layers
- raw compute shortest paths (not all graph search strategies do)
- connected components of undirected graphs ( compute its pieces )
- linear time: O(m + n) // edges + nodes
- at end of BFS, v explored <-> G has a path from s to v

Application: shortest paths

Goal: compute dist(v), fewest number of edges on a path from s to v
Extra code: initialize dist(v) = 0 if v=s, else infinity
- while considering edge(v, w):
    - if w unexplored then set dist(w) = dist(v) + 1
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
    def addEdge(self, u, v):
        self.g[u].append(v)
    def BFS(self, src):
        visited = [src]
        queue = [src]
        dist = {src: 0}

        while queue:
            s = queue.pop(0)
            print(s)
            for i in self.g[s]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
                    dist[i] = dist[s] + 1
        print(dist)

def main():
    graph = Graph()
    graph.addEdge("s", "a")
    graph.addEdge("s", "b")
    graph.addEdge("a", 'c')
    graph.addEdge('b', 'c')
    graph.addEdge('b', 'd')
    graph.addEdge('c', 'e')
    graph.addEdge('d', 'e')

    graph.BFS("s")
    return 0

if __name__ == '__main__':
    main()