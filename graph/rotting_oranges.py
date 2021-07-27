# Return minimum number of minutes that must elapse until no cell has a 
# fresh orange. If impossible, return -1

class Solution:
    def orangesRotting(self, grid):
        # add all initially rotten oranges to queue
        q = []
        fresh_exists = False
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_exists = True
        # no rotten oranges
        if not q:
            # no fresh oranges
            if not fresh_exists:
                return 0
            # only fresh oranges exist
            else:
                return -1
        # breadth first search algo
        positions = [(0,1),(1,0),(0,-1),(-1,0)]
        time = -1
        while q:
            # initialize new queue per layer
            new_q = []
            for cur_x, cur_y in q:
                for pos in positions:
                    new_x, new_y = cur_x+pos[0], cur_y+pos[1]
                    # out of bounds
                    if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                        continue
                    # new orange infected
                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        new_q.append((new_x,new_y))
            time += 1
            q = new_q.copy()
        
        # if there are still fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return time


