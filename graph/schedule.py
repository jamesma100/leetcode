'''
[a, b] means must take to take a, you must take b
return True if exists a topological ordering

----- DFS algorithm for topological sort -----

L <- empty list that will contain sorted elements
while exists node without a permanent mark do
    select unmarked node n
    visit(n)

function visit(node n)
    if n has a permanent mark then
        return
    if n has a temporary mark then
        stop (not a DAG)
    mark n with temporary mark
    for each node m with an edge from n to m do
        visit(m)
    remove temporary mark from n
    mark n with permanent marrk
    add n to head of L


'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if visited[i] == 1:
                return True
            elif visited[i] == -1: # temp marker
                return False
            visited[i] = -1
            for val in graph[i]:
                if not dfs(val):
                    return False
            visited[i] = 1
            q.insert(0, i)
            return True
            
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        q = []
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            # can also do graph[course].append(prereq)
            # only difference is top ordering needs to flip
            # i.e. use q.append(i) instead of q.insert(0, i)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        