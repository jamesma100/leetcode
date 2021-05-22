'''
Problem
- water flows up down left or fight, from a cell to adjacent one with equal or lower height
- return list of coordinates where water can flow to both Pacific and Atlantic oceans

Solution
- add cells adjacent to each oceans (base case)
- search from edge cells towards middle via BFS/DFS, if encounter cell with equal or larger height,
add to list
- return intersection of two results from BFS/DFS (can flow to Atlantic + can flow to Pacific)
'''
class Solution1:
    def pacificAtlantic(self, heights):
        def bfs(q):
            positions = [(0,1), (0,-1), (1,0), (-1,0)]
            vis = []
            reach = [i for i in q]
            while q:
                cur_x, cur_y = q.pop(0)
                for pos in positions:
                    new_x, new_y = cur_x+pos[0], cur_y+pos[1]
                    if new_x < 0 or new_x >= len(heights):
                        continue
                    if new_y < 0 or new_y >= len(heights[0]):
                        continue
                    if (new_x, new_y) in vis:
                        continue
                    if heights[new_x][new_y] < heights[cur_x][cur_y]:
                        continue
                    vis.append((new_x,new_y))
                    reach.append((new_x,new_y))
                    q.append((new_x,new_y))
            return reach
        m = len(heights)
        n = len(heights[0])
        pac, atl = [], []
        for i in range(m):
            pac.append((i,0))
        for j in range(1, n):
            pac.append((0,j))
        for i in range(m-1):
            atl.append((i,n-1))
        for j in range(n):
            atl.append((m-1,j))
        pac = bfs(pac)
        atl = bfs(atl)
        res = []
        for i in pac:
            for j in atl:
                if i==j:
                    res.append(i)
        return set(res)

# use DFS 
# much more efficient (288 ms vs 9000 ms)
class Solution2:
    def pacificAtlantic(self, heights):
        positions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows = len(heights)
        cols = len(heights[0])
        def dfs(vis, i, j):
            vis.add((i,j))
            for pos in positions:
                cur_x, cur_y = i+pos[0], j+pos[1]
                if cur_x < 0 or cur_x >= rows:
                    continue
                if cur_y < 0 or cur_y >= cols:
                    continue
                if heights[cur_x][cur_y] < heights[i][j]:
                    continue
                if (cur_x, cur_y) in vis:
                    continue
                dfs(vis, cur_x, cur_y)
        vis_pac, vis_atl = set(), set()
        for col in range(cols):
            dfs(vis_pac, 0, col)
            dfs(vis_atl, rows-1, col)
        for row in range(rows):
            dfs(vis_pac, row, 0)
            dfs(vis_atl, row, cols-1)
        return [i for i in vis_pac if i in vis_atl]