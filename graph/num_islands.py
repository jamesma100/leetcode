class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
            return
        if grid[i][j] != "1":
            return
        grid[i][j] = "x"
        neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        for neighbor in neighbors:
            self.dfs(grid,neighbor[0],neighbor[1])