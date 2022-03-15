import random
import numpy as np
import math

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
    
    def custom_add_new_num(self, i, j, num):
        """ Is used for determining all possible spawns of numbers """
        self.board[i][j] = num

    def move(self, direction, do_move):
        """ WASD controls: w = up, a = left, s = down, d = right """
        """Init before state, to see if board changes with chosen direction """
        before_matrix = self.board.copy()
        before = np.array(before_matrix)

        for i in range(4):
            empty = []
            changed = []
            if (direction == 'w' or direction == 'a'):
                order = range(4)
            else:
                order = reversed(range(4))
            
            for j in order:
                if (direction == 's' or direction == 'w'):
                    if (self.board[i][j] == 0):
                        empty.append(j)
                    elif(len(empty) > 0):
                        index = min(empty) if (direction == 'w') else max(empty)
                        self.board[i][index] = self.board[i][j]
                        self.board[i][j] = 0
                        empty.remove(index)
                        empty.append(j)
                        if (self.merge(i, index, direction, changed)):
                            empty.append(index)
                    else:
                        if (self.merge(i, j, direction, changed)):
                            empty.append(j)

                        
                else:
                    if (self.board[j][i] == 0):
                        empty.append(j)
                    elif (len(empty) > 0):
                        index = max(empty) if (direction == 'd') else min(empty)
                        self.board[index][i] = self.board[j][i]
                        self.board[j][i] = 0
                        empty.remove(index)
                        empty.append(j)
                        if (self.merge(index, i, direction, changed)):
                            empty.append(index)
                    else:
                        if(self.merge(j, i, direction, changed)):
                            empty.append(j)
        
        after_matrix = np.array(self.board.copy())

        if (do_move is False):
            self.board = before

        """ Check is board has changed. If not, no valid moves for this direction """
        """ We return False if no valid moves if present for this direction """
        return not (before_matrix == after_matrix).all()
     

    def merge(self, i, j, direction, changed):
        if (direction == 'd'):
            if (i > 2):
                return False
        elif (direction == 's'):
            if (j > 2):
                return False
        elif (direction == 'w'):
            if (j < 1):
                return False
        else:
            if (i < 1):
                return False

        modifier = -1 if (direction == 'w' or  direction =='a') else 1

        if (direction == 'w' or direction == 's'):
            if ((self.board[i][j] == self.board[i][j+modifier]) and self.board[i][j] != 0):
                self.board[i][j+modifier] *= 2
                self.board[i][j] = 0
                return True

        else:
            if ((self.board[i][j] == self.board[i+modifier][j]) and self.board[i][j] != 0):
                self.board[i+modifier][j] *= 2
                self.board[i][j] = 0
                return True
    
    def calculate_score(self):
        """ Also calculates new spawns into the score. The official rules does not """
        score = 0
        for i in range(4):
            for j in range(4):
                square_value = self.board[i][j]
                exponant = 1
                while(square_value > 2):
                    square_value = square_value/2
                    exponant += 1
                score += (exponant-1)* math.pow(2,exponant)
        return int(score)

    def has_won(self):
        for i in range(4):
            for j in range(4):
                if (self.board[i][j] == 2048):
                    return True
        return False

    def print_state(self):
        print(f' {self.board[0][0]} {self.board[1][0]} {self.board[2][0]} {self.board[3][0]}')
        print(f' {self.board[0][1]} {self.board[1][1]} {self.board[2][1]} {self.board[3][1]}')
        print(f' {self.board[0][2]} {self.board[1][2]} {self.board[2][2]} {self.board[3][2]}')
        print(f' {self.board[0][3]} {self.board[1][3]} {self.board[2][3]} {self.board[3][3]}')

