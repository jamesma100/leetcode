class Solution:
    def uniquePaths(self, m, n):
        # declare array of size mxn
        ar = [[0 for j in range(n)] for i in range(m)]

        # base cases: top row and left most column only has 1 option: 
        # move from left to right, move from top to bottom respectively
        for i in range(m):
            ar[i][0] = 1
        for j in range(n):
            ar[0][j] = 1
        
        # recurrence relatioin: ar[i][j] = ar[i-1][j] + ar[i][j-1]
        for i in range(1,m):
            for j in range(1,n):
                ar[i][j] = ar[i-1][j] + ar[i][j-1]
        return ar[-1][-1]
        

if __name__ == '__main__':
    Solution().uniquePaths(3,7)