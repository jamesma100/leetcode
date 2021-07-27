# Return true of word exists in grid
# Same letter cannot be used more than once

def dfs(self, board, word, i, j):
    # target is empty
    if len(word) == 0:
        return True
    # recursive call out of bounds
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    # no match found
    if word[0] != board[i][j]:
        return False
    temp = board[i][j]
    board[i][j] = "#"
    res = \
        self.dfs(board, word[1:], i, j-1) or \
        self.dfs(board, word[1:], i, j+1) or \
        self.dfs(board, word[1:], i-1, j) or \
        self.dfs(board, word[1:], i+1, j)
    # if no solution found during this iteration
    # backtrack and restore board
    if not res:
        board[i][j] = temp
    return res

def exists(self, board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if self.dfs(board, word, i, j):
                return True
    return False