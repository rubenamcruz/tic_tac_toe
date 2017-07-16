class TicTacToe:
    def __init__(self):
        self.field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1

    def play(self, player, px, py):
        if player == self.turn:
            if self.field[px][py] == 0:
                self.field[px][py] = player
                victory = self.test_victory(px, py)
                if victory:
                    return 1
                else:
                    if self.turn == 1:
                        self.turn = 2
                    else:
                        self.turn = 1
                    return 0
            else:
                return -1
        else:
            return -2

    def test_victory(self, px, py):
        i = 0
        vertical_victory = self.field[px][0] != 0 and self.field[px][0] == self.field[px][1] and self.field[px][1] == \
                                                                                                 self.field[px][2]
        horizontal_victory = self.field[0][py] != 0 and self.field[0][py] == self.field[1][py] and self.field[1][py] ==\
                                                                                                   self.field[2][py]
        diagonal_victory1 = False
        diagonal_victory2 = False
        if (px == py):
            if (px == 2):
                diagonal_victory1 = self.field[0][0] == self.field[1][1] and self.field[1][1] == self.field[2][2]
                diagonal_victory2 = self.field[0][2] == self.field[1][1] and self.field[1][1] == self.field[2][0]
            else:
                diagonal_victory1 = self.field[0][0] == self.field[1][1] and self.field[1][1] == self.field[2][2]
        elif (px + py == 4):
            diagonal_victory2 = self.field[0][2] == self.field[1][1] and self.field[1][1] == self.field[2][0]
        return vertical_victory or horizontal_victory or diagonal_victory1 or diagonal_victory2

    def reset(self):
        self.field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1