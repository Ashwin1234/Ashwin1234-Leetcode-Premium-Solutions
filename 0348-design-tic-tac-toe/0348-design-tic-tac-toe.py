class TicTacToe:
    rows = []
    cols = []
    diagonal = 0
    antidiagonal = 0
    n = 0
    
    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0
        self.n = n
    
    def move(self, row: int, col: int, player: int):
        if player == 1:
            self.rows[row] = self.rows[row] + 1
            self.cols[col] = self.cols[col] + 1
            if row == col:
                self.diagonal = self.diagonal + 1
            if col == (len(self.cols) - row - 1):
                self.antidiagonal = self.antidiagonal + 1
        if player == 2:
            self.rows[row] = self.rows[row] - 1
            self.cols[col] = self.cols[col] - 1
            if row == col:
                self.diagonal = self.diagonal - 1
            if col == ((self.n - row) - 1):
                self.antidiagonal = self.antidiagonal - 1
        
        for i in range(0, self.n):
            if self.rows[i] == self.n or self.cols[i] == self.n:
                return 1
            elif self.rows[i] == -self.n or self.cols[i] == -self.n:
                return 2
            
            if self.diagonal == self.n or self.antidiagonal == self.n:
                return 1
            elif self.diagonal == -self.n or self.antidiagonal == -self.n:
                return 2
        return 0
            


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)