import random

class Board:
    def __init__(self) -> None:
        self.board = []
        self.create_board()

    def create_board(self):
        for i in range(4):
            self.board.append([0] * 4)
    
    def add_new_num(self):
        """ Adds new number """
        r = random.random()
        new_num = 2 if r < 0.9 else 4
        i = random.randint(0,3)
        j = random.randint(0,3)
        while(self.board[i][j] != 0):
            i = random.randint(0,3)
            j = random.randint(0,3)

        self.board[i][j] = new_num

    def is_full(self):
        for i in range(4):
            for j in range(4):
                if (self.board[i][j] == 0):
                    return False
        return True

    def shuffle(self, direction):
        for i in range(4):
            empty = []

            if (direction == 'u' or direction == 'l'):
                order = range(4)
            else:
                order = reversed(range(4))
            
            for j in order:
                if (direction == 'd' or direction == 'u'):
                    if (self.board[i][j] == 0):
                        empty.append(j)
                    elif(len(empty) > 0):
                        index = min(empty) if (direction == 'u') else max(empty)
                        self.board[i][index] = self.board[i][j]
                        self.board[i][j] = 0
                        empty.remove(index)
                        empty.append(j)

                else:
                    if (self.board[j][i] == 0):
                        empty.append(j)
                    elif (len(empty) > 0):
                        index = max(empty) if (direction == 'r') else min(empty)
                        self.board[index][i] = self.board[j][i]
                        self.board[j][i] = 0
                        empty.remove(index)
                        empty.append(j)

    def print_state(self):
        print(f' {self.board[0][0]} {self.board[1][0]} {self.board[2][0]} {self.board[3][0]}')
        print(f' {self.board[0][1]} {self.board[1][1]} {self.board[2][1]} {self.board[3][1]}')
        print(f' {self.board[0][2]} {self.board[1][2]} {self.board[2][2]} {self.board[3][2]}')
        print(f' {self.board[0][3]} {self.board[1][3]} {self.board[2][3]} {self.board[3][3]}')

