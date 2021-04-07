'''
Depth first search: explore aggressively, only backtrack when necessary
Runtime: O(m + n)

Guarantees
1: at end of algorithm, v marked as explored <-> exists path from s to v in G
2: runtime is O(m + n) = nodes, edges reachable from s

Reason 1: particular instantiation of generic search procedure
Reason 2: look at each node in connected component of s at most once, each edge at most twice

Application: topological ordering of a directed graph G is a labeling f of G's node such that
1. the f(v)'s are set (1, 2, ..., n)
2. (u, v) in G -> f(u) < f(v) i.e. every direcetd edge goes forward in the ordering

Motivation: sequence tasks while respecting all precedence constraints
Note: G has directed cycle -> no topological ordering

Motivation: one has to come before another
'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
    def addEdge(self, src, dst):
        self.g[src].append(dst)

    def DFS(self, graph, src, visited):
        visited.append(src)
        print(src)
        for i in graph.g[src]:
            if i not in visited:
                visited.append(i)
                self.DFS(graph, i, visited)

def main():
    graph = Graph()
    graph.addEdge("s", "a")
    graph.addEdge("s", "b")
    graph.addEdge("a", 'c')
    graph.addEdge('b', 'c')
    graph.addEdge('b', 'd')
    graph.addEdge('c', 'e')
    graph.addEdge('c', 'd')
    graph.addEdge('d', 'e')

    graph.DFS(graph, "s", [])
    return 0

if __name__ == "__main__":
    main()