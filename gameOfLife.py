class Solution:
    def __init__(self, board):
        self.board = board
        self.ans = board.copy() 

    def gameOfLife(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                counter2 = self.counter_(i, j)
                if self.board[i][j] == 1:
                    if counter2 < 2:
                        self.ans[i][j] = 0
                    if counter2 > 3:
                        self.ans[i][j] = 0
                else:
                    if counter2 == 3:
                        self.ans[i][j] = 1
        self.board = self.ans

    def horizontalCheck(self, i, j):
        if j+1 < len(self.board[0]):
            if self.board[i][j+1] == 1:
                self.counter += 1
        if j-1 >= 0:
            if self.board[i][j-1] == 1:
                self.counter += 1
        
    def verticalCheck(self, i, j):
        if i-1 >= 0:
            if self.board[i-1][j] == 1:
                self.counter += 1   
        if i+1 < len(self.board):
            if self.board[i+1][j] == 1:
                self.counter += 1

    def diagonalCheck(self, i, j):
        if j+1 < len(self.board[0]) and i+1 < len(self.board):
            if self.board[i+1][j+1] == 1:
                self.counter += 1
        if j-1 >= 0 and i+1 < len(self.board):
            if self.board[i+1][j-1] == 1:
                self.counter += 1
        if i-1 >= 0 and j+1 < len(self.board[0]):
            if self.board[i-1][j+1] == 1:
                self.counter += 1
        if i-1 >= 0 and j-1 >= 0:
            if self.board[i-1][j-1] == 1:
                self.counter += 1

    def counter_(self, i, j):
        self.counter = 0
        self.horizontalCheck(i, j)
        # print(self.counter)
        self.verticalCheck(i, j)
        # print(self.counter)
        self.diagonalCheck(i, j)
        # print(self.counter,'\n')
        return self.counter


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
s1 = Solution(board)
s1.gameOfLife()
print(s1.board)