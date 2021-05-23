# dfs solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= m:
                return
            if j < 0 or j >= n:
                return
            if grid[i][j] == "x":
                return
            if grid[i][j] == "0":
                return
            if grid[i][j] == "1":
                grid[i][j] = "x"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1) 
        if not grid:
            return
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count+=1
        return count
        
# bfs solution
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        m = len(grid)
        n = len(grid[0])
        positions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(i,j):
            q = [(i,j)]
            while q:
                cur_x, cur_y = q.pop(0)
                for pos in positions:
                    new_x, new_y = cur_x+pos[0], cur_y+pos[1]
                    if new_x < 0 or new_x >= m:
                        continue
                    if new_y < 0 or new_y >= n:
                        continue
                    if grid[new_x][new_y] != "1":
                        continue
                    grid[new_x][new_y] = "x"
                    q.append((new_x,new_y))
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count+=1
        return count